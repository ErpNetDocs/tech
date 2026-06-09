# Shared grid behavior

Client Center uses a shared grid behavior in the pages that display lists of records.

This means that pages such as **Orders**, **Invoices**, **Due Payments**, and **Payment History** follow the same general grid interaction model. Once users understand how the grid works in one section, they can use the same actions and controls in the others.

The purpose of this shared behavior is to provide a consistent way to review, filter, group, and organize record lists across Client Center.

[screenshot: client-center/concepts/shared-grid-behavior/cc-concepts-shared-grid-behavior-01-grid-overview.png]

## Where the shared grid is used

The shared grid behavior is used in Client Center pages that display tabular business data.

Typical examples include:

- **Orders**;
- **Invoices**;
- **Due Payments**;
- **Payment History**.

These pages may show different business objects, but the grid interaction model remains the same.

For more information about these pages, see:

- [Orders page](../orders/concepts/orders-page.md)
- [Invoices page](../billing/concepts/invoices-page.md)
- [Due Payments page](../billing/concepts/due-payments-page.md)
- [Payment History page](../billing/concepts/payment-history-page.md)

## What the grid allows users to do

The shared grid allows users to work with record lists in a flexible way.

Depending on the page and the available data, users can typically:

- sort records by column values;
- filter the visible records;
- search within the grid;
- group records by selected columns;
- choose which columns are visible;
- save and restore a preferred grid layout;
- review totals and summaries for numeric values.

These capabilities help users focus on the information that is most relevant to their current task.

## Sorting and browsing records

Grid columns can be used to sort the listed records.

Sorting helps users quickly reorganize the list by values such as document number, date, amount, status, or due date, depending on the page.

This is especially useful when users need to browse long lists and identify the most recent, most urgent, or highest-value records more easily.

## Filtering and search

The shared grid supports filtering and search so that users can reduce the visible result set and focus on specific records.

Filtering can be used to limit the records shown according to selected values or conditions. Search can be used to find records that contain specific text or numbers.

Together, these options make it easier to work with larger datasets without leaving the current page.

[screenshot: client-center/concepts/shared-grid-behavior/cc-concepts-shared-grid-behavior-02-filter-and-search.png]

## Grouping records

The grid can group records by selected columns.

Grouping helps users organize the visible records into logical sections based on a shared value, such as status, document type, period, or another available field.

This is useful when users want to review records by category instead of as one flat list.

## Showing and hiding columns

Users can control which columns are visible in the grid.

This makes it possible to adapt the view according to the information that matters most in a given scenario. For example, users can choose to keep only the most relevant fields visible and hide columns that are not currently needed.

Because different Client Center pages expose different data, the exact available columns may vary, but the interaction model for showing and hiding columns remains the same.

## Saving and restoring a layout

The shared grid allows users to save and restore a preferred layout.

A saved layout can preserve grid settings such as:

- visible columns;
- column order;
- grouping;
- sorting;
- other grid-related view preferences.

This allows users to keep a familiar working view instead of reconfiguring the grid each time they open the page.

[screenshot: client-center/concepts/shared-grid-behavior/cc-concepts-shared-grid-behavior-03-column-chooser-and-layout.png]

## Summaries and totals

When the page includes numeric data, the grid can display totals and summary values.

This is particularly useful in pages where users need a quick overview of amounts, balances, or other numeric indicators without opening each record individually.

The summary behavior depends on the data shown in the specific page, but the presentation follows the same general grid model across Client Center.

## Shared behavior across sections

The same grid principles apply across the different Client Center sections that use list pages.

This consistency reduces the learning effort for external users. Once they know how to work with one list page, they can apply the same approach in the others.

For example, a user who understands filtering and grouping in **Orders** can use the same interaction pattern in **Invoices** or **Due Payments**.

## Relationship to roles and visible data

The grid interaction model is shared, but the actual data shown in the grid still depends on the user's role and access scope.

This means that:

- the same type of grid can show different columns or values depending on the page;
- some users may see more detailed commercial information than others;
- the visible records can also be limited by restrictions such as **Days Back Access**.

For example, users with order access that excludes prices can still use the same grid functions, but they will not see the price-related columns available to higher roles.

For more information, see [Access model and external roles](access-model-and-external-roles.md).

## Relationship to page-specific behavior

The shared grid behavior explains the common interaction model, but each page still has its own business meaning and page-specific actions.

For example:

- **Orders** may include access to order details and order-specific actions;
- **Invoices** may lead to invoice-specific document details;
- **Due Payments** focuses on currently outstanding payments;
- **Payment History** focuses on completed payment records.

This is why the grid should be understood as a reusable interface pattern rather than as a separate business feature.

## Summary

Client Center uses a shared grid behavior across its list-based pages.

This shared behavior provides a consistent way to:

- browse and sort records;
- filter and search data;
- group records;
- show or hide columns;
- save and restore layouts;
- review totals and summary values.

As a result, users can move more easily between Client Center sections while working with a familiar list interaction model.
