# Orders

The "Orders" menu provides information on upcoming orders. 

![Orders](pictures/orders.png)

The order navigator is divided in two categories:

-	<b>ASSIGNED TO ME</b> - the employee who is logged into their own account can check the orders they have for execution 
-	<b>UNASSIGNED</b> - orders that are not redirected to a specific employee and should be executed by someone who can take them

The total number of orders can be checked at the bottom of the page.

## Order details

Click an order to see more information about it.

![Order details](pictures/order-details.png)
 
The details on the screen include:

-	<b>Assigned To</b> - the employee who has to execute the order;
-	<b>Document Date</b> - the date of the order
-	<b>Creation Time</b> - the time and date of creation of the order;
-	<b>Lines Count</b> - the rows number in the order table;
-	<b>Total Qty</b> - the sum of quantities, regardless of the unit of measurement.

Click the <b>Open</b> button to open the order.

A summary of the order lines shows up:

![Open order](pictures/open-order.png)

The screen has three tabs:

-	<b>All</b> - shows all lines in the order regardless of whether they have been fulfilled or not
-	<b>Remaining</b> - shows rows that have not yet been fulfilled
-	<b>Executed</b> - shows the rows that have already been fulfilled

The lines contain information about the requested product and its quantity. 

-	<b>Task</b> - shows the main task;
-	<b>Loc</b> - stands for Location of the Product.
-	<b>Prd</b> - stands for Product. 
-	<b>Total Remain</b> - shows how many pieces of the product need to be procured. The amount of the total number is written on the top line - Qty (4), and on the bottom line is written the quantity that remains to be obtained-Remaining (4). In this case, not a single piece of the total number has been received yet, and the necessary 4 pieces are yet to be procured.
-	<b>Еxec</b> - a check mark appears in this column when the row is completed. 

At the bottom of the screen, there are buttons that help complete the order. On the left side is the button to terminate the order (<b>Stop</b>), on the right is the button that indicates that the employee is ready to start the execution of the order (<b>Execute</b>), and in the middle there is a Menu button that allows access to all functions:

![Order actions](pictures/order-actions.png)

## Location

Pressing the <b>Execute</b> button indicates that the order is in progress. The option to scan the location of the product will appear. There is already a suggested location that can be used if needed by clicking the <b>Use</b> button next to it:
 
![Location](pictures/order-location.png)

## Availability

<b>AVAILABILITY</b> is a reference through which the quantity of the product can be checked at different locations. The availability option is usable when the product has a Lot. Click to expand and see the availability for the specific product:

![Availability](pictures/order-availability.png)

Click on the desired location to make the selection.

## Product 

After selecting the location, a field for scanning the Product will appear. You could use the product suggested by the system by clicking the <b>Use</b> button. The interface allows for the product to be replaced if needed. 
Even if the product is not replaced, it still needs to be scanned. 

![Product](pictures/order-product.png)

## Lot

If the product has a Lot, the system will ask you to enter it. There could be a suggestion you can use again. The Lot can be scanned. However, if it does not have a barcode, it can be entered manually as long as it already exists in the system. You can check the AVAILABILITY section as well, if needed:

![Lot](pictures/order-lot.png)

## Quantity

The Quantity field allows the employee to select the unit and quantity of the product:

![Quantity](pictures/order-quantity.png)

You can make the quick suggested action with the <b>Use</b> button or enter it manually. The <b>INFO</b> section underneath summarizes your previous selections.

## Serial

Depending on the product, you might be asked for its serial number, with or without suggested value to use and with AVAILABILITY section again:

![Serial](pictures/order-serial.png)

Once the serial number is selected, there is no need to fill in the Quantity field and it can be skipped.

## Complete

When you are done with the execution of the order, press <b>Complete Order</b>. 
A pop-up window will appear asking for permission to change the status of the order to Completed.

![Location](pictures/order-complete.png)

After clicking Yes, you will be returned to the main Orders page and will be able to pick a new order to complete.

The execution of the order is reflected in the total number of orders left at the bottom of the screen.
