---
uid: deterministic-generations
---

# Deterministic generations

Not all generations support generating and adjusting (patching) a transitional document. 

Since the adjustment (patch) procedure supports matching the lines primarily by _Line No._ the generation should guarantee to always generate the same line numbers, given the same starting document.

If you execute a generation several times for the same document, the same line numbers will be generated. This can be guaranteed if the generation creates the sub-document(s) using data only from the source (parent) document and **doesn't** look outside of it. 

Common external data that can make a generation **non-deterministic** includes: 

- Using date or time
- Using available quantities
- Using data from the definitions of related objects

Generations sometimes use outside data and are still considered **deterministic**.
The main driving factor is whether this outside data influences the resulting line numbers.
If a generation uses outside data, but still generates the same line numbers, it's considered **deterministic** for the purposes of document generation.

Most often, deterministic generations generate exactly **one** line for each parent line. They use the line number from the parent line to set the line number of the generated line (without auto-numbering).

For example, let's have the following sales order:

- sales order line 10: Product1 Qty=15
- sales order line 20: Product2 Qty=25

and two generations that use this input to create a store order:

**Generation A** generates the store order using strictly the data from the sales order and generates:
   
- store order line **10**: Product1 Qty=15
- store order line **20**: Product2 Qty=25

Generation A is **deterministic** and can support adjusting transitional documents.

**Generation B** uses the current available quantities to split the lines of the sales order, based on the availability of the different lots. It generates:

- store order line **10**: Product1 Lot11 Qty=8
- store order line **20**: Product1 Lot12 Qty=7
- store order line **30**: Product2 Lot21 Qty=25

Generation B **cannot** be used to adjust (patch) the generated document. 

The line numbers of the generated document will vary, based on the current availability.

Therefore, Generation B is **non-deterministic**
   
## Adjustment procedure

If a transitional document needs adjustment after it's generated (to be in-line with its parent), an **adjustment document** is created.
It's a peer document that contains **changes**, and is usually hidden in the document tree.

Such documents are used to **adjust** (patch) main documents. The operation is executed upon setting the adjustment document status.
Then, the main document is updated to reflect the changes.

## Generating adjustment documents

When a generation supporting adjustment of transitional documents is executed, it **checks** the sub-documents. 

If it founds documents that can be adjusted (patched), it automatically generates **changes-only** document(s). 

Generations usually determine the changes in the following way:

- If a quantity, amount or other **scalar** attribute is updated, a 'changes' line is generated, containing the numeric difference between the scalars.

- If notes, dates or other **non-scalar** attributes are updated, a 'changes' line is generated, containing the new values for the non-scalars.

- Rule 1 and 2 can be combined. A 'changes' line can include **both** scalar and non-scalar changes. However, scalars are updated with 'difference' value, while non-scalars are updated with 'last' value.
