# System requirements

Although WMS workin is web-based and does not require any installation, there are some  minimum system requirements that should be met.

## Browser 

WMS Worker is supported in the browsers shown in the following table.

|Browser | Version|
| ---- | ----- |
| Google Chrome, including Android |	Current* |
| Microsoft Edge |	Current* |
| Mozilla Firefox |	Current* |

*Current refers to the latest version of the browser.

## OS

The minimmum requirement of the operational system is Android 8.0 (Oreo) or higher.

## Devices

#### Mobile RF handheld devices ####
Requirements:
-	Minimum RAM: 1 GiB, recommended: 2 GiB or higher
-	Minimum Processor: 1 GHz

Recommendations:
<br/>The manufacturers device software should allow to configure following scanner settings on the device:
- Convert barcode input via scan head or camera to text
- Possibility to give an automatic ENTER after a scan
- Identifies GS1-128/EAN128 barcodes (when such is used in the warehouse)

> [!NOTE]
>Please consult with both your implementatorand and device provider before purchasing a device. They will help you determine the specific requirements that would be most appropriate for the specifics of your business.

## Compatible devices
The following Android devices have been tested:
- ???
- ???
- 

> [!NOTE]
>Other models may work as well when meeting the other requirements in this document but cannot be guaranteed.



## Test device compatibility

You have a mobile RF handheld devices and you want to make sure it is compatible with  WMS Worker?
<br/>We've created a test environment where you can test the WMS Worker in action.

**Тo test your device, just follow these steps:**
1. Open the following link in the browser of the mobile terminal https://testdb.my.erp.net/cl/wmsworker
<br/> user: admin
<br/> password: 123
2. Select Orders 
3. Select Warehouse Order 0000000003 
4. Change the Quantity of the first line to 4
5. Scan the Location

![Location](pictures/location.png)

6. Scan the Lot

![Lot](pictures/lot.png)

7. Press Execute
8. Scan the Location for the second line

![Location2](pictures/location2.png)

9. Press Execute

You have successfully executed a warehouse order with your device!

