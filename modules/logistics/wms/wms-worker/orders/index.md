---
uid: orders-menu
---

# Orders

This screen gives access to all upcoming warehouse orders that are available for execution.

They are distributed into **five sections** and sorted in an **ascending** order in each.

![Orders](pictures/main_menu.png)

### Search and totals

Above the sections, there is a **search bar** that can be used to filter the existing orders. 

You can search by scanning or entering an order number, a party name (if any), or a document type.

For reference, the **Total** number of orders can be checked at the bottom-left corner of the page.

![Orders](pictures/search_totals_wms.png)

### Context menu

The **Orders** screen features a Context menu, accessible through the three-dot button at the bottom.

It allows you to execute the following actions:

* **Refresh** - When triggered, it will instantly refresh the contents of the page, taking into account orders previously not added and dismissing the ones that have been voided.

  ![Orders](pictures/refresh_orders.png)

### Order details

Once an order is opened, you can see the following details about it:

![Order details](pictures/details.png)

- **Enterprise Company** - name of the associated enterprise company, positioned at the top; if not present, it will be replaced by a dash
-	**Assigned To** - the employee who has to execute the order
-	**Document Date** - the date of the order
-	**Creation Time** - the time and date of creation of the order
-	**Status** - the status of the order
-	**Lines Count** - the rows number in the order table
-	**Total Qty** - the sum of product quantities; if there are lines in different measurement units, there will be separate totals for each unit
-	**Total Base Qty** - the overall quantity of individual products, grouped according to the respective measurement unit (e.g. 8 sets total qty equals 96 pcs base qty).

---

### Section breakdown

The **Orders** screen consists of the following sections:

**Started by me**

These are all the *Released* warehouse orders which are started by and assigned to the **currently** logged-in user.

**Assigned to me**

Contains orders in states higher than *New* and lower than *Released*. They are assigned to the **currently** logged-in user.

**Unassigned**

Orders with states higher than *New* and lower than *Released*. 

They are **not** assigned to a specific worker and can be executed by anyone who takes them.

**Started by others**

Here, you will find all *Released* orders which are assigned to users **different** from the currently logged-in one.

**Assigned to others**

This section contains orders in states higher than *New* and lower than *Released*.

They are assigned to users **different** from the currently logged-in one.

---

### Action buttons

When accessing an order, different **buttons** will be visualized based on the section you access the order from.

They indicate the **action** you're able to perform. Clicking some of them will result in the order being moved to a different section.

**Started by me**

Accessing an order from here reveals general information about it, as well as a dedicated **Continue** button.

Upon clicking it, you'll **open** the order and will be able to continue with its processing.

![Orders](pictures/started_by_me.png)

**Assigned to me**

Accessing an order from here reveals general information about it, as well as a dedicated **Start** button.

Upon clicking it, the order will be **released** and **opened**.

![Orders](pictures/assigned_to_me.png)

**Unassigned**

Accessing an order from here reveals general information about it, as well as a dedicated **Take & Start** button.

Upon clicking it, the order will be **assigned** to you, **released** and **opened**.

![Orders](pictures/unassigned.png)

**Started by others**

Accessing an order from here reveals general information about it, as well as a dedicated **Join** button.

Upon clicking it, you'll **open** the order.

![Orders](pictures/started_by_others.png)

**Assigned to others**

Accessing an order from here reveals general information about it, as well as a dedicated **Take & Start** button.

Upon clicking it, the order will be **re-assigned** to you, **released** and **opened**.

![Orders](pictures/assigned_to_others.png)

## Order lines

Once an order is taken, started, continued or joined, a summary of its lines will show up:

![Open order](pictures/lines_data_wms.png)

On this screen, you will find three tabs dedicated to line execution:

-	**All** - shows all lines of the order regardless of whether they have been executed or not
-	**Remaining** - shows rows that have not yet been executed
-	**Executed** - shows the rows that have already been executed

All lines contain information about the requested product and its quantity.

-	**Task** - shows the main task
-	**Loc** - shows the location of the product
-	**Prd** - shows the product itself
-	**Total/Exec** - shows what quantity of the product needs to be procure compared to what quantity has already been executed
- **Еxec** - a check mark that appears only if the line is fully executed

More details about each line, e.g. the full name of the product, the ordered lot, variant, serial number, etc. can be accessed via the line's respective **info button**. If an execution has already taken place, the **Info** screen will include details about it as well.

![Info button](pictures/info_wms.png)

At the top of the screen, there is a general **Scan field**. 

When scanning a value in this field, a matching unexecuted line is searched through the lines list. If such a line is found, its **[execution](https://docs.erp.net/tech/modules/logistics/wms/wms-worker/orders/lines-execution.html)** is started automatically. 

![Scan field](pictures/scan_wms.png)

> [!NOTE]
> The scanned value recognition is done by **[Barcode Parsers](https://docs.erp.net/tech/modules/logistics/wms/how-it-works/barcode-parsers/index.html)** such as Product Code and GS1 - Single Product. <br>
> The list of currently active parsers can be seen by accessing the vertical three-dot **Menu button** at the bottom of the app.

At the bottom of the screen, there are buttons for managing the order:

- **Stop** - terminates the order 
- **Execute** - allows for **[line execution](https://docs.erp.net/tech/modules/logistics/wms/wms-worker/orders/lines-execution.html)**; will change to **Complete Order** when all lines have been executed
- **Menu** - allows access to several additional functions like **[Suggest Routing](https://docs.erp.net/tech/modules/logistics/wms/wms-worker/orders/picking-routes.html?q=suggest%20routing)**, **Active Parsers**, and **Refresh**, which will instantly refresh the contents of the order.

  ![Order actions](pictures/menu_wms.png)
