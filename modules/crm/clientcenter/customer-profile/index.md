# Customer Profile

The **Customer Profile** section in Client Center gives external users access to company information and customer-related files for the currently selected customer.

This section is intended to provide a customer-facing view of the registered customer data together with files that are attached directly to the customer record and shared for external access.

[screenshot: client-center/customer-profile/cc-customer-profile-overview-01-customer-profile-section.png]

## What users can do in Customer Profile

In the Customer Profile section, users can typically:

- review the basic company information for the current customer;
- view identifiers such as **UIN** and **VAT number**;
- access customer-related files when such files are available and shared for external access;
- download visible files directly from the profile page.

Customer Profile is intended to give users a single place where they can review the current customer identity and, when applicable, access shared customer documents.

## Role-based visibility in Customer Profile

Access to Customer Profile is part of the Client Center access model.

All external roles can access the basic customer information available in this section.

Additional file-related visibility depends on both:

- the user's assigned external role;
- the sharing configuration of the file itself.

Users with **L40 - Billing** and above can access the dedicated **Files** panel in Customer Profile when eligible files are available.

For more information, see [Access model and external roles](../concepts/access-model-and-external-roles.md).

## Customer Profile and customer-specific context

Customer Profile always reflects the currently selected customer.

When a user has access to multiple customers, the information shown in this section belongs only to the active customer context. After switching to another customer, the Customer Profile page updates to show that customer's information and available files.

This keeps the section aligned with the customer-specific access model used throughout Client Center.

For more information, see [Multi-customer login](../concepts/multi-customer-login.md).

[screenshot: client-center/customer-profile/cc-customer-profile-overview-02-customer-information-and-files.png]

## Customer information and files

Customer Profile combines two related kinds of information:

- the customer's registered company data;
- the files attached to the customer record and shared for both internal and external users.

This makes Customer Profile different from the **Orders** and **Billing** sections, where files are attached to individual documents such as orders or invoices.

In Customer Profile, the files belong to the customer record itself and are intended for shared company-level documents such as contracts, annexes, agreements, catalogs, and similar materials.

For more information, see:

- [Customer information](concepts/customer-information.md)
- [Files in Customer Profile](concepts/files-in-customer-profile.md)
- [File visibility and downloads](../concepts/file-visibility-and-downloads.md)

## Downloading files from Customer Profile

When customer-related files are available and externally shared, users can download them directly from the **Files** panel in Customer Profile.

If no accessible customer files are available, the page shows the message **No documents available.**

For task-oriented guidance, see [Download files from Customer Profile](operations/download-files-from-customer-profile.md).

## In this section

### Operations

Use the Operations pages for task-oriented guidance:

- [Operations overview](operations/index.md)
- [Download files from Customer Profile](operations/download-files-from-customer-profile.md)

### Concepts

Use the Concepts pages to understand how Customer Profile works:

- [Concepts overview](concepts/index.md)
- [Customer information](concepts/customer-information.md)
- [Files in Customer Profile](concepts/files-in-customer-profile.md)

## Related sections

- [Home and navigation](../concepts/home-and-navigation.md)
- [File visibility and downloads](../concepts/file-visibility-and-downloads.md)
- [Troubleshooting](../troubleshooting/index.md)

## Summary

The Customer Profile section gives users access to company information and customer-related files for the active customer.

It reflects the current customer context, exposes the customer's registered identifiers, and provides access to shared customer files when those files are configured for external visibility.
