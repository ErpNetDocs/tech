---
uid: system-variables
---

# System variables

System variables are an essential part of @@name string interpolation. They provide additional kind of data, **unrelated** to a specific object or its state. For example, if you need to get the current date, you can do it directly via the system variable `$date`.

Each system variable starts with `$`, which identifies it as such, and must be surrounded by curly brackets `{ }`. 

`{$date}` is a legitimate system variable selector (or expression) which will evaluate to the current date.

There are also system variables with values depending on specific context, like the current transaction or a specific application. They're evaluated via an externally provided **resolver**. 

Below, you can find all system variables, their return type and the resolvers by which they're supported.

| System Variable              | Type                | Description                                                                                                                     |
| :----------------------------| :-------------------| :-------------------------------------------------------------------------------------------------------------------------------|
| `$date`                      | DateTime            | Server system date.                                                                                                             |
| `$time`                      | DateTime            | Server system time.                                                                                                             |
| `$datetime`                  | DateTime            | Server system date and time.                                                                                                    |
| `$datetimeutc`               | DateTime            | Server system date and time in UTC.                                                                                             |
| `$newguid`                   | string              | Serialized random Guid.                                                                                                         |
| `$dbname`                    | string              | Database name.                                                                                                                  |
| `$instance`                  | string              | Current database instance. Equals to `$rooturl`, but without the scheme prefix (i.e., *https://*)                               |
| `$rooturl`                   | string              | Current database URL.                                                                                                           |
| `$repository`<sup>**1**</sup>   | string              | The repository name the object is part of.                                                                                      |
| `$entity`<sup>**1**</sup> (**obsolete**)     | string              | The entity name the object is part of.                                                                                          |
| `$idlist`<sup>**1**</sup>                    | string              | Comma-separated list with Ids (serialized Guid) of the current context. For example, the selected rows in a **Navigator Form**. |
| `$enterprisecompany`         | EnterpriseCompany   | The enterprise company in the current (transaction) context.                                                                    |
| `$enterprisecompanylocation` | CompanyLocation     | The enterprise company Location in the current (transaction) context.                                                           |
| `$user`                      | User                | User instance of the current user.                                                                                              |
| `$role`                      | Role                | Role instance of the user's role.                                                                                               |
| `$language`                  | string              | The language name (UI culture) of the current user.                                                                             |

<sup>**1**</sup> When applicable. E.g., `$repository` can't be evaluated when there's no repository context where the interpolation is performed.
