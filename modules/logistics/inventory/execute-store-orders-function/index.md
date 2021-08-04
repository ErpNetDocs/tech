# Execute Store orders function

This function allows easier work with the barcode scanner and more functional methods for the execution of one Store order row by more than one Transaction row. This is useful in case the user operates with lots or serial numbers, etc.

The function contains two main components:

- Store orders panel;
- Input data panel

## Store orders Panel

It loads the unfulfilled Store order rows according to the filters in the navigator. The data includes the ordered quantity of the row, the executed part of that quantity and the remaining quantity (the unfulfilled part). This data is read-only except for the *Input Quantity* which is used for easier data entering.

## Input data Panel

This panel is editable by the users. They enter information about what store transactions are executed in the current moment and do not mark the specific Store orders that they are executing. This is defined automatically by the system. 

The data that is entered is ***Product, Lot, Serial Number, Quantity, Measurement Unit*** and ***Base Quantity***. There are several methods to enter such information:

- Manually. This is the rarest method used. To be more precise, it is for editing information entered by any other method.
- Using the *Input Quantity* field in the Store orders panel. When the user enters data in it, it automatically creates new row in the Input data panel with the entered quantity and the product, lot, serial number and measurement unit copied from the Store order row ,  Also, the new row in the Input data panel is marked as reserved for the row in the Store order rows panel. This method's purpose is to support the old method from the old execution navigator, where the user always enters the exact Store order row that he is executing.
- Using barcode scanner (or other system for control/counting/marking the stocks). This is considered as the standard way to enter data, where the user do not specify the Store order row and only marks the store transaction.

## Distributing the Executions

The data entered in the Input data panel has to be distributed through the rows from the Store orders panel. This is performed after each change in the Input data panel. The distribution is executed by **Store order rows Execution algorithm** and all calculations about the quantity are based on *Base Quantity*. The Store order rows form the list [ORD] and the data in the Input data panel forms the list **[EXC]**.

There is a small difference from the **algorithm** - rows from the Input data panel *reserved* to specific Store order row, always execute this specified row. The algorithm is not allowed to distribute them to other rows. The purpose of this is to avoid a situation when  the user enters quantity in *Input Quantity* field and it is distributed to another Store order row (just because the algorithm considers it as with higher priority than the one that the user has chosen). So this gives the user the ability to mark specific rows for execution.

 The distributed quantities are illustrated as sub-rows of the Store order rows. They contain data (quantity, lot, serial number and more) from the Input data panel which may be different than the data in the Store order row. 

## Creating Transaction

At the end, when the user creates Transaction, its rows are based on the distributed executions. For example,  if a Store order row has 4 distributed sub-rows of execution, then the Transaction has 4 rows with the information from the Input data panel and all those rows are executing the specific Store order row.

When the Transaction is created, the data in the Input data panel is deleted and the navigator is ready to be used again.
