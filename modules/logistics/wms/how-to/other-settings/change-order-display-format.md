# Change order display format

In the **WMS Worker**, you have the ability to modify the information displayed for the **Orders**. 

This can be achieved using a **Configuration Key** that presents information through **String Interpolation**.

![picture](pictures/Order_information_09_02.png)

## Configuration Key

To change the information that is shown in **WMS Worker – Orders**, you need to use the **Configuration Key in Setup – Core – Config**.

![picture](pictures/Config_view_09_02.png)

When you do that, a table with all available configurations will open. 

![picture](pictures/Core_view_09_02.png)

Find the **Configuration** named **/WMS/WMS-Worker/OrderDisplayFormat** and open it. 

![picture](pictures/Core_config_11_02.png)

Once you’ve done that you can change the **Key Value** in the **Configuration** using [String Interpolation](https://docs.erp.net/tech/advanced/string-interpolation/index.html?q=string). 
The **String Interpolation** is taking values from the current **Warehouse Order – WarehouseOrder(id)**. 

![picture](pictures/Core_key_value_11_02.png)

Based on the **Key Value**, different information will be shown  about the orders.

## Behavior in particular cases 

Here is the expected behavior in some different cases:

•	If there is no **Configuration Key** set, the information displayed is retrieved from the **To Party** field. This is the default behavior.

•	If there is a **Configuration Key** set, but the **Key value** field is blank, the information displayed is also retrieved from **To Party** field.

•	There is a **Configuration Key** set, but the assigned parameters are not returning any value. The information displayed is going to be “-“.
