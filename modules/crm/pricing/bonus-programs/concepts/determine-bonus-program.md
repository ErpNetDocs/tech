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

After the general filtering, @@name evaluates the remaining bonus programs against the sales order lines.

If a bonus program contains multiple line-based conditions, all of them must match for the program to remain applicable.

If the bonus program has no product condition, the evaluation is based on all sales order lines. If product conditions are defined through **Condition Product**, the **Products** panel, or **Condition Product Group**, including its subgroups, only lines whose products match those conditions participate in product and quantity evaluation.

Lines that already have a bonus program or belong to a promotional package do not participate in this evaluation.

### Product and quantity conditions

A bonus program remains applicable only if all of the following conditions are met:

- If the bonus program has a product condition, at least one participating sales order line matches it.
- **Condition Min Quantity** is empty or is less than or equal to the context quantity.
- **Condition Max Quantity** is empty or is greater than or equal to the context quantity.

The context quantity is calculated from the participating sales order lines. The calculation depends on **Sum Quantities Regardless Of Measurement Unit**.

When **Sum Quantities Regardless Of Measurement Unit** is disabled, the following restrictions apply to the context quantity calculation:

- For additional triggering products configured in the **Products** panel, quantities from products with a different base measurement unit are excluded from the total.
- Products matched only through **Condition Product Group**, including its subgroups, do not contribute to the total, even if they all have the same base measurement unit.

These restrictions concern only the quantity used to check **Condition Min Quantity** and **Condition Max Quantity**.

When **Sum Quantities Regardless Of Measurement Unit** is enabled and at least one quantity threshold is specified, @@name calculates the context quantity as follows:

- The numeric base quantities of matching products configured through **Condition Product**, the **Products** panel, or **Condition Product Group**, including its subgroups, are summed.
- The products' base measurement units do not have to match.
- No conversion between measurement units is performed.

> [!IMPORTANT]
> The total is a numeric value for evaluating the bonus program's quantity conditions. It is not a physical quantity expressed in a common measurement unit.

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
8. Whether **Sum Quantities Regardless Of Measurement Unit** is enabled when the expected quantity total includes products with different base measurement units.
9. Whether the evaluated **Amount** satisfies **Condition Min Amount** / **Condition Max Amount**.
10. Whether the document currency matches **Condition Document Currency**, when amount conditions are defined.
11. Whether a higher-priority bonus program is applicable in the same context.
12. Whether the **Apply Trade Conditions** field is enabled on the sales order and on the relevant sales order lines.

Keep in mind that:

- empty condition values mean "applies to all";
- filtering is performed before line-based evaluation;
- if the bonus program has a product condition, only sales order lines whose products match that condition participate in the product and quantity evaluation;
- lines that already have a bonus program or belong to a promotional package do not participate in this evaluation;
- when **Sum Quantities Regardless Of Measurement Unit** is disabled, quantities from additional triggering products with different base measurement units are not accumulated together;
- when **Sum Quantities Regardless Of Measurement Unit** is enabled and a quantity threshold is specified, the numeric base quantities of all participating lines are summed without conversion between measurement units;
- when quantity conditions are used with additional triggering products, quantities from products with different base measurement units are not accumulated together;
- if more than one bonus program is applicable, the bonus program with the highest priority is selected.

## See also

- [Create product bonus program](../getting-started/create-basic-product-bonus-program.md)
- [Create discount bonus program](../getting-started/create-basic-discount-bonus-program.md)
- [Create cascade discount bonus program](../getting-started/create-basic-cascade-discount-bonus-program.md)
- [Configuring bonus programs](../configuration.md)
