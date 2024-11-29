---
items: UserBusinessRuleExamples
---

## Set value into Amount and Quantity fields

Values cannot be set directly in the main **Amount** and **Quantity** fields, as these fields require a specific format that includes both a 'Value' and a 'Unit of Measure.

However, the attribute list contains a special version of the field, ending with **"Value"**, which holds only the numerical value. This version allows you to set values with business rules.


### Example

If you want to fill in the **"VATAmountBase"** in VAT Entries entity, you must create a Business Rule that sets the value in the **"VATAmountBaseValue"** instead.


### More Information

For further details about Amount and Quantity data types, refer to the model documentation:

- [Amount Data Type](https://docs.erp.net/model/data-types.html#amount)
- [Quantity Data Type](https://docs.erp.net/model/data-types.html#quantity)



