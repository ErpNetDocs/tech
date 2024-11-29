---
items: UserBusinessRuleExamples
---

# Start a business rule only on first releasing

Sometimes, a business case may require a certain **[business rule](https://docs.erp.net/tech/advanced/user-business-rules/index.html)** to be executed only on first releasing of a document. When **[calculated attributes](https://docs.erp.net/tech/advanced/calculated-attributes/index.html)** are triggered, they perform their calculation in real-time. If you use them as conditions for business rules, they may be fulfilled today, but not after a certain period of time.

A business rule can be used to allow a sales order to be released only if the lots used in its lines haven't expired. The condition is fulfilled at the moment of first releasing, and the goods are delivered to the customer. 

What if the released state of the sales order is **re-selected** after a month because of an adjustment of the document notes? The rule will be executed again, though the adjustment may be impossible because some of the lots could have expired by this time. 

You can set a business rule that's triggered only when you're releasing a document for the **first** time. This works despite business rules currently not supporting a first releasing event parameter. You can create a calculated attribute like 'IsFirstReleasing' that check whether the releasing is first and returns 'True' or 'False'. 

For more information, see **[Check whether the releasing of the document is first or not?](https://docs.erp.net/tech/advanced/calculated-attributes/examples/check-for-first-releasing.html)**. 

You can use this attribute as a business rule condition `#IsFirstReleasing = True` - the rule is triggered only when the document is released for the first time, **not** when the released state is re-selected.
