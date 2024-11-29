# Set the VAT rate depending on Deal type

In Sales orders, the VAT rate can be set dynamically based on the selected DealType in the header using the following rule.

You can get that information using **[this](https://docs.erp.net/tech/advanced/calculated-attributes/examples/check-if-system-type-is-in-cash.html)** calculated attribute, which returns 'True' or 'False'.

Тo achieve this, a calculated attribute #VATBYDEALTYPE is used, which returns the VAT percentage based on the selected Deal type.
The **BEFORERECALCULATE** event is utilized, which occurs just before the calculation of additional amounts.
There are two conditions: one based on the code of the Document Type, for which the calculated attribute #DocType is used, and the other based on the ID of the additional amount type for VAT.

|Repository|
|:----|
|General.Documents.DocumentAmounts|

|Events|
|:-----|

|Event type|Event parameter|Execution priority|
|:----|:----|:----|
|BEFORERECALCULATE|                 |Normal|

|Conditions|
|:-----|

|Condition No|Attribute name|Comparison type|Value|
|:-----|:-----|:----|:-----|
|1|#DocType|=|DirectSales|
|2|DocumentAmountTypeId|=|3340ebbc-9253-4aa9-8e7c-5cf2d18bfe95|

|Actions|
|:-----|

|Action No|Action type|Parameter1 type|Parameter1 value|Parameter2 type|Parameter1 value|
|:----|:----|:----|:----|:----|:-----|
|1|SETVALUE|Attribute|InputPercent|Attribute|#VATBYDEALTYPE|

> [!NOTE] 
>
> '#DocType' is a **[calculated attribute](https://docs.erp.net/tech/advanced/calculated-attributes/index.html)**. 
>
> '#VATBYDEALTYPE'  is a **[calculated attribute](https://docs.erp.net/tech/advanced/calculated-attributes/index.html)**.
