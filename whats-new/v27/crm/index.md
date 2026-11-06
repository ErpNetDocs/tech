# CRM

## Notable features

## Other features

### 1. Bonus programs - Sum Quantities Regardless Of Measurement Unit

The new **Sum Quantities Regardless Of Measurement Unit** checkbox in the bonus program definition allows products with different base measurement units to contribute to a shared quantity threshold. This supports bonus programs based on the combined numeric quantity of products selected through the **Products** panel or **Condition Product Group**, including its subgroups.

When the checkbox is selected, ERP.net sums the numeric base quantities of matching products regardless of their base measurement units, then compares the total with **Condition Min Quantity** and/or **Condition Max Quantity**. No conversion between measurement units is performed: for example, **60 pcs** of one product and **40 hours** of another contribute a numeric total of **100**, satisfying a minimum quantity threshold of **100**.

The checkbox is **disabled by default**, preserving existing behavior: quantities from products with different base measurement units are not added together, and products matched only through **Condition Product Group** do not contribute to the quantity total.

For configuration details and examples, see [Configuring bonus programs](../../../modules/crm/pricing/bonus-programs/configuration.md#sum-quantities-regardless-of-measurement-unit).
