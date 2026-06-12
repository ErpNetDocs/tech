# Determine available promotional packages

@@name determines the promotional packages available for selection in a sales order based on the package conditions and the current sales order context.

## Context data used to determine the available promotional packages

@@name evaluates the available promotional packages based on data from the current sales order.

Depending on the conditions defined in the promotional package, the following data can participate in the determination:

- Date
- Customer
- Ship To Customer
- Distribution Channel
- Price List
- Enterprise Company
- Enterprise Company Location

The context ****Date**** is taken from the sales order ****Required Delivery Date****.  
If ****Required Delivery Date**** is empty, the ****Document Date**** is used.

> [!NOTE]
> The customer is required for promotional package determination.  
> If the sales order does not contain a customer, no promotional packages are available for selection.

## Filtering conditions

@@name filters the available promotional packages by comparing the conditions defined in each package with the corresponding context data.

A promotional package remains available for selection only if the package satisfies all applicable conditions:

- ****Active**** is true.
- ****Valid From Date**** is empty or is earlier than or equal to the context ****Date****.
- ****Valid To Date**** is empty or is later than or equal to the context ****Date****.
- ****Valid For Customer**** is empty or is equal to the context ****Customer****.
- ****Valid For Ship To Customer**** is empty or is equal to the context ****Ship To Customer****.
- ****Valid For Distribution Channel**** is empty or is equal to the context ****Distribution Channel****.
- ****Valid For Price List**** is empty or is equal to the context ****Price List****.
- ****Valid For Enterprise Company**** is empty or is equal to the context ****Enterprise Company****.
- ****Valid For Enterprise Company Location**** is empty or is equal to the context ****Enterprise Company Location****.
- ****Valid For Customer Filter XML**** is empty or the context ****Customer**** satisfies the filter.
- ****Valid For Ship To Customer Filter XML**** is empty or the context ****Ship To Customer**** satisfies the filter.
- ****Valid For Distribution Channel Filter XML**** is empty or the context ****Distribution Channel**** satisfies the filter.
- ****Valid For Target Group**** is empty or the context ****Customer**** belongs to the target group.

If any specified condition does not match, the promotional package is excluded from the candidate set.

## Result

The result of the determination is the set of promotional packages that are available for selection in the sales order.

## Troubleshooting

### Why are no promotional packages available for selection?

- The sales order does not contain a **Customer**.
- There are no active promotional packages that match the current sales order context.
- The package validity period does not include the context **Date**.

### Why is a specific promotional package not available?

- The package is not active.
- The package is not valid for the context **Date**.
- The package is restricted to another **Customer**.
- The package is restricted to another **Ship To Customer**.
- The package is restricted to another **Distribution Channel**.
- The package is restricted to another **Price List**.
- The package is restricted to another **Enterprise Company**.
- The package is restricted to another **Enterprise Company Location**.
- The context **Customer** does not belong to the package **Valid For Target Group**.
- The context **Customer**, **Ship To Customer**, or **Distribution Channel** does not satisfy the corresponding filter XML condition.

### Why is the package not available on the expected date?

- Promotional package validity is checked against the sales order **Required Delivery Date**.
- If **Required Delivery Date** is empty, the system uses the sales order **Document Date**.

### Why is a package available in one sales order but not in another?

- The two sales orders have different context data, such as **Customer**, **Ship To Customer**, **Distribution Channel**, **Price List**, **Enterprise Company**, or **Enterprise Company Location**.
- The package filters or target group conditions are satisfied in one sales order but not in the other.
- The two sales orders use different determination dates.

## Related topics

- [Apply promotional packages](determine-available-promotional-packages.md)
- [Create basic promotional package](../create-basic-promotional-package.md)
- [Promotional package configuration](../configuration.md)
