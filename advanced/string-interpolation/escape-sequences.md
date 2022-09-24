---
uid: escape-sequences
---


# Escape sequences

An escape sequence is a sequence of characters that isn't represented when used inside a character or string literal, but it's translated into another character or a sequence of characters.

Let's form the most typical example of an escape sequence as a question:

_How do you put a "new line" in a single input field?_

If you can't thing of it now, how about this:

`\r\n`

Yes, that's pretty standard. And yes - @@erpnet supports it. So you can write down something like:

`Hello, \r\n\ world!`

and the interpolated string will be this:

```
Hello,
world!
```

## Syntax

The escape sequence's sytnax is quite straightforward. Just put a `\` (backslash) before the *escape character*. E.g.,

| Escape sequence | Interpretation |
| --- | --- |
| \\' | ' |
| \\" | " |
| \\{ | { |
| \\} | } |
| \\r | NEW LINE |
| \\R | R |

Did you notice the last row of the table? 

> [!NOTE]
> 
> Escaping sequences in @@erpnet is case SENSITIVE.

That's the reason why `\R` is different than `\r`.

## Supported escape sequences

The following escape sequences are defined and supported in @@erpnet.

| Escape sequence | Interpretation | @@erpnet representation (ASCII) |
| --- | --- |
| \\r | NEW LINE | #13#10 |
| \\n | NEW LINE | #13#10 |
| \\r\\n | NEW LINE | #13#10 |


_*NEW LINE is platform dependent_.

Any other escape sequence that not part of the supported ones will be escaped by removing the backslash. E.g., 

* This: `\z`, will become this: `z`
* `\A` - `A`
* etc

## Caution about Windows file paths

Because file paths in Windows consist of backslashes- e.g.,

```
C:\MyFolder\file.txt
```

They themselves have to be escaped. That's done by doubling them. So, when you need to visualize a backslash, you should write `\\` instead of `\`. Or to the example above, the path should look like this:

```
C:\\MyFolder\\file.txt
```