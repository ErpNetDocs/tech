# Determine bonus program

Bonus programs allow promotional benefits to be defined under different conditions.

Typical examples include:

  - a bonus program valid for all customers;
  - a bonus program valid only for a specific customer;
  - a bonus program valid only for a specific ship to customer;
  - a bonus program valid only for a specific distribution channel;
  - a bonus program valid only for a specific price list;
  - a bonus program valid only for a limited period;
  - a bonus program valid only when the ordered quantity or amount reaches a defined threshold.

To determine the applicable bonus program in a specific business context, @@name evaluates the available bonus programs against the context data and then selects one to apply.

The determination has three stages:

1. @@name filters the available bonus programs by general applicability.
2. @@name filters the remaining bonus programs by line-based conditions.
3. If more than one bonus program remains applicable, @@name selects the one with the highest priority.

## Context data used to determine the bonus program

@@name evaluates the available bonus programs based on data from the current sales order and its lines.

Depending on the conditions defined in the bonus program, the following data can participate in the determination:

- Date
- Customer
- Ship To Customer
- Distribution Channel
- Price List
- Enterprise Company
- Enterprise Company Location
- Currency
- Sales order line data, such as Product, Quantity, and Line Amount

The context **Date** is taken from the sales order **Required Delivery Date**. If **Required Delivery Date** is empty, from **Document Date**.

## Filtering conditions

@@name filters the available bonus programs by comparing the conditions defined in each bonus program with the corresponding context data.

A bonus program remains in the candidate set only if all of the following conditions are met:

  - **Active** is true.
  - **Condition From Date** is empty or is earlier than or equal to the context Date.
  - **Condition To Date** is empty or is later than or equal to the context Date.
  - **Enterprise Company** is empty or is equal to the context Enterprise Company.
  - **Enterprise Company Location** is empty or is equal to the context Enterprise Company Location.
  - **Condition Customer** is empty or is equal to the context Customer.
  - **Condition Ship To Customer** is empty or is equal to the context Ship To Customer.
  - **Condition Distribution Channel** is empty or is equal to the context Distribution Channel.
  - **Condition Price List** is empty or is equal to the context Price List.
  - **Condition Customer Filter XML** is empty or the context Customer satisfies the filter.
  - **Condition Ship To Customer Filter XML** is empty or the context Ship To Customer satisfies the filter.
  - **Condition Distribution Channel Filter XML** is empty or the context Distribution Channel satisfies the filter.
  - **Condition Target Group** is empty or the context Customer belongs to the target group.

If any specified condition does not match, the bonus program is excluded from the candidate set.

## Line-based conditions

After the general filtering, @@name evaluates the remaining bonus programs against the sales order lines. All configured line-based conditions must be satisfied for a bonus program to remain applicable.

Lines that already have a bonus program or belong to a promotional package do not participate in this evaluation.

Product conditions determine which of the remaining sales order lines are relevant to the bonus program. They can be defined through **Condition Product**, the **Products** panel, or **Condition Product Group**, including its subgroups. If no product conditions are defined, the evaluation uses the sales order as its context.

If **Condition Product** is specified, products listed in the **Products** panel are ignored when calculating both the quantity and the amount used to evaluate the bonus program's conditions. This rule applies regardless of the **Sum Quantities Regardless Of Measurement Unit** setting.

### Product and quantity conditions

A bonus program remains applicable only if all of the following conditions are met:

- If the bonus program has a product condition, at least one participating sales order line matches it.
- **Condition Min Quantity** is empty or is less than or equal to the context quantity.
- **Condition Max Quantity** is empty or is greater than or equal to the context quantity.

The context quantity is calculated according to the product conditions and the **Sum Quantities Regardless Of Measurement Unit** setting. For details on which quantities contribute to this total and how measurement units affect the calculation, see [Sum Quantities Regardless Of Measurement Unit](../configuration.md#sum-quantities-regardless-of-measurement-unit).

If any of these conditions is not satisfied, the bonus program is excluded from the candidate set.

### Amount conditions

A bonus program remains applicable only if all of the following conditions are met:

- **Condition Min Amount** is empty or is less than or equal to the context **Amount**.
- **Condition Max Amount** is empty or is greater than or equal to the context **Amount**.
- If **Condition Min Amount** or **Condition Max Amount** is specified, **Condition Document Currency** is equal to the document currency.

> [!NOTE]
> Amount conditions are evaluated in the document currency. 
>
> If the bonus program has a product condition, the context **Amount** is the total amount of the participating sales order lines. Otherwise, it is the total amount of all sales order lines.

## Selection logic

After filtering and line-based evaluation, @@name may find one, many, or no applicable bonus programs.

- If no bonus program remains in the candidate set, no bonus program is determined.
- If exactly one bonus program remains, that bonus program is selected.
- If more than one bonus program remains, the bonus program with the highest priority is selected.

This ensures deterministic selection when multiple bonus programs are applicable in the same sales order context.

> [!NOTE]
> Bonus programs are considered only when the **Apply Trade Conditions** field is enabled on the sales order and on the relevant sales order lines.

## Result

The algorithm determines the bonus program applicable in the current sales order context.

If no bonus program satisfies the defined conditions, no bonus program is determined.

## Troubleshooting bonus program determination

When an expected bonus program is not determined, check the following:

1. Whether the bonus program is active.
2. Whether the context **Date** is within the **Condition From Date** / **Condition To Date** range.
3. Whether the **Customer**, **Ship To Customer**, **Distribution Channel**, and **Price List** match the defined conditions.
4. Whether the **Customer**, **Ship To Customer**, or **Distribution Channel** satisfies the corresponding filter.
5. Whether the **Customer** belongs to the defined **Target Group**.
6. Whether the sales order lines contain products that match the product condition, if such a condition is defined.
7. Whether the evaluated **Quantity** satisfies **Condition Min Quantity** / **Condition Max Quantity**.
8. Whether **Sum Quantities Regardless Of Measurement Unit** is enabled when the expected quantity total includes products with different base measurement units or products selected only by **Condition Product Group**, including its subgroups.
9. Whether **Condition Product** is specified, causing products listed in the **Products** panel to be ignored in the quantity and amount calculations.
10. Whether the evaluated **Amount** satisfies **Condition Min Amount** / **Condition Max Amount**.
11. Whether the document currency matches **Condition Document Currency**, when amount conditions are defined.
12. Whether a higher-priority bonus program is applicable in the same context.
13. Whether the **Apply Trade Conditions** field is enabled on the sales order and on the relevant sales order lines.

Keep in mind that:

- empty condition values mean "applies to all";
- filtering is performed before line-based evaluation;
- if the bonus program has a product condition, only sales order lines whose products match that condition participate in the product and quantity evaluation;
- lines that already have a bonus program or belong to a promotional package do not participate in this evaluation;
- when **Sum Quantities Regardless Of Measurement Unit** is disabled, quantities from additional triggering products with different base measurement units are not accumulated together;
- when **Sum Quantities Regardless Of Measurement Unit** is enabled and a quantity threshold is specified, the numeric base quantities of all participating lines are summed without conversion between measurement units;
- if more than one bonus program is applicable, the bonus program with the highest priority is selected.

## See also

- [Create product bonus program](../getting-started/create-basic-product-bonus-program.md)
- [Create discount bonus program](../getting-started/create-basic-discount-bonus-program.md)
- [Create cascade discount bonus program](../getting-started/create-basic-cascade-discount-bonus-program.md)
- [Configuring bonus programs](../configuration.md)
