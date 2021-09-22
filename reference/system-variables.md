---
uid: system-variables
---

# System Variables

The system variables are an essential part of @@name string interpolation (`DomainObject.FormatString()`). They provide additional kind of data, not related with a specific `DomainObject` or its state. For example, if we need to get the current date, we can do it directly via the system variable `$date`.

Each system variable starts with the `$` character that identifies it as such and must be surrounded with curly braces `{ }`. To the example above - `{$date}` is a legitimate system variable "selector" (a.k.a. expression) which will evaluate to the current date.

There are system variables, which value depends on a specific context - e.g. the current `Transaction` or a specific `Application`. Therefore, they are evaluated via an externally provided `Resolver`. In the table below are listed all supported system variables, their return type and the resolvers from which they are supported.

> [!WARNING]
> If a system variable does not exist, it will not be evaluated and its expression will be returned untouched. E.g. `{$non-existing-variable}` will evalaute to the same thing- `{$non-existing-variable}`. In contrast, existing system variables, but having a `null` value, will evaluate to an empty `string`.

| System Variable              | Type                  | Description                                                          | Resolver    |
| :----------------------------| :---------------------| :--------------------------------------------------------------------| :-----------|
| `$date`                      | `DateTime`            | Server system date                                                   | Globally    |
| `$time`                      | `DateTime`            | Server system time                                                   | Globally    |
| `$datetime`                  | `DateTime`            | Server system date and time                                          | Globally    |
| `$datetimeutc`               | `DateTime`            | Server system date and time in UTC                                   | Globally    |
| `$user.login`                | `string`              | Login name of the current user                                       | Globally    |
|                              |                       |                                                                      |             |
| `$rooturl`                   | `string`              | Current database URL                                                 | @@winclient |
| `$dbname`                    | `string`              | Database name                                                        | @@winclient |
| `$repository`                | `string`              | The repository name of which the domain object is part of            | @@winclient |
|                              |                       |                                                                      |             |
| `$enterprisecompany`         | `EnterpriseCompany`   | The Enterprise Company in the current (transaction) context          | @@winclient |
| `$enterprisecompanylocation` | `CompanyLocation`     | The Enterprise Company Location in the current (transaction) context | @@winclient |
| `$user.id`                   | `Guid`                | The Id of the current user                                           | @@winclient |
| `$user.name`                 | `MultilanguageString` | The full name of the current user                                    | @@winclient |
| `$role.id`                   | `Guid`                | The `Id` of the current user's role                                  | @@winclient |
| `$role.name`                 | `string`              | The name of the current user's role                                  | @@winclient |
| `$language`                  | `string`              | The language name (UI Culture) of the current user                   | @@winclient |