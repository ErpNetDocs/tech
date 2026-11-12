# Access permissions for documents

Access permissions determine which users can access protected resources in
ERP.net and which actions they can perform on them.

ERP.net uses **access keys** to protect resources, including entity types and
individual records. Permissions are assigned to **user groups**, and users
receive permissions through their group memberships.

Access to a resource and permission to perform an action are not the same.
For example, a user may be able to open a record without being allowed to
update or delete it.

## Access permissions on individual documents

An individual document can have its own access key. The permissions associated
with that key control access to the document and actions such as:

- **Update** — change the document.
- **Delete** — delete the document.
- **Administer** — manage its access permissions.

For example, a group may have access to open a sales order but not permission
to update it.

When checking a user's permissions, consider **all groups** the user belongs
to. A permission granted through one group is not removed simply because it is
unchecked for another group.

Read the domain model [HERE](https://docs.erp.net/model/entities/General.Documents.Documents.html#accesskey)

## Permissions and document states

A document's **state** and a user's **permissions** are separate considerations:

- The state determines which changes and transitions are generally allowed.
- Permissions determine whether the user is allowed to perform an action.

For example, a document in the **New** state can generally be edited, but
the user must also have the applicable permissions. Conversely, having update
permission does not override restrictions imposed by the document's state.

See also

- [Security in ERP.net](https://info.erp.net/information/system-information/security.html)
- [Document states](https://docs.erp.net/tech/concepts/documents/states.html)

## Document type access permissions

A document type also has its own access permissions. Some apply to the
**type definition**, while others control specific actions on **documents of
that type**.

The **Access Permissions** panel for a document type contains two kinds of permissions:

| Permission | What it controls |
| --- | --- |
| **Update, Delete, Administer** | Changes to the document type definition and its security. |
| **Release Documents, Complete Documents, Void Documents**, and other named document actions | The corresponding actions on documents of that type. |

See the [Document Types reference](https://docs.erp.net/model/entities/Systems.Documents.DocumentTypes.html).

![picture](accessdoctype.png)

## Example 1: Editing but not releasing

A user has no Update, Delete, Administer or Release Documents permission on the document type *Seller Order*.

- He cannot edit the **document type definition**.
- He may still be able to edit and save an order of that type in a state lower than "Released"
- He cannot release the order unless he receives "Release Documents" permission 

A document's state and its permissions are separate checks: **New** generally allows editing, but it does not override access restrictions. See [Document States](https://docs.erp.net/tech/concepts/documents/states.html).

## Example 2: Restricting a specific document

To restrict editing of a particular document, the document itself can have an **access key** with its own Update, Delete and Administer permissions. Restricting the document type definition does not automatically apply those restrictions to the document itself.

See the [Documents reference](https://docs.erp.net/model/entities/General.Documents.Documents.html).

## Check all group memberships

If a user belongs to multiple groups, check all of them: a permission may be granted through another group.

See [Security](https://info.erp.net/information/system-information/security.html).
