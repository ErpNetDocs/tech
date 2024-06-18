# ATTRIBUTECHANGING

|Name| ATTRIBUTECHANGING
|:----|:----
|**Layer**| Front-end
|**Description**| Occurs before the attribute's value is changed. The attribute's name is specified in the 'Event Parameter' field.
|**Version**| Introduced: 2019 <br> Updated: -

The ATTRIBUTECHANGING event is always used with a **Parameter**, which is the name of the Attribute (Field) whose value change triggers the event.

This event occurs immediately before the value changes.

A typical use case is when you need to save, set or calculate something based on the previous (old) value of the field.

_**Example**_

**Event:** ATTRIBUTECHANING(QuantityValue)
<br/>**Action:** ActionType: SETVALUE | Attribute: Notes | Attribute: QuantityValue

The Quantity in the line is **5.00**.
<br/>The user changes the Quantity to **7.00**.
<br/>The change of the Quantity field triggers the rule and sets the Old value i.e. **5.00** to the Notes field.
