---
items: CalculatedAttributeExamples
---

# Check if the system type of payment type in the sales order is 'In Cash'

With this attribute we can check if the system type of payment type which is set in the sales order is 'In Cash'. When we have  that information we can, for example, use the attribute to create a business rule (for more information, see **Allow a credit limit override when the client pays in cash**) that allows a credit limit override when the client pays in cash.

```
10: IIF EXP:20 CONST:True CONST:False      
20: EQUAL EXP:25 EXP:30                                
25: CAST CONST:0 CONST:System.Nullable`1[Aloe.EnterpriseOne.Model.Finance.Payments.PaymentTypesRepository+SystemType]          
30: GETOBJVALUE REF:PaymentType ATTRIB:SystemType
```

Explanation:

- 10: Return True of False according to the result of EXP:20
- 20: Check if EXP:25 is equal to EXP:30  
- 25: Converts '0' to type  System.Nullable`1[Aloe.EnterpriseOne.Model.Finance.Payments.PaymentTypesRepository+SystemType] using **CAST**
- 30: Get the system type of the payment type which is set in the sales order.

> [!NOTE]
> When using **[EQUAL](https://docs.erp.net/tech/advanced/calculated-attributes/operators/equal.html)** we should make sure that we are comparing parameters from the same type. 
> If we don’t know which is the type of the particular object or what is the value that it is going to return, we can use the **Aloe.EnterpriseOne.Model Documentation**. 
> In the particular example, we can check [PaymentTypesRepository.SystemType Enumeration](https://restdev.erp.bg/model/html/2fd52ed9-8c3d-8b99-c824-6574557864c0.htm), where we can see that the value that corresponds to the system type in 'Cash' is '0'.
