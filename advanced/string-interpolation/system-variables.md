---
uid: system-variables
---

# System variables

System variables are an essential part of @@name string interpolation. They provide additional kind of data, **unrelated** to a specific object or its state. For example, if you need to get the current date, you can do it directly via the system variable `$date`.

Each system variable starts with `$`, which identifies it as such, and must be surrounded by curly brackets `{ }`. 

`{$date}` is a legitimate system variable selector (or expression) which will evaluate to the current date.

There are also system variables with values depending on specific context, like the current transaction or a specific application. They're evaluated via an externally provided **resolver**. 

Below, you can find all system variables, their return type and the resolvers by which they're supported.

> [!WARNING]
> 
> If a system variable doesn't exist, it won't be evaluated and its expression will be returned **untouched**. <br> `{$non-existing-variable}` will evalaute to the same thing- `{$non-existing-variable}`. <br> In contrast, existing system variables with a null value will evaluate to an **empty string**.


| System Variable              | Type                | Description                                                                                                                     | Resolver    |
| :----------------------------| :-------------------| :-------------------------------------------------------------------------------------------------------------------------------| :-----------|
| `$date`                      | DateTime            | Server system date.                                                                                                             | Globally    |
| `$time`                      | DateTime            | Server system time.                                                                                                             | Globally    |
| `$datetime`                  | DateTime            | Server system date and time.                                                                                                    | Globally    |
| `$datetimeutc`               | DateTime            | Server system date and time in UTC.                                                                                             | Globally    |
| `$repository`                | string              | The repository name the object is part of.                                                                                      | Globally    |
| `$newguid`                   | string              | Serialized random Guid.                                                                                                         | Globally    |
|                              |                     |                                                                                                                                 |             |
| `$rooturl`                   | string              | Current database URL.                                                                                                           | @@winclient |
| `$instance`                  | string              | Current database instance. Equals to `$rooturl`, but without the scheme prefix (i.e., *https://*)                                                                                            | @@winclient |
| `$dbname`                    | string              | Database name.                                                                                                                  | @@winclient |
| `$entity` (**obsolete**)     | string              | The entity name the object is part of.                                                                                          | @@winclient |
| `$idlist`                    | string              | Comma-separated list with Ids (serialized Guid) of the current context. For example, the selected rows in a **Navigator Form**. | @@winclient |
|                              |                     |                                                                                                                                 |             |
| `$enterprisecompany`         | EnterpriseCompany   | The enterprise company in the current (transaction) context.                                                                    | @@winclient |
| `$enterprisecompanylocation` | CompanyLocation     | The enterprise company Location in the current (transaction) context.                                                           | @@winclient |
| `$user`                      | User                | User instance of the current user.                                                                                              | @@winclient |
| `$role`                      | Role                | Role instance of the user's role.                                                                                               | @@winclient |
| `$language`                  | string              | The language name (UI culture) of the current user.                                                                             | @@winclient |