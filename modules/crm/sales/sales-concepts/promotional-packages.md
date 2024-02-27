---
uid: promotional-package
---

# Promotional packages

Promotional packages are packages of products which can be added into sales orders. 
 
The products from the package appear as **sales order lines** and their quantity is a multiple of the number of the sold packages. 
 
If a line is added from a promotional package, then the **name** of the promotional package is filled in the **Promotional package** field.

A promotional package can be applied for a sales order only if it fulfills the **conditions** of the package:

|Promotional package fields |Description
|:-------|:-------|
|Valid from date |Starting date from which the promotional package is valid.
|Valid to date |End date (inclusive) to which the promotional package is valid.
|Valid for price list |Price list for which the promotional package is valid.
|Valid for customer |Customer for which the promotional package is valid.
|Valid for target group |Target group for which the promotional package is valid.
|Valid For Customer Filter XML |Sets a custom filter for clients. The promotional package only applies if the customer fulfills this condition.
|Valid for Ship to customer |Ship to customer for which the promotional package is valid.
|Valid for Ship to customer Filter XML |The promotional package only applies if the customer, which is supplied, fulfills this condition.
| Valid for Distribution channel |Distribution channel, for which the promotional package is valid. 
|Valid for Distribution channel Filter XML |The promotional package only applies if the distribution channel in the sales order fulfills this condition.

**Promotional package lines**

Promotional packages lines represent the products that are part of  the particular package. Quantity and Standard discount percent adjust are required for each line.

|Promotional package line fields|Description
|:---------|:----------|
|Line Number|Line number
|Product Id|Product code
|Quantity|Product quantity
|Unit Price|When filled sets the unit price of the product.
|Unit Price|CurrencySpecifies the currency of the unit price
|Standard discount Percent Adjust |Specifies the amount of change (in percentage points) of the standard discount.
|Standard discount Adjust Or Replace    |Specifies the type of change of the standard discount.</br> Possible values:</br>• Add – adds the percent set into the field ‘Standard Discount Percent Adjust’ to the already existing trade discount in the sales order lines:</br>Standard Discount = Standard Discount + adjust, where ‘adjust’ is the value in the field ‘Standard Discount Percent Adjust’.</br>• Replace – Saves the percent of the field ‘Standard Discount Percent Adjust’ in the standard discount for the line: Standard Discount = adjust</br>• Mark Down – Applies after the standard discount and is calculated as follows:</br>Standard Discount = 1 - (1 – Standard Discount) * (1 - adjust) </br>
