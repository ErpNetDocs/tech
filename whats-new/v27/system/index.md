# System features

This section introduces **new and improved ERP.net system capabilities** that are not limited to a particular client or business module. These features extend how the platform stores, connects, validates, and makes data available. Where relevant, each update also explains how you can use it in the Desktop and Web clients.

## 1. Stored Attributes of Type Reference

Stored attributes now support a new **Reference** type. It lets you link a record to a specific record elsewhere in ERP.net—for example, to select a **Main customer** for a product.

To create one, add a stored attribute, set its **Property Type** to **Reference**, and select the target repository in **Allowed Values Entity Type**. You can then select a value for the attribute in both the Desktop and Web clients.

**How is this different from a Text attribute with entity-backed allowed values?** 

A Text attribute can also offer records from another repository as choices and may store the selected record’s ID. Those records, however, serve as the *source of allowed values*. With a Reference attribute, the selected record is treated as the *object the attribute refers to*. The record ID identifies the reference; its stored text is only a display representation, not the authoritative value. This reference visualized as a link, really links and leads to the exact record which can be opened and observed in WEB Client.

System Business rules help preserve the integrity of Reference attributes by validating their configuration and values. This makes references more reliable than depending on a displayed name, while giving users a familiar way to select linked records.

In the Web client, a Reference attribute can be selected from the entity’s **system items** when customizing a form—not only from the **Stored Attributes** section. The corresponding stored-attribute field, bears the suffix **“(A)”**, may also appear there - it is the text value of the reference. To change the selection, use the reference field.

Learn more from the dedicated page: [User-defined references](https://docs.erp.net/dev/domain-api/common-tasks/custom-property-references.html)

![picture](reference.png)

## 2. Master Document Activation and Deactivation Dates for Document Routes

Document routes now support two new optional fields: **Master Document Activation Date** and **Master Document Deactivation Date**.

When a document generates the next document through a route, the system can now check not only the date of the document performing the generation, but also the date of the original document that started the document flow.

For example, a **Warehouse Order** generated in November may belong to a document flow that started from a **Sales Order** dated in October. When the Warehouse Order generates the next document, the existing **Activation Date / Deactivation Date** fields check the Warehouse Order date, while the new master document dates check the date of the original Sales Order.

This makes it possible to introduce new routes for document flows started from a specific date, while unfinished older flows can continue using their previous routes.

The new fields are configured directly on the document route and work together with the existing activation dates and all other route conditions.

For configuration details, examples, and important considerations when changing existing routes, see [Route activation dates](../../../advanced/document-flow/route-activation-dates.md).

## 3. System-Calculated Attributes: Total Line Amount and Amount To Pay 

The **Total Line Amount** and **Amount To Pay** system-calculated attributes are being extended to **Invoice Orders, Receiving Orders, Purchase Invoices, and Offers (Total Line Amount only)**.

These attributes give users a convenient way to view key document amounts without manual calculations. 

👉**Total Line Amount** represents the sum of the document’s lines. For Offers, it includes **all lines**, including unselected alternatives.

👉**Amount to Pay** is the total amount payable for a document calculation - Total Line Amount + additional amounts marked “Add To Customer”. 
Those additional amounts can include VAT and other charges payable by the customer.

👉 **Both** calculated attributes can be displayed in the document header and in navigators, making key amounts easy to review. However, they cannot be used as search criteria in the advanced filter.

This enhancement makes financial figures easier to review when working with documents.
<br>
<img width="1373" height="821" alt="image" src="https://github.com/user-attachments/assets/3c601512-3e68-4df5-8c02-bb03a2993570" />
<br>


## 4. Product Type Properties Now Available in Purchase Invoice Lines in the Web Client

The Web Client now supports up to five custom properties in [Purchase invoice lines](https://docs.erp.net/model/entities/Logistics.Procurement.PurchaseInvoiceLines.html#linecustomproperty1), bringing functionality already available in the Desktop Client to the web interface.

These properties capture additional information about a specific purchase, such as a **project, cost center, or activity**. The product type determines which properties are relevant, helping users enter consistent information without searching through all custom properties available for purchase invoice lines. Where the accounting template is configured accordingly, these values can also be used to populate accounting analytics during posting.

Through **Customize panel** in the purchase invoice lines panel, users can **display** the five property positions as grid columns - section "Purchase invoice line properties".

<br>
<img width="876" height="331" alt="image" src="https://github.com/user-attachments/assets/68f6ccb5-d212-47a9-ad48-11de154d90db" />
<br>

Each position is linked to the corresponding custom property configured in the selected product’s **Product Type**. The same position can therefore represent different properties on different invoice lines—for example, “Project” for Product Type "Goods" and “Colour” for Product Type "Materials".

<br>
<img width="758" height="554" alt="image" src="https://github.com/user-attachments/assets/5de0ccef-e3ca-45df-bc98-766e7d13a132" />
<br>

Each Property 1-5 offers its configured allowed values. Values entered through these columns are stored in the invoice line’s existing custom properties—not as a separate set of data—and remain **synchronized** with other representations of the same property.<br>

<br>
<img width="1596" height="143" alt="image" src="https://github.com/user-attachments/assets/1d60a88f-988e-489c-b3c2-58fdff8ea9f5" />
<br>

The property columns **update dynamically** when the product on a line changes, reflecting the new product type’s configuration. Each position displays the corresponding custom property and offers its allowed values, so users always work with the properties relevant to the currently selected product.

This makes product-type-specific information easier to access and enter directly in the Web Client’s invoice grid.

Learn more about [Stored Attributes](https://docs.erp.net/tech/advanced/stored-attributes/index.html)
