---
items: CalculatedAttributeExamples
---

# ExecutionStatus for Warehouse Orders

This example defines a calculated attribute that returns a descriptive status value for a warehouse order. The logic uses two supporting attributes:

1. #Status_NotStarted – returns True if the warehouse order has no fulfillments.
2. #Status_Fulfilled – returns True if there are no unfulfilled lines.

The final attribute, ExecutionStatus, evaluates those and returns one of the following values:

- NotStarted
- Completed
- CompletedWithIssues
- InProgress

## Step 1: Check if the Order is Not Started (#Status_NotStarted)

This attribute checks if the warehouse order has no fulfillments.

### Expression
```
10: IIF EXP:20 CONST:True CONST:False  
20: EQUAL EXP:30 CONST:0  
30: COUNT CHILD:Fulfillments
```
### Explanation

- 10: Returns True if EXP:20 is true; otherwise returns False.
- 20: Compares the result of EXP:30 to 0.
- 30: Counts how many fulfillments the warehouse order has.

## Step 2: Check if All Lines are Fulfilled (#Status_Fulfilled)

This attribute verifies whether all lines in the warehouse order are fulfilled.

### Expression
```
10: IIF EXP:20 CONST:false CONST:true  
20: GTE EXP:30 CONST:1  
30: COUNT EXP:40  
40: FILTER CHILD:Lines EXP:50  
50: EQUAL ATTRIB:#LineIsFulfilled CONST:false
```
### Explanation

- 10: Returns false if EXP:20 is true, true otherwise.
- 20: Checks if there is at least one line that is not fulfilled.
- 30: Counts lines filtered by EXP:40.
- 40: Filters child Lines based on EXP:50.
- 50: Filters lines where #LineIsFulfilled is false.

## Step 3: Determine Execution Status (ExecutionStatus)

This attribute returns a string value representing the current status of the warehouse order.

### Expression
```
10: IIF EXP:20 CONST:NotStarted EXP:30  
20: EQUAL ATTRIB:#Status_NotStarted CONST:True  
30: IIF EXP:40 CONST:Completed EXP:50  
40: EQUAL ATTRIB:#Status_Fulfilled CONST:True  
50: IIF EXP:60 CONST:CompletedWithIssues CONST:InProgress  
60: GTE EXP:70 CONST:40  
70: CAST ATTRIB:State CONST:System.Int32
```

### Explanation

- 10: If #Status_NotStarted is True → returns NotStarted.
- 30: If not, and #Status_Fulfilled is True → returns Completed.
- 50: Otherwise:
  - If document State (as integer) >= 40 → returns CompletedWithIssues.
  - Else → returns InProgress.

## Summary

- #Status_NotStarted checks whether the warehouse order has no fulfillments.
- #Status_Fulfilled ensures all lines in the order are fulfilled.
- ExecutionStatus combines both checks with the document state to give a readable, traceable lifecycle label for the order.

This attribute is intended for use in manager dashboards and WMS views to help warehouse supervisors track progress and identify issues quickly.
