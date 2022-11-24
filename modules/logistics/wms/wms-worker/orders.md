# Orders

The "Orders" menu provides information on upcoming warehouse orders. 

![Orders](pictures/orders.png)

The order navigator is divided in two categories:

-	<b>ASSIGNED TO ME</b> - the warehouse worker who is logged into their own account can check the orders they have for execution. 
-	<b>UNASSIGNED</b> - orders that are not assigned to a specific worker and should be executed by someone who can take them.

Above the list is a search bar that can be used to filter orders. In it, you can search by scanning or entering an order number, party name (if any) or the document type.

The total number of orders can be checked at the bottom of the page.

## Order details

Click an order to see more information about it.

![Order details](pictures/order-details.png)
 
The details on the screen include:

-	<b>Assigned To</b> - the employee who has to execute the order;
-	<b>Document Date</b> - the date of the order
-	<b>Creation Time</b> - the time and date of creation of the order;
-	<b>Lines Count</b> - the rows number in the order table;
-	<b>Total Qty</b> - the sum of quantities. If there are lines in different measurement units, there will be separate totals for each unit.

Click the <b>Open</b> button to open the order.

## Order lines

A summary of the order lines shows up:

![Open order](pictures/open-order.png)

The screen has three tabs:

-	<b>All</b> - shows all lines in the order regardless of whether they have been executed or not
-	<b>Remaining</b> - shows rows that have not yet been executed
-	<b>Executed</b> - shows the rows that have already been executed

The lines contain information about the requested product and its quantity. 

-	<b>Task</b> - shows the main task;
-	<b>Loc</b> - stands for Location of the Product.
-	<b>Prd</b> - stands for Product. 
-	<b>Total</b> - shows what quantity of the product needs to be procured. 
-	<b>Remain</b> - shows what quantity of the product have already been executed. The remaining quantity that needs to be to be procured is the difference between Total and Remain.
-	<b>Еxec</b> - a check mark that shows if the line is fully executed on not. 

More details about each line e.g. the full name of the product, the ordered lot, variant, serial number, etc. can be accessed via the <b>Info button</b>.
If the line already has an execution, the Info screen contains more details about it as well.

![Info button](pictures/info-button.png)

At the top of the screen there is a general <b>Scan field</b>. When scanning a value in this field, a matching unexecuted line is searched through the lines list. If such a line is found, its execution of the line is started automatically. The scanned value recognition is done by @parcers (e.g. Product Code parcer, GS1-128 Single Product parcer). The list of currently enabled parsers can be seen in the question mark button. 

![Scan field](pictures/scan-field.png)

At the bottom of the screen, there are buttons that help complete the order. On the left side is the button to terminate the order (<b>Stop</b>), on the right is the button that indicates that the employee is ready to start the execution of the order (<b>Execute</b>), and in the middle there is a <b>Menu button</b> that allows access to all functions:

![Order actions](pictures/order-actions.png)

## Line Execution

The line execution starts when we press the <b>Execute</b> button in the lines list or when we Scan a code and a matching line is found.
The execution guides the worker trough the applicable screens. The applicable screens are .... 

### Location

The option to scan the location of the product will appear. There is already a suggested location that can be used if needed by clicking the <b>Use</b> button next to it:
 
![Location](pictures/order-location.png)

### Availability

<b>AVAILABILITY</b> is a reference through which the quantity of the product can be checked at different locations. The availability option is usable when the product has a Lot. Click to expand and see the availability for the specific product:

![Availability](pictures/order-availability.png)

Click on the desired location to make the selection.

### LUN 



### Product 

After selecting the location, a field for scanning the Product will appear. You could use the product suggested by the system by clicking the <b>Use</b> button. The interface allows for the product to be replaced if needed. 
Even if the product is not replaced, it still needs to be scanned. 

![Product](pictures/order-product.png)

### Variant


### Lot

If the product has a Lot, the system will ask you to enter it. There could be a suggestion you can use again. The Lot can be scanned. However, if it does not have a barcode, it can be entered manually as long as it already exists in the system. You can check the AVAILABILITY section as well, if needed:

![Lot](pictures/order-lot.png)

### Serial

Depending on the product, you might be asked for its serial number, with or without suggested value to use and with AVAILABILITY section again:

![Serial](pictures/order-serial.png)

Once the serial number is selected, there is no need to fill in the Quantity field and it can be skipped.

### Quantity

The Quantity field allows the employee to select the unit and quantity of the product:

![Quantity](pictures/order-quantity.png)

You can make the quick suggested action with the <b>Use</b> button or enter it manually. The <b>INFO</b> section underneath summarizes your previous selections.

### Destination

## Complete

When you are done with the execution of the order, press <b>Complete Order</b>. 
A pop-up window will appear asking for permission to change the status of the order to Completed.

![Location](pictures/order-complete.png)

After clicking Yes, you will be returned to the main Orders page and will be able to pick a new order to complete.

The execution of the order is reflected in the total number of orders left at the bottom of the screen.
