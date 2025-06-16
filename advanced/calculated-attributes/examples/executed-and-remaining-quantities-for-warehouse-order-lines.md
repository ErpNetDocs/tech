---
items: CalculatedAttributeExamples
---

# Executed and Remaining Quantities for Warehouse Order Lines

This example demonstrates how to define and combine two calculated attributes used in warehouse order lines:

1. #ExecutedQuantity – calculates the total fulfilled quantity for a line using document fulfillments. This attribute can also be reused independently in other calculations and reports.
2. RemainingQuantity – calculates the remaining quantity by subtracting the executed quantity from the ordered (standard) quantity.

## Step 1: Fulfilled Quantity per Line (#ExecutedQuantity)

This attribute calculates the total fulfilled quantity for a specific line by summing StandardQuantity from all related DocumentFulfillments.

### Expression

```
10: SUM EXP:20 ATTRIB:StandardQuantity  
20: SELECT REPO:General.Documents.DocumentFulfillments EXP:30  
30: WHERE EXP:40  
40: EQUAL ATTRIB:DocumentLineId EXP:50  
50: GETOBJVALUE INPUT:10 ATTRIB:Id
```

### Explanation

- 10: Sums the StandardQuantity from all document fulfillments selected in EXP:20.
- 20: Selects fulfillments linked to the current line.
- 30: Filters fulfillments using the condition in EXP:40.
- 40: Checks if DocumentLineId from the fulfillment matches the current line's Id.
- 50: Retrieves the Id of the current line from input 10.

This attribute can be used independently to track execution progress per line and is reused in the RemainingQuantity calculation below.

## Step 2: Remaining Quantity (RemainingQuantity)

This attribute calculates the remaining quantity by subtracting the fulfilled quantity from the ordered quantity.

### Expression
```
10: ADD EXP:20 EXP:30  
20: SUM EXP:40 ATTRIB:StandardQuantityValue  
30: SUM EXP:40 EXP:37  
35: CAST ATTRIB:#ExecutedQuantity CONST:System.Decimal  
36: MULTIPLY EXP:35 CONST:-1.00  
37: CAST EXP:36 CONST:System.Decimal  
40: SELECT REPO:Logistics.Wms.WarehouseOrderLines EXP:50  
50: WHERE EXP:60  
60: EQUAL ATTRIB:Id EXP:70  
70: GETOBJVALUE INPUT:10 ATTRIB:Id
```

### Explanation

- 10: Adds the ordered quantity (EXP:20) and the negative of the fulfilled quantity (EXP:30) to calculate remaining.
- 20: Sums StandardQuantityValue for all relevant warehouse order lines.
- 30: Sums negative #ExecutedQuantity values (EXP:37).
- 35: Retrieves the calculated value from attribute #ExecutedQuantity and casts it to Decimal.
- 36: Multiplies the executed quantity by -1.00 to make it negative.
- 37: Casts the result of the multiplication to Decimal, ensuring numeric consistency.
- 40: Selects warehouse order lines to evaluate.
- 50: Applies filtering logic.
- 60: Compares current line’s Id with the referenced one.
- 70: Fetches the current line’s Id from input 10.

## Summary

- #ExecutedQuantity gives you how much has been fulfilled per line and is useful on its own for reporting, monitoring and further calculations.
- RemainingQuantity gives you how much is still pending based on the initial ordered quantity.

This structure ensures clean reuse, type safety, and clear traceability of fulfillment logic in warehouse workflows.
```
