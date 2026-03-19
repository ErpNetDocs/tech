# How to use function _"Replace with..."_

ERP.net allows you to replace _one_ product in a document line with _another_ product that has been defined as a valid **Replacement**. <br>
The feature is available in both the **Web Client** and the **Desktop Client**. It helps users select approved substitute products without searching manually and ensures that only currently valid replacements are offered.<br>

The product replacement function is executed within a document (an Offer, an Order...) and involves three main elements:

- **From Product**  
  The original product in the document line that will be replaced.

- **To Product**  
  The substitute product that replaces the original product.

- **Product Relation Type** with **System Type = Replacement**  
  The relation type that marks the link between the two products as a valid replacement relation.

A product can be replaced only when there is an active **Product Relation**  - relation validity period:

- **From Date** must be empty or earlier than or equal to the current date.
- **To Date** must be empty or later than or equal to the current date.

If the selected replacement relation includes a **QtyFactor**, the quantity in the document line is recalculated automatically when the replacement is performed.

When a replacement is selected, the original product is substituted with the replacement product, and the quantity is recalculated automatically using the defined QtyFactor.

In the next sections, you will see how to use this function in each client.

## In Desktop client 

**1.** Ensure that a product is already entered in the **Product** field of the document line. The function is available only when the field contains a product.

**2.** Right-click in the **Product** field and reveal the context menu;  
  
**3.** Click **Replace with...** in it - the system opens a filtered navigator with the available replacements for the current product;

![picture](../../pictures/replace_with.png)

**4.** In the navigator, select the desired product relation;

**5.** Confirm with button **Select** in the lower-right corner.

![picture](../../pictures/confirm_replacement.png)

**Result:**
- The selected replacement product is entered in the **same document line**, replacing the original product. The replacement does not create a new line;
- The quantity is recalculated in the same line. For example, if **QtyFactor = 2**, the original quantity is multiplied by 2;
- The price is updated.

![picture](../../pictures/replaced.png)

## In WEB Client
