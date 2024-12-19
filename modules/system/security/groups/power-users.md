# Power Users

**Power users** is a system-defined group type providing select users with privileges elevated above those of the **Normal user-definable group** type but below the **Administrators** type. Its primary purpose is to allow users to access the **Access Permissions** panel of the **Security** section, as well as have the option to make this panel visible for normal users.

The Power Users role enhances system functionality by delegating access control responsibilities to designated users without compromising administrative security. 

This role bridges the gap between Normal Users and Administrators, ensuring a scalable and secure management framework.

![pictures](pictures/Power_user_group_17_12.png)

## Key features

Users can be **manually** added to the Power users group by System Administrators. 

Unlike the **Administrators** group type, there is no checkbox or automated assignment process.

The Power Users group is a system group and cannot be edited directly by users.

Any attempt to modify this group will result in an **error**.

Rule **R37166 SecurityGroup – System Group Update Not Allowed** ensures that standard users cannot modify the **Power users** group.
  
![pictures](pictures/Error_window_18_12.png)

**Database and System Configuration**

- **GroupType Value:** The `GroupType` value is for Power Users:
  
   - **Value:** `P`
   - **Description:** PowerUsers
   - **Database Value:** `P`
   - **Model Value:** 4
   - **Display Name:** In the user interface, this group is displayed as:
     - **Power Users**  
