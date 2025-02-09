# SCAN field

Scanning Products
Single Scan
To scan a product once, simply enter its code into the SCAN field and tap the blue arrow button. This will take you to the Quantity screen, where you need to specify Location, Lot, and Quantity.

Multiple Scans
To scan a product multiple times, input the desired quantity into the SCAN field and tap the blue arrow button. You can optionally include the multiplication operator (“*”).

The quantity entered will be displayed in a separate field under the main SCAN field. For example, if you enter “200*”, it will indicate that you are scanning the product 200 times.

Adding Locations to the SCAN Field
As part of the latest development, the SCAN field can now also recognize locations. The following improvements have been made:

Valid Location Recognition
When scanning a valid location from the Logistics.Wms.WarehouseLocations entity (ERP.net Domain Model), the location will appear as a line under the SCAN field, similar to how quantities are displayed. The location line will appear below the quantity line.

Location Labeling
The line for location will display "Location:" (or "Складово място:" in Bulgarian) followed by the scanned location. A small X icon will be shown on the right side to remove the current location.

Quantity Labeling
When a quantity is entered, the quantity line will now show "Quantity:" (or "Количество:") before the number, with the quantity followed by an asterisk (e.g., "200*").

Storing Current Location
Once a location is scanned, it will be stored in the WMS Worker’s memory until you scan another location or remove it by clicking the X.

Location Skip
If a location is scanned and then a product from the list is scanned, the location screen will be skipped. Additionally, the product screen will be skipped, and you will be taken directly to the quantity screen (unless there are lots, serial numbers, or variants to enter).

Returning to the Line List
After completing a line, the worker will return to the line list, and the current location will remain. If another product is scanned, the action from point 5 will repeat.

Executing with Current Location
If there is a current location and you execute a line instead of scanning a product, the location screen will be skipped, and the stored location will be automatically applied to that line.

Scan Priorities
Scanning priorities are now defined as follows (from highest to lowest): Quantity, Location, Product. This means that if the same code is used for both a location and a product, the scan will be treated as a location. Quantity codes are unlikely to overlap since values over 1000 need to be followed by an asterisk.

If the scanned code is not recognized as a quantity, location, or product, an error message will be shown:

EN: "No location or product was found with the scanned code."
BG: "Не е открито складово място или продукт със сканирания код."
Scanning Logistic Units (LUN)
In addition to locations, the SCAN field now supports scanning Logistic Units (LUNs) that are not in SSCC format. This includes the following improvements:

New LUN Parser
A new parser has been added to recognize logistic units that are not in SSCC format.

Code: P04
Description: LUN Serial Code
Default Activation in Warehouse Orders
The new parser is enabled by default in the SCAN field for Warehouse Orders and can be listed in the Active Parsers button.

If the recognized LUN has no content, the new parser will be activated (P04).
The existing parser (P03) has been modified to activate only when the logistic unit has content.
Recognizing Serial Codes
For defined logistic units, values from the LogisticUnit.SerialCode field are now recognized.

Displaying LUN
When a valid logistic unit is scanned, it will be displayed as a line under the SCAN field, following the same structure as quantities and locations. The LUN line will appear below both the quantity and location lines.

LUN Labeling
The LUN line will display "LUN:" (or "ЛЕ:" in Bulgarian) followed by the scanned logistic unit. A small X will be available to remove the current LUN.

Storing Current LUN
Once a LUN is scanned, it will remain stored in WMS Worker’s memory until another LUN is scanned or the current LUN is removed by clicking the X.

LUN Screen Skip
If a LUN is scanned followed by a product from the list, the LUN screen will be skipped. If there is also a current location, both the location and product screens will be skipped, and the user will go directly to the quantity screen.

Returning to Line List
After completing a line, the worker will return to the line list, and the current LUN will remain. If another product is scanned, the action from point 7 will repeat.

Executing with Current LUN
If a current LUN is stored and a line is executed without scanning a product, the LUN screen will be skipped, and the stored LUN will be automatically applied to that line.

Updated Scan Priorities
The updated scanning priorities are as follows (from highest to lowest): Quantity, Location, LUN, Product. If the same code is used for both a location and a LUN (which is rare), the scan will be treated as a location.

If the scanned code is not recognized as a quantity, location, LUN, or product, an error message will be displayed:

EN: "No location, LUN, or product was found with the scanned code."
BG: "Не е открито складово място, ЛЕ или продукт със сканирания код."
Text Formatting
The text for current values of Quantity, Location, and LUN will now be displayed in smaller font and in bold. For example:

"Location: PA-02-06"
