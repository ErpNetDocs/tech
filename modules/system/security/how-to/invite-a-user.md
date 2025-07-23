# How to invite a user to a WEB instance

To create an account for a new user, an **email invitation** must be sent to this user from you. The process involves two participnats - tha administrator of the instance and the new user.

First the administrator must create a new user in the system:

1. Go to “Security” module and open navigator "Users"

2. On the header line (the horizontal grey line) find the “plus” button and click on it
   This will open a form that you should fill in. It looks like this:

3. Fill in several required fields
   * Login - the login name of the user
   * Name - the name of the user
   * Email - a valid email address, to receive the invitation
   * User Type - this is a very important field at this point. Clicking on it will open a dropdown menu. You must chose “Invitation Internal (No login)“

4. Assign a role for the new user - you can do it now, or at a later stage.
   This is done in panel "Roles".
   Find the “Plus” icon on the right side and add a new line in the panel. In column "Role" choose an available role e.g. Salesperson, Manager, Worker etc.
   You can assign several roles per user.

5. Now find the “Save” button with a downward strike. Click the downward strike and save the new user with "Save and reload" button.

   At this stage a new user is created and saved in the platform. It is time to send the invitation.

6. On the header line, click “Run”.

7. Choose option "Send invitation mail"
   The system will ask for confirmation. Confirm by clicking OK.
   This sends an email to the user

8. The user will receive an email from sender e-mail "notification@erpnet.info", Subject: "Invitation to join {InstanceName.my.erp.net}."

9. The user must click on the **Create Account** link and will be transferred to a form.
   In the form, Login and Name are already filled - Do not change them!
   Input only a 8 character password.
   Confirm.
   
11. The user can now login in the platform with the given login and the set password.
12. The User type will the automatically changed to “Internal” and will be assigned to the “Everybody” User Group

    Note: If a role has not been assigned, after the ogin, the user might encounter an error like this:
    "The currently logged user {UserName} has no addigned roles. Please contact your system administrator to configure the roles for user {UserName}"
    In this case he should seek assistance from the administrator.
    
   
