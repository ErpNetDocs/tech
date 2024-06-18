# ATTRIBUTECHANGED

|Name| ATTRIBUTECHANGED
|:----|:----
|**Layer**| Front-end
|**Description**| Occurs after the attribute's value is changed. The attribute's name is specified in the 'Event Parameter' field.
|**Version**| Introduced: 2019 <br> Updated: -

The ATTRIBUTECHANGED event is always used with a **Parameter**, which is the name of the Attribute (Field) whose value change triggers the event.

This event occurs immediately **after** the value changes.

A typical use case is when you need to save, set, or calculate something based on the new value of the field.

_**Example**_

**Event:** ATTRIBUTECHANGED(QuantityValue)
<br/>**Action:** ActionType: SETVALUE | Attribute: Notes | Attribute: QuantityValue

The Quantity in the line is **5.00**.
<br/>The user changes the Quantity to **7.00**.
<br/>The change of the Quantity field triggers the rule and sets the New value i.e. **7.00** to the Notes field.
