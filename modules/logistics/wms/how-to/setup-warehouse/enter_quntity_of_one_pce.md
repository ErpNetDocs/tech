---
uid: enter_quntity_of_one_pce
---

# Enter quantity of one pce

You can configure the behavior when scanning a barcode in the WMS-Worker app. 

The settings determine whether scanning a barcode automatically enters a quantity of one piece or simply locates the product row and allows for manual quantity entry.

To adjust this setting, use the following [config options reference](https://docs.erp.net/tech/reference/config-options-reference.html) :

`/WMS/WMS-Worker/SingleBarcodeScanEntersQuantityOfOnePce`.

- When the value of this configuration is set to "1", scanning a barcode directly enters a quantity of one piece.
- When the value is set to "0", the WMS-Worker app locates the product row and switches to execute mode for that line, allowing for manual quantity entry.

![pictures](pictures/Logistic_enter_quntity_of_one_pce_27_05.png)
