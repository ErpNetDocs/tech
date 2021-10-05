---
uid: document-generation-and-transitional-documents
---

# Document Generation and Transitional Documents

## Transitional document setup

To setup a document type as transitional:

1. Go to the document type definition and select "Transitional Document".
2. To generate documents of this type, use only generations, that support transitional document generation.

## Deterministic Generations

Not all generations support generating and adjusting (patching) a transitional document. 
Since the adjustment (patch) procedure supports matching the lines primarily by **Line No**, the generation should guarantee to always generate the same line numbers, given the same starting document.

In other words, if we execute the generation several times for the same document, the same resulting line numbers will be generated. This can be guaranteed if the generation generates the sub-document(s) using data only from the source (parent) document and **does not** look outside it. 
Common external data, that can make a generation **non-deterministic** include: 

- Using date or time
- Using available quantities
- Using data from the definitions of related objects

Actually, generations sometimes use outside data and are still considered **deterministic**.
The main driving factor is whether the outside data influences the resulting line numbers.
If the generation uses outside data, but still maintains generating the same line numbers, it is still considered deterministic for the purposes of document generation.

Most commonly, deterministic generations simply:

1. Generate exactly one line for each parent line.
2. Use the line number from the parent line to set the line number of the generated line (e.g. they do not use auto-numbering).

For example, let's have the following Sales Order:

Sales Order Line 10: Product1 Qty=15

Sales Order Line 20: Product2 Qty=25

Let's have two generations, that use this input to create a Store Order:

1. **Generation A**
   Generates the Store Order using strictly the data from the Sales Order and generates:
   Store Order Line **10**: Product1 Qty=15
   Store Order Line **20**: Product2 Qty=25

   Generation A is **deterministic** and can support adjusting transitional documents.

2. **Generation B**

   The generation uses the current available quantities to split the lines of the sales order, based on the availability of the different lots. This generation creates:

   Store Order Line **10**: Product1 Lot11 Qty=8
   Store Order Line **20**: Product1 Lot12 Qty=7
   Store Order Line **30**: Product2 Lot21 Qty=25

   Generation B obviously cannot be used to adjust (patch) the generated document, because the line numbers of the generated document will vary, based on the current availability.

   Generation B is **non-deterministic**

## Adjustment Procedure

When a transitional document is generated, if later the document needs to be adjusted (to be in-line with its parent), an *Adjustment Document* is created.
The adjustment document is a document, which contains **changes**. It is a peer document in the document tree and is usually hidden. 
The adjustment document is used to adjust (patch) the main document. The adjustment is executed upon setting the "Adjustment" document status.
After the adjustment, the main document is updated to reflect the changes brought by the adjustment document.

## Generating Adjustment Documents

When a generation, which supports adjusting transitional documents, is executed, it checks the sub-documents. If it founds documents, that can be adjusted (patched), it automatically generates changes-only document(s). The generations usually determine the changes in the following way:

1. If quantity, amount or other **scalar** attribute is updated, a changes line is generated, containing the numeric difference between the scalars.
2. If notes, dates or other **non-scalar** attribute is updated, a changes line is generated, containing the new values for the non-scalars.
3. Rule 1 and 2 can be combined. E.g. a changes line can combine both scalar and non-scalar changes. The main difference is, that scalars are updated with difference value, while non-scalars are updated with last value.
