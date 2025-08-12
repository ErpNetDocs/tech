# Orders

The Orders page is home to all sales orders linked to a customer.

It is visible to all Client Center users accessing this customers's data with an **[external role](https://docs.erp.net/tech/modules/crm/sales/customers/external-access.html#roles)** **L20 - Orders** and above.

![pictures](pictures/orders_screen.png)

### Details

You can find the following information about each sales order in the table:

- **Date** - Date of submission (or registration) of the document.
- **Type name** - Type of the document, Sales Order by default.
- **Document No** - The document number.
- **Amount** - The amount of the sales order. 
- **Status** - Current state of the order (e.g. New, Ordered, Cancelled).

> [!Important]
>
> Pricing data like **Amount** is visible ONLY to users with an external role **L30 - Orders with Prices** and above.

> [!NOTE]
>
> Orders that are started but not placed are automatically saved and registered with status **New**.

### Sales order document 

If you click the **blue arrow button** on the leftmost portion of a row, you can open a sales order document.

The document itself includes customer and enterprise company data, as well as individual lines breakdown.

![pictures](pictures/orders_sele.png)

#### Actions

1. It is possible to **download** a sales order as a PDF file.

    ![pictures](pictures/order_details_download.png)
   
2. If present, files attached to an order will be displayed in a dedicated section, along with their name, extension and size.

    **Clicking once** on a file will trigger its download.

    ![pictures](pictures/order_file_downloads.png)

3. You can also **cancel** a submitted order before it is released. This will trigger a notification for confirmation.

    ![pictures](pictures/order_cancel.png)

> [!NOTE]
> 
> The screenshots taken for this article are from v.26 of the platform.
