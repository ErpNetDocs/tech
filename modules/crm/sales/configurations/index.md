# Sales Order Configurations

## Validation against free quantity

This behavior is controlled by the **Available quantity only** option in **Entity Settings / Sales Orders - Options** for the respective user-defined sales document type.

When this option is enabled, the sales document can be released only if there is sufficient available quantity.

This validation depends on whether the document generates planned store orders for the stock-managed quantities. If the document participates in the inventory planning flow, its quantities affect the future availability calculation and the release can be blocked when the free quantity falls below zero.

If the document does not generate at least planned store orders, the expected restriction may not be triggered in the same way. However, if the free quantity is already below zero before the sales document is released, the release is blocked even if no planned store orders are generated.

For more information about how availability is calculated, see [Available to promise](https://docs.erp.net/tech/modules/logistics/inventory/concepts/available-to-promise/index.html)..
