## Security

### Project-based access control

To enhance confidentiality and governance in **Agile PM**, @@name introduces project-level access control using Access Keys. This security model ensures that only authorized users and teams can view or act on Cases associated with sensitive projects.

Access permissions are defined centrally within the **Access Permissions** panel of each Project and include:

- **Basic permissions:**
  - **Update** – modify the project or its related Cases
  - **Delete** – remove the project
  - **Administer** – full control over the project setup and its security settings

- **Extended permissions** (specific to Agile PM Cases):
  - **Change to CONSIDER**
  - **Change to READY**
  - **Change to IN PROGRESS**
  - **Change to WAITING**
  - **Change to RESOLVED**
  - **Change to CLOSED**

`[screenshot]`

These extended permissions regulate **status transitions** for Cases under the project.  
For example, if a user only has the "Change to READY" right for a project, they can only move Cases into that state — and not others.

> [!Note]
> These permissions are automatically inherited by all Cases linked to the Project.

When a user attempts an unauthorized state change, they receive a clear error message indicating the lack of permission to perform that specific transition for the project’s Cases.


### Visibility filtering

To prevent unauthorized access to sensitive Cases, the system applies secure filtering at the data level:

- In the **Cases navigator**, users only see Cases linked to Projects for which they have access rights.
- In the **Global Search**, Cases outside the user's access scope are excluded from the results.

This ensures that users can only discover and interact with project information that aligns with their granted permissions, reinforcing data confidentiality across the **Agile PM** module.
