# Documents

The Documents screen is designed to centralize and display all documents in @@name that are relevant to a user's account. This includes documents you have created as well as those assigned to you.

By offering instant access and various ways of customizing how documents are displayed, Documents is both flexible and time-saving, eliminating the need to search across different modules.

![pictures](pictures/documents_overview.png)

### Document assignment

For a document to appear in the **Documents** environment, its **Assigned To User** field must be filled with the appropriate **username**.

* New documents are automatically assigned to **the person creating them** (i.e., the current user) by default.
* If you assign the document to someone else in your organization, it will appear in their Documents environment.

![pictures](pictures/document_assignment.png)

> [!NOTE]
>
> If the **Assigned To User** field is not visible in the document form, you need to reveal it manually with the **Customize panel** menu.

![pictures](pictures/doc_assignment_customize.png)

## Interface

The screen is composed of a table containing all document records which are related to the currently logged-in user.

It allows simple operations like searching, filtering, and sorting, as well as more advanced options.

### Top bar actions

You can perform basic actions in the top bar above the table:

1. **Reload:** Refreshes the table to display the most up-to-date information.
2. **Search:** A dedicated search bar to quickly find documents by providing details like their number, date, or document type.

![pictures](pictures/documents_searchbar.png)

### Multi-select and export

You can select one or more documents and perform batch operations on them.

Toggling the **Multi select** option from the panel Menu allows you to select multiple documents using checkboxes.

The Export feature will become available as soon as one document is selected. This action exports the documents into an Excel file for external analysis or reporting.

![pictures](pictures/documents_export.png)

### Sharing 

One or multiple documents can be shared with others using the **Share** button in the ribbon.

You can copy a **direct link** to the selected document, or share the it to a **[group](https://docs.erp.net/tech/modules/my/groups/index.html)** within your organization's collaborative environment.

![pictures](pictures/documents_share.png)

The second option requires you to select a group and optionally add a comment.

![pictures](pictures/documents_group_share.png)

## Customization and navigation

My Documents provides extensive customization features to organize and display documents in a variety of ways.

### Panel menu options

The **vertical three-dot button** at the upper-right corner of the Documents table contains a list of actions and layout controls.

| Menu Option | Functionality |
| :--- | :--- |
| **Show filter row** | Toggles the dedicated row beneath column headers for direct, column-specific filtering of the table. |
| **Show grouping panel** | Reveals a section above the table used for dragging column headers to apply document grouping. |
| **Maximum row count** | Adjusts the maximum number of document rows that the page loads and displays in the table. |
| **Customize panel** | Opens a configuration window to adjust column visibility and order within the main document grid. |

![pictures](pictures/documents_panelmenu.png)

### Grouping panel

The **Show grouping panel** feature allows you to arrange documents in a hierarchical order based on values in one or more column headers.

When you enable it, an additional space with instructions will appear above the main table.

![pictures](pictures/documents_grouping_panel.png)

To group, you need to **drag and drop** a column header into that area.

The table will automatically be re-organized to show documents grouped based on the column you selected.

![pictures](pictures/documents_grouped.png)

You can create **multi-level grouping** by dragging multiple column headers. 

The first column dragged creates the primary level of groups, and subsequent columns create subgroups (e.g., first grouping by Document Date, then by Document Type).

![pictures](pictures/documents_doublegrouped.png)

### Summary

The Summary feature provides useful statistical information for each Document table column.

Simply right-click on a column header and select **Summary**.

![pictures](pictures/documents_summary.png)

The options most relevant for the Documents table are:

* **Count**: Calculates the total number of documents where a value is present in that column.
* **Distinct**: Counts the number of unique values in the field (e.g., the number of unique states, ignoring repetitions).

Fields with a number data type also offer functions like **Max** and **Min** values.

![pictures](pictures/documents_count_distinct.png)

### Panel customization

You can manage the Documents table's appearance via the **Customize panel** option accessible from the panel Menu.

This will open a window consisting of two tabs:

**Items**: Allows you to hide or reveal columns by toggling the slider next to the column name. 

![pictures](pictures/documents_enable_disable_items.png)

You can further restructure the table using the **Position** settings for each column.

![pictures](pictures/documents_fullrow_feature.png)

By default, columns are set to Column mode, but you can make some of them take up an entire row.

![pictures](pictures/documents_fullrow_view.png)

**Reorder**: Allows you to change the sequence of column headers by dragging and dropping them up or down the list.

![pictures](pictures/documents_reorder.png)

### Main menu

The Menu button in the ribbon above the Documents table provides access to more page-oriented and document-specific features.

![pictures](pictures/documents_mainmenu.png)

#### Details

Reveals a preview of a selected document, including shortcuts to pre-populated fields such as Customer, Enterprise Company and Sales Person.

You can also upload attachments and access the full document directly.

![pictures](pictures/documents_details.png)

#### Document flow

Displays the entire chain (sequence) for a selected document, allowing you to access documents that came before and after it.

![pictures](pictures/documents_flow.png)

#### Tiles

You can save a specific configuration of the My Documents page (including filters and grouping) as a **[tile](https://docs.erp.net/tech/modules/my/tiles/index.html)** for direct access.

![pictures](pictures/documents_tile.png)

#### Customize form

Opens the main customization window, allowing you to hide or reveal entire panels and widgets on the screen. 

![pictures](pictures/documents_customize_page.png)

> [!NOTE]
> The screenshots taken for this article are from v.26 of the platform.
