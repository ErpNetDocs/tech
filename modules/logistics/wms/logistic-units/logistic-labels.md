---
uid: logistic-labels
---

# Logistic Labels 
**GS1 logistic labels** are standardized labels used to identify and track products throughout the supply chain. GS1 is a global organization that sets standards for product and **[Logistic Units](index.md)** identification and communication, and their logistic labeling standards are widely used in the retail and healthcare industries.

**The GS1 logistic label consists of three sections**:
-	**The top section** of the label contains information in free format that can be used by the label-making company for various purposes.
-	**The middle section** contains the encoded data in readable text format, in accordance with GS1 Standards.
-	**The last section** contains the barcode symbols. For the encoding of the information are used GS1 barcode identifiers.

![Logistic Label](pictures/logistic-label.png)

If the [Logistic Unit](index.md) is **homogeneous** (for more information, see [Logistic units types](index.md#logistic-units-types)) and therefore contains one type of trade item, in addition to the SSCC code, these labels can include trade item information. This typically includes a Global Trade Item Number (GTIN), which is a unique identifier assigned to each product, as well as other information such as the product description, batch or lot number, and expiration date. 

If the [Logistic Unit](index.md) is **heterogeneous** (for more information, see [Logistic units types](index.md#logistic-units-types)) and therefore contains different types of trade items that are identified with different GTINs, then it is NOT possible to include trade item information on the logistic label. In these cases the data about the expected Logistic Units contents is exchanged prior the shipment arrival using an **[Advance Shipping Notice (ASN)](asn.md)**. 

In @@name, the **logistic labels** are created and printed using the standard reports functionality. The labels are typically printed on adhesive labels that are affixed to **[Logistic Unit](index.md)**, and they are scanned at various points in the supply chain to ensure the product is properly tracked and accounted for.

By using standardized **logistic labels**, companies can improve the efficiency and accuracy of their supply chain operations, reduce the risk of errors and delays, and improve customer satisfaction by ensuring that the right products are delivered on time.
