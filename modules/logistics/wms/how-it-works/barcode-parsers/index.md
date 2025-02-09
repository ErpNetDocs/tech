---
uid: parcers
---

# Barcode Parsers
Barcode parsers are used to read and interpret different barcodes by the Scan field in the Order Lines menu in the [WMS Worker](xref:wms-worker) app. 

Their algorithm analyzes the barcodes and extracts the encoded data in them. The extracted data is then used by the [WMS Worker](xref:wms-worker) app to easily find a suitable Warehouse Order Line and start its execution.
How the barcode is recognized, how a suitable line is found, and how its execution is started depends on the action of the particular parser. 

> **_NOTE:_**  The list of the active parsers can be found in the Question mark button in the Scan field of the Order Lines screen in the WMS Worker app. Their order in this list also shows their application order during the barcode reading. Currently, all available parsers are enabled by default. They cannot be disabled and their application order cannot be changed. 

Here is a list of the available parsers:
* [P01: Product Code](p01.md)
* [P02: GS1 - Single Product](p02.md)
* [P03: GS1 - SSCC](p03.md)
* [P04:LUN Serial Code](../wms-worker/orders/scanning.md)
* [P05:Warehouse Location](../wms-worker/orders/scanning.md)
* [P06:Quantity](../wms-worker/orders/scanning.md)
