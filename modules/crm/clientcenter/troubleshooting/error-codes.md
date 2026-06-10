# Error codes

This page lists the Client Center error codes and explains what each one means.

Use this page when Client Center shows an explicit error code. If the problem does not include an error code, see the other pages in [Troubleshooting](index.md) and choose the one that best matches the symptom.

## Error exception codes

| Error code | Description | Resolution |
|---|---|---|
| **CC002** | The logged user is not defined as a Person. | Define a Person object for this user in order to use Client Center. |
| **CC003** | Parent party of the logged user is empty. | Set the parent party to the company on behalf of which the user is entering Client Center. |
| **CC004** | The parent party is not defined as a customer. | The parent party must be a customer in order to use Client Center. |
| **CC005** | The Client Center is not set up correctly because **Enterprise Company** is not set in the definition of the website. | Set the Enterprise Company accordingly. |
| **CC006** | The parent party does not have a customer agreement for the enterprise company of the Client Center. | Create a customer agreement for this party. |
| **CC007** | `ServicedByEnterpriseCompanyLocation` is null. | Set `ServicedByEnterpriseCompanyLocation` to the assigned `ParentParty.Customer` for this user. |
| **CC008** | Not well formatted JSON string. | Correct the JSON string in the Client Center settings. |
| **CC009** | Incorrect setup of Client Center: the `NewOrderDocumentType` option is set, but `DocumentType` is null. | Configure a valid document type for `NewOrderDocumentType`. |
| **CC010** | The logged-in user does not have a defined role. | Add the user to the `Crm_Customer_External_Access` table and assign an appropriate role. |

## Related pages

- [Cannot access a page or section](cannot-access-a-page-or-section.md)
- [New Order is not available](new-order-is-not-available.md)
- [Cannot add a user](cannot-add-a-user.md)
- [Settings changes are not applied](settings-changes-are-not-applied.md)
- [Access model and external roles](../concepts/access-model-and-external-roles.md)
- [User access and customer assignment](../user-management/concepts/user-access-and-customer-assignment.md)
