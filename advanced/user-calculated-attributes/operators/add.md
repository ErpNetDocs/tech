---
uid: cao-add
---
# ADD - Calculated Attribute Operator

| Specification | Value |
| ---- | ----- |
| Name | ADD |
| Description | The operator returns the sum of two numbers. |
| Parameter 1 Name | Number1 |
| Parameter 1 Type | numeric type - int, double or decimal |
| Parameter 2 Name | Number2 |
| Parameter 2 Type | numeric type - int, double or decimal |
| Parameter 3 Name |
| Parameter 3 Type | 
| Return Value | Number1 + Number2 |

> [!NOTE]
> Ensure that the numbers which are summed up have the same type. For example, Parameter 1 and Parameter 2 must be both integers, or doubles, or decimals.

## Example

If the user wants to see what is the total Quantity of the material in a Recipe which would include the Used Quantity and the Scrap Rate, he would add the following Calculated Attribute:

Repository Name: Production.Technologies.RecipeIngredients
Name: TotalUsedQuantity

And the Calculated Attribute expressions are as follows:

```
10: ADD ATTRIB:UsageQuantityValue EXP:20
20: MULTIPLY ATTRIB:UsageQuantityValue ATTRIB:ScrapRate
```

```
Explanation:
10: Add the result from expression 20 to the attribute UsageQuantityValue
20: Multiply UsageQuantityValue and ScrapRate
```
