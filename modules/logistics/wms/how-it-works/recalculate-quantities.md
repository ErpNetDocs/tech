# Recalculating quantities in the WMS Worker 

If a product has a defined additional **coding system** with a default base measurement category, it is possible to **recalculate** the product's quantities when scanning its coding system in the WMS Worker app.

**For example:**

You have an order which contains dozens of pcs of coffee which arrive in a box with its own unique code. As long as the box is defined for the coffee as an additional coding system and has a default base measurement category (e.g. 20pcs), you will be able to instantly count **multiple** instances of coffee with a **single** scan of the box's product code. This **overrides** the product's own default unit.

If no measurement category is set, the product will still be recognized but its default unit (e.g. 1pcs) will be taken into account instead.

### Prerequisites

1. Make sure your product has a defined **coding system**.
   
    You can find a list of all coding systems and create new ones on demand in the **Web Client**.

2. Use the **WMS Worker App** to open an order and scan the defined coding system of the products.

## How it works

Assuming your order contains a box with several instances of products, you can scan their coding system's product code right away.

1. Within the **SCAN** field, provide the respective code, or use your mobile device to scan the barcode of the box.
   
2. The standard **Quantity** step will be skipped and you will only need to select a **lot**.

3. You will get a **suggested** quantity to add to the scan, after which you can click **Next** to confirm the operation.

4. Instead of the default product unit, several or all pcs of the product will be scanned **instantly**.

