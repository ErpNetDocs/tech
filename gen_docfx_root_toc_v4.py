#!/usr/bin/env python3
"""
Generate/Update DocFX toc.yml for the *current folder only* + (optional) parent update,
with the ability to auto-create missing `index.md` and `toc.yml` in direct subfolders.

Anchors disabled: YAML output is forced to have **no** anchors (&id001/*id001) via a custom dumper.

Typical usage
  python gen_docfx_root_toc_v4.py --root ./docs/operators --write --auto-create-subdirs --update-parent
"""
from __future__ import annotations

import argparse
import fnmatch
from pathlib import Path
import re
import sys
from typing import List, Dict, Any, Tuple

try:
    import yaml  # PyYAML
except Exception as e:
    print("PyYAML is required: pip install pyyaml", file=sys.stderr)
    raise

# ---- Disable YAML anchors (no &id001 / *id001) ----
class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True

MD_EXTS = {".md", ".markdown"}
DEFAULT_INDEX_NAMES = ["index.md", "readme.md"]
DEFAULT_EXCLUDES = [
    ".git", ".github", ".vscode", ".idea", "_site", "_build", "_output", "obj", "bin",
]

FRONT_MATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
H1_RE = re.compile(r"^#\s+(.+)$", re.MULTILINE)
NUM_PREFIX_RE = re.compile(r"^(\d{1,4})[\-_\s]+(.*)$")

# -------------------- utilities --------------------

def load_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(encoding="utf-8", errors="ignore")


def parse_title_from_markdown(md_path: Path) -> str:
    text = load_text(md_path)
    m = FRONT_MATTER_RE.match(text)
    if m:
        try:
            fm = yaml.safe_load(m.group(1)) or {}
            for key in ("toc_title", "title"):
                v = fm.get(key)
                if isinstance(v, str) and v.strip():
                    return v.strip()
        except Exception:
            pass
    m = H1_RE.search(text)
    if m:
        return m.group(1).strip()
    return humanize_name(md_path.stem)


def humanize_name(name: str) -> str:
    m = NUM_PREFIX_RE.match(name)
    if m:
        name = m.group(2)
    name = name.replace("-", " ").replace("_", " ")
    return " ".join(w.capitalize() if not w.isupper() else w for w in name.split())


def sort_key_for_name(s: str) -> Tuple[int, str]:
    m = NUM_PREFIX_RE.match(s)
    if m:
        try:
            return (int(m.group(1)), m.group(2))
        except Exception:
            pass
    return (1_000_000, s)


def sort_key_for_path(p: Path) -> Tuple[int, str]:
    return sort_key_for_name(p.name)


def match_any(path: Path, patterns: List[str]) -> bool:
    if not patterns:
        return False
    s = path.name
    for pat in patterns:
        if fnmatch.fnmatch(s, pat):
            return True
    return False

# -------------------- build desired items --------------------

def ensure_subdir_scaffolding(root: Path, index_names: List[str], verbose: bool) -> None:
    """Ensure each direct subfolder has index.md and toc.yml (minimal)."""
    for d in sorted([p for p in root.iterdir() if p.is_dir()], key=sort_key_for_path):
        idx = next(((d / cand) for cand in index_names if (d / cand).exists()), None)
        if not idx:
            idx = d / "index.md"
            if not idx.exists():
                idx.write_text(f"# {humanize_name(d.name)}\n", encoding="utf-8")
                if verbose:
                    print(f"[CREATE] {idx}")
        sub_toc = d / "toc.yml"
        if not sub_toc.exists():
            sub_toc.write_text("- name: Overview\n  href: index.md\n", encoding="utf-8")
            if verbose:
                print(f"[CREATE] {sub_toc}")


def build_desired_items(
    root: Path,
    index_names: List[str],
    excludes: List[str],
    include_root_files: bool,
    require_sub_toc: bool,
    require_sub_index: bool,
    verbose: bool,
) -> List[Dict[str, Any]]:
    items: List[Dict[str, Any]] = []

    # Overview (root landing)
    root_index = next(((root / cand) for cand in index_names if (root / cand).exists()), None)
    if root_index and root_index.is_file():
        overview_name = parse_title_from_markdown(root_index)
        items.append({"name": overview_name or "Overview", "href": root_index.name})
        if verbose:
            print(f"[ROOT] index: {root_index.name} -> '{overview_name}'")

    # Root-level extra pages
    if include_root_files:
        for f in sorted(root.iterdir(), key=sort_key_for_path):
            if f.is_file() and f.suffix.lower() in MD_EXTS and f != root_index and not match_any(f, excludes):
                items.append({"name": parse_title_from_markdown(f), "href": f.name})
                if verbose:
                    print(f"[ROOT] file: {f.name}")

    # Direct subfolders
    subdirs = [d for d in root.iterdir() if d.is_dir() and not match_any(d, excludes)]
    for d in sorted(subdirs, key=sort_key_for_path):
        sub_index = next(((d / cand) for cand in index_names if (d / cand).exists()), None)
        sub_toc = d / "toc.yml"
        if require_sub_toc and not sub_toc.exists():
            if verbose:
                print(f"[SKIP] {d.name} (no toc.yml and --require-sub-toc)")
            continue
        if require_sub_index and not sub_index:
            if verbose:
                print(f"[SKIP] {d.name} (no index and --require-sub-index)")
            continue

        if sub_index:
            name = parse_title_from_markdown(sub_index)
            topic_href = f"{d.name}/{sub_index.name}"
        else:
            name = humanize_name(d.name)
            topic_href = None

        entry: Dict[str, Any] = {"name": name, "href": f"{d.name}/toc.yml"}
        if topic_href:
            entry["topicHref"] = topic_href
        items.append(entry)
        if verbose:
            print(f"[SUBDIR] {d.name} -> name='{name}', href='{entry['href']}', topicHref='{entry.get('topicHref','-')}'")

    return items

# -------------------- merge/update helpers --------------------

def read_yaml_list(path: Path) -> List[Dict[str, Any]]:
    if not path.exists():
        return []
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        if isinstance(data, list):
            return data
    except Exception:
        pass
    return []


def write_yaml_list(path: Path, items: List[Dict[str, Any]]):
    yaml_str = yaml.dump(items, sort_keys=False, allow_unicode=True, width=1000, Dumper=NoAliasDumper)
    path.write_text(yaml_str, encoding="utf-8")


def upsert_current_toc(toc_path: Path, desired: List[Dict[str, Any]], verbose: bool) -> None:
    """Update existing toc.yml preserving manual items and order; create if missing."""
    existing = read_yaml_list(toc_path)

    if not existing:
        write_yaml_list(toc_path, desired)
        if verbose:
            print(f"[WRITE] {toc_path} (new)")
        return

    # Map desired by href for quick lookup
    desired_by_href = {it.get("href"): it for it in desired if it.get("href")}

    # Ensure Overview entry is updated and kept at first position if already first
    def is_overview(item: Dict[str, Any]) -> bool:
        href = (item.get("href") or "").lower()
        return href in {"index.md", "readme.md"}

    # Try to locate overview in existing
    overview_desired = next((it for it in desired if is_overview(it)), None)

    updated: List[Dict[str, Any]] = []
    seen_hrefs = set()

    for it in existing:
        href = it.get("href")
        if href in desired_by_href:
            d = desired_by_href[href]
            # update fields from desired
            merged = dict(it)
            merged["name"] = d.get("name", merged.get("name"))
            if "topicHref" in d:
                merged["topicHref"] = d["topicHref"]
            else:
                if "topicHref" in merged:
                    del merged["topicHref"]
            updated.append(merged)
            seen_hrefs.add(href)
        else:
            # keep manual/unknown items as-is
            updated.append(it)

    # If overview missing in existing, insert it at the top
    if overview_desired and not any(is_overview(x) for x in updated):
        updated.insert(0, overview_desired)

    # Append new desired items not present yet, sorted by numeric prefix of href
    missing = [it for h, it in desired_by_href.items() if h not in seen_hrefs]
    missing.sort(key=lambda it: sort_key_for_name(it.get("href") or it.get("name", "")))
    updated.extend(missing)

    write_yaml_list(toc_path, updated)
    if verbose:
        print(f"[WRITE] {toc_path} (updated)")

# -------------------- parent update --------------------

def update_parent_toc(child_root: Path, index_names: List[str], verbose: bool) -> None:
    parent = child_root.parent
    if parent == child_root:
        if verbose:
            print("[PARENT] No parent to update")
        return

    parent_toc = parent / "toc.yml"
    items = read_yaml_list(parent_toc)

    sub_index = next(((child_root / cand) for cand in index_names if (child_root / cand).exists()), None)
    if sub_index:
        name = parse_title_from_markdown(sub_index)
        topic_href = f"{child_root.name}/{sub_index.name}"
    else:
        name = humanize_name(child_root.name)
        topic_href = None

    desired = {"name": name, "href": f"{child_root.name}/toc.yml"}
    if topic_href:
        desired["topicHref"] = topic_href

    hrefs = [it.get("href") for it in items]
    if desired["href"] in hrefs:
        for it in items:
            if it.get("href") == desired["href"]:
                it["name"] = desired["name"]
                if topic_href:
                    it["topicHref"] = topic_href
                else:
                    it.pop("topicHref", None)
                break
    else:
        items.append(desired)
        items.sort(key=lambda it: sort_key_for_name(it.get("href") or it.get("name", "")))

    write_yaml_list(parent_toc, items)
    if verbose:
        print(f"[PARENT] Updated {parent_toc} with entry: {desired}")

# -------------------- CLI --------------------

def parse_args(argv: List[str]):
    p = argparse.ArgumentParser(description="Generate/Update a single DocFX toc.yml for the current folder; optionally update parent and auto-create subdirs")
    p.add_argument("--root", default=".", help="Folder to scan (default: .)")
    p.add_argument("--write", action="store_true", help="Write current folder's toc.yml (default: dry-run)")
    p.add_argument("--no-write-current", action="store_true", help="Skip writing current folder's toc.yml (useful with --update-parent)")
    p.add_argument("--update-parent", action="store_true", help="Update parent folder's toc.yml to include this folder")
    p.add_argument("--auto-create-subdirs", action="store_true", help="Ensure each direct subfolder has index.md and toc.yml (minimal)")
    p.add_argument("--index-names", default=",".join(DEFAULT_INDEX_NAMES), help="Comma-separated index candidates (default: index.md,readme.md)")
    p.add_argument("--exclude", default=",".join(DEFAULT_EXCLUDES), help="Comma-separated patterns to exclude")
    p.add_argument("--include-root-files", action="store_true", help="Include non-index markdown files from root")
    p.add_argument("--require-sub-toc", action="store_true", help="Only include subfolders that already contain toc.yml")
    p.add_argument("--require-sub-index", action="store_true", help="Only include subfolders that contain index.md/readme.md")
    p.add_argument("--verbose", action="store_true", help="Verbose output")
    return p.parse_args(argv)


def main(argv: List[str]) -> int:
    args = parse_args(argv)
    root = Path(args.root).resolve()
    if not root.exists():
        print(f"Root not found: {root}", file=sys.stderr)
        return 2

    index_names = [s.strip() for s in args.index_names.split(",") if s.strip()]
    excludes = [s.strip() for s in args.exclude.split(",") if s.strip()]

    if args.auto_create_subdirs:
        ensure_subdir_scaffolding(root, index_names=index_names, verbose=args.verbose)

    desired_items = build_desired_items(
        root=root,
        index_names=index_names,
        excludes=excludes,
        include_root_files=args.include_root_files,
        require_sub_toc=args.require_sub_toc,
        require_sub_index=args.require_sub_index,
        verbose=args.verbose,
    )

    toc_path = root / "toc.yml"

    if not args.no_write_current:
        if args.write:
            upsert_current_toc(toc_path, desired_items, verbose=args.verbose)
        else:
            existing = read_yaml_list(toc_path)
            print(f"--- {toc_path} (dry-run, existing={'yes' if existing else 'no'}) ---")
            print(yaml.dump(desired_items, sort_keys=False, allow_unicode=True, width=1000, Dumper=NoAliasDumper))
            print("--- end ---")

    if args.update_parent:
        update_parent_toc(root, index_names=index_names, verbose=args.verbose)

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

