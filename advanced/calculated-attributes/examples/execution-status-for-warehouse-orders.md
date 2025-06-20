---
items: CalculatedAttributeExamples
---

# ExecutionStatus for Warehouse Orders

This example defines a calculated attribute that returns a descriptive status value for a warehouse order. The logic uses three supporting attributes:

1. #LineIsFulfilled – returns True if a line is considered fulfilled based on quantity logic.
2. #Status_NotStarted – returns True if the warehouse order has no fulfillments.
3. #Status_Fulfilled – returns True if there are no unfulfilled lines.

The final attribute, ExecutionStatus, evaluates those and returns one of the following values:

- NotStarted  
- Completed  
- ClosedWithIssues  
- InProgress

> [!NOTE]  
> The repository of the attributes is *Logistics.Wms.WarehouseOrders* for ExecutionStatus and its status flags, and *Logistics.Wms.WarehouseOrderLines* for #LineIsFulfilled.

## Attribute: #LineIsFulfilled

### Expression
```
10: IIF EXP:20 CONST:true CONST:false  
20: LTE ATTRIB:StandardQuantityValue EXP:100  
100: SUM EXP:110 ATTRIB:StandardQuantity  
110: FILTER EXP:120 EXP:130  
120: GETOBJVALUE REF:WarehouseOrder CHILD:Fulfillments  
130: AND EXP:140 EXP:160  
140: EQUAL ATTRIB:DocumentLineId EXP:150  
150: GETOBJVALUE INPUT:10 ATTRIB:Id  
160: EQUAL EXP:170 CONST:1  
170: CAST ATTRIB:FulfillmentType CONST:System.Int32
```
### Explanation

- 100–170: Sums the StandardQuantity from all document fulfillments for the current line, where FulfillmentType = 1 and DocumentLineId matches the current line’s Id.
- 20: Compares if the fulfilled quantity is greater than or equal to StandardQuantityValue.
- 10: Returns true if the condition is met, otherwise false.

## Attribute: #Status_NotStarted

### Expression
```
10: IIF EXP:20 CONST:True CONST:False  
20: EQUAL EXP:30 CONST:0  
30: COUNT CHILD:Fulfillments
```
### Explanation

- 30: Counts how many fulfillments the order has.
- 20: Checks whether the count is 0.
- 10: Returns true if there are no fulfillments, false otherwise.

## Attribute: #Status_Fulfilled

### Expression
```
10: IIF EXP:20 CONST:false CONST:true  
20: GTE EXP:30 CONST:1  
30: COUNT EXP:40  
40: FILTER CHILD:Lines EXP:50  
50: EQUAL ATTRIB:#LineIsFulfilled CONST:false
```
### Explanation

- 50: Filters lines where #LineIsFulfilled is false.
- 40: Applies the filter to all child lines.
- 30: Counts how many unfulfilled lines there are.
- 20: Checks if there is at least one.
- 10: Returns false if there are any unfulfilled lines, true if all are fulfilled.

## Attribute: ExecutionStatus

### Expression
```
10: IIF EXP:20 CONST:NotStarted EXP:30  
20: EQUAL ATTRIB:#Status_NotStarted CONST:True  
30: IIF EXP:40 CONST:Completed EXP:50  
40: EQUAL ATTRIB:#Status_Fulfilled CONST:True  
50: IIF EXP:60 CONST:ClosedWithIssues CONST:InProgress  
60: GTE EXP:70 CONST:40  
70: CAST ATTRIB:State CONST:System.Int32
```
### Explanation

- 20: Checks if the order has no fulfillments.
- 40: Checks if all lines are fulfilled.
- 60–70: Checks if the document state is greater than or equal to 40.
- 10: Returns NotStarted, Completed, ClosedWithIssues or InProgress depending on the conditions above.

## Summary

- #LineIsFulfilled determines whether a single line is fulfilled based on fulfillment documents and quantity comparison.
- #Status_NotStarted checks if there are no fulfillments in the order.
- #Status_Fulfilled verifies whether all lines in the order are fulfilled.
- ExecutionStatus combines the above with the document state to provide a readable and traceable status for the order lifecycle.
