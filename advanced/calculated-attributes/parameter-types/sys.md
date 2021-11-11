# SYS

SYS is used with system variables.

They can be applied when you need to acquire information for the current user, date, time, enterprise company and others.

Here's a list of those variables:

| Value                       | Description                                                  | Example (returned value)             |
| --------------------------- | ------------------------------------------------------------ | ------------------------------------ |
| Login                       | The login of the user that is logged into the program. | admin                                |
| UserId                      | The ID of the user that is currently logged in the program.  | 9da64839-a8d0-491d-aebb-4d18fa42b014 |
| RoleName                    | The name of role that is currently set for the user.         | Administration                       |
| RoleId                      | The role that is currently set for the user.                 | c764ff2b-38ca-4906-893a-2a21a1691f43 |
| Today                       | Current date.                                                | 23.6.2017 0:00:00                    |
| Now                         | Current date-time from the server time zone.                 | 23.6.2017 13:25:33                   |
| UtcNow                      | Current date-time in Coordinated Universal Time (UTC)        | 23.6.2017 10:25:33                   |
| EnterpriseCompanyId         | The ID of the enterprise company that is set for the user. | b0e80577-fbbe-4c9b-811e-20b6c6dd465f |
| EnterpriseCompanyLocationId | The ID of the enterprise company location that is currently set for the user. | f2947790-e21f-4def-b533-fdc00a343ce6 |


**Example:**

```
10: GETVALUE SYS:Login
```

The line returns the login of the user that is currently logged into the program.
