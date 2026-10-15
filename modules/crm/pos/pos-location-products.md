# POS Location Products

**POS Location Products** defines the products offered for sale at a particular POS location. Each record links a product to a POS location and holds settings that apply to that combination, such as its status, validity period, gross price, and target stock quantities.

The same product can be included at multiple POS locations, with different settings for each location. This allows locations to share a product catalog while maintaining their own assortments.

POS Location Products does **not** create a new product or record actual stock on hand. It specifies how an existing product is offered at a POS location. Minimum and maximum quantities are targets; entering them does not, by itself, create a replenishment order or stock transfer.

## Purpose

POS Location Products is used to manage:

- **Location-specific assortments:** Which products are offered at each POS location.
- **Availability over time:** Whether a product is active and the period during which its record applies.
- **Location-specific prices:** The gross price associated with the product at the location.
- **Stock targets:** Minimum and maximum quantities that can be used as targets when monitoring or replenishing stock.
- **Product placement:** A description of where the product is normally kept at the location.

ERP.net Retail POS loads the products and prices for its selected POS location from these records. A product’s presence in the general product catalog alone does not add it to the location’s assortment.

## How availability works in Retail POS

Retail POS loads **active** POS Location Products records whose validity period includes the current date. A missing *Valid From* or *Valid To* date leaves that end of the period open.

Retail POS uses locally loaded data. Changes to a location’s assortment or prices in ERP.net become available in the app after a successful **Pull Data** operation; they should not be assumed to appear immediately on every device.

To avoid ambiguity, maintain validity periods carefully, particularly when more than one record for the same product and location could apply on the same date.


**Related documentation:** [POS Location Products — Domain Model](https://docs.erp.net/model/entities/Crm.Pos.LocationProducts.html) · [Retail POS — Pull Data](https://retailpos.app.erp.net/help/pull-data)
