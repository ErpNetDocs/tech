# **Power Users**

The Power Users role is a system-defined group created to provide select users with elevated privileges above Normal Users but below full administrative rights.

The primary purpose of this role is to allow users to manage security settings without accessing other administrator-level controls.

## **Key Features and Functionality**

1. **Access Permissions Panel**

   - Power Users have exclusive access to the Security (Access Permissions) panel, enabling them to manage access rights for other users.
   - This panel is hidden for Normal Users.

2. **Manual User Assignment**

   - Users are manually added to the Power Users group by system administrators. Unlike the Administrators group, there is no checkbox or automated assignment process.

3. **Restricted Group Management**

   - The Power Users group is a system group and cannot be edited directly by users.
   - Any attempt to modify this group will result in an error, similar to the behavior for the Administrators group.

4. **Database and System Configuration**

   - **GroupType Value:** The `GroupType` value is for Power Users:
     - **Value:** `P`
     - **Description:** PowerUsers
     - **Database Value:** `P`
     - **Model Value:** 4
   - **Display Name:** In the user interface, this group is displayed as:
     - ** Power Users **

## **Implementation Details**

1. **Group Creation**

   - A new system-defined group is added to the `Systems.Security.Groups` entity with the type `PowerUsers`.
  
   ![pictures](pictures/Power_user_group_17_12.png)

2. **UI Restrictions**

   - The Power Users group is displayed in the program’s dropdown list as “Power Users”.
   - Editing restrictions for this group are enforced by front-end validation and back-end rules (e.g., error thrown on unauthorized modification attempts).

3. **Business Rule Enforcement**

   - Rule **R37166 SecurityGroup – System Group Update Not Allowed** ensures that users cannot modify the Power Users group configuration.

The Power Users role enhances system functionality by delegating access control responsibilities to designated users without compromising administrative security. 

This role bridges the gap between Normal Users and Administrators, ensuring a scalable and secure management framework.
