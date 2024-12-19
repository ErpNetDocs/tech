# Power Users

**Power users** is a system-defined group type providing select users with privileges elevated above those of the **Normal user-definable group** type but below the **Administrators** type. Its primary purpose is to allow users to access the **Access Permissions** panel of the **Security** section, as well as have the option to make this panel visible for normal users.

![pictures](pictures/Power_user_group_17_12.png)

## Key features

1. Users can be **manually** added to Power users groups by System Administrators.

   Unlike the **Administrators** group type, there is no checkbox or automated assignment process.

2. Power users is a **system** group type and **cannot** be edited directly by users.

   Any attempt by users to modify it will result in an **error**, ensured by bysiness rule **R37166 SecurityGroup – System Group Update Not Allowed**.

   ![pictures](pictures/Error_window_18_12.png)

### Database and System Configuration

- **GroupType Value:** The `GroupType` value is for Power Users:
  
   - **Value:** `P`
   - **Description:** PowerUsers
   - **Database Value:** `P`
   - **Model Value:** 4
   - **Display Name:** In the user interface, this group is displayed as:
     
     - **Power Users**  
