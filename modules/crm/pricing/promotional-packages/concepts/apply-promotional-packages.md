# Apply promotional packages

@@name applies promotional packages in the sales order by determining how the selected package is reflected in the sales order lines.

This process covers two situations:

- applying a promotional package when it is newly assigned to the sales order;
- recalculating a promotional package that is already assigned to the sales order.

## Applying a newly assigned package

When a promotional package is assigned to the sales order and corresponding sales order lines do not yet exist, @@name creates the package lines in the sales order.

A new sales order line is created for each line in the promotional package definition.

For each created line, the system determines:

- the **Promotional Package** from the package assigned to the sales order;
- the **Product** from the corresponding promotional package line;
- the **Lot** from the corresponding promotional package line, if specified;
- the **Quantity** by multiplying the selected number of packages by the quantity in the corresponding promotional package line;
- the **Quantity Unit** as the base measurement unit of the product, because the package line quantity is defined in that unit;
- the **Unit Price** from the corresponding promotional package line, if specified;

The **Line Standard Discount Percent** is also determined during package application. The promotional package line can add to, cascade with, or replace the standard discount otherwise determined for the sales order line.

If the sales order line does not contain a **Line Store**, it is set to the sales order **Store**.

If the sales order line does not contain a **Required Delivery Date**, it is set to:

- the sales order **Required Delivery Date**, if specified;
- otherwise, a default required delivery date is calculated from the sales order **Document Date** plus the default delivery term days of the **Ship To Customer**, or, if these are not set, of the **Customer**.

## Recalculating an already applied package

When a promotional package is already assigned to the sales order, @@name recalculates its sales order lines after changes in the sales order context so that they remain synchronized with the current promotional package definition.

> [!NOTE]
> Promotional package lines are recalculated only when **Apply Trade Conditions** is enabled for the sales order and for the existing sales order lines of the package.

During recalculation, @@name first checks whether the existing sales order lines for the package should still remain in the sales order.

The lines are deleted when:

- the selected number of packages is zero;
- the promotional package has been removed from the sales order.

If sales order lines for the package still remain, @@name checks whether they still correspond to the current promotional package definition.

The existing lines are reused and updated only when:

- their number is equal to the number of lines in the promotional package;
- their products correspond to the products in the package lines in the same order.

Otherwise, the existing lines are deleted and created again from the current package definition.

Whether the existing lines are updated or created again, their quantities, prices, and discounts are recalculated according to the current package data and the current sales order context.

## Quantity calculation

The quantity of each sales order line is calculated as:

**Sales Order Line Quantity = Number Of Packages × Promotional Package Line Quantity**

## Pricing

If the promotional package line contains a unit price, that price is applied to the sales order line.

In this case:

- the **Product Price** reference is cleared;
- the package line unit price is converted to the document currency;
- the converted value is set as the sales order line **Unit Price**.

## Standard discount determination

When a sales order line is created or recalculated from a promotional package, its standard discount can also be affected by the package line settings.

The promotional package line can determine the standard discount in one of the following ways:

- **Add** - the package line adds its discount adjustment to the standard discount already determined for the line.
- **MarkDown** - the package line combines its discount adjustment with the standard discount already determined for the line as a cascading discount.
- **Replace** - the package line replaces the standard discount with the value of the discount adjustment.

If the promotional package line does not adjust or replace the standard discount, the standard discount is determined by the other applicable discount conditions, such as bonus programs and line discounts.

## Related topics

- [Determine available promotional packages](determine-available-promotional-packages.md)
- [Create basic promotional package](../create-basic-promotional-package.md)
- [Promotional package configuration](../configuration.md)
