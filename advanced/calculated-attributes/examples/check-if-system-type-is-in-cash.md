---
items: CalculatedAttributeExamples
---

# Check if the system type of a payment type in a sales order is 'In cash'

This attribute checks if the system type of a payment type set in the sales order is 'In Cash'. 

You can use the attribute to create a business rule that allows a **credit limit override** when the client pays in cash.

For more information, see **Allow a credit limit override when the client pays in cash**.

```
10: IIF EXP:20 CONST:True CONST:False
20: EQUAL EXP:25 EXP:30
25: CAST CONST:0 CONST:System.Nullable`1[Aloe.EnterpriseOne.Model.Finance.Payments.PaymentTypesRepository+SystemType]
30: GETOBJVALUE REF:PaymentType ATTRIB:SystemType
```

**Explanation:**

- 10: Return 'True' of 'False' according to the result of EXP:20
- 20: Check if EXP:25 is equal to EXP:30  
- 25: Converts '0' to type **System.Nullable`1[Aloe.EnterpriseOne.Model.Finance.Payments.PaymentTypesRepository+SystemType]** using **CAST**
- 30: Get the system type of the payment type which is set in the sales order.

> [!NOTE]
> 
> When using **[EQUAL](https://docs.erp.net/tech/advanced/calculated-attributes/operators/equal.html)**, make sure you're comparing parameters from the same type. 
> If you don’t know which type the object is or what value it's going to return, you can use the **Aloe.EnterpriseOne.Model Documentation**. <br>
> In the particular example, you can check the **[PaymentTypesRepository.SystemType Enumeration](https://restdev.erp.bg/model/html/2fd52ed9-8c3d-8b99-c824-6574557864c0.html)**, where you'll find that the value corresponding to the system type in 'Cash' is '0'.
