---
uid: beforerecalculate
items: events
---

# BEFORERECALCULATE

<br />

|Name|BEFORERECALCULATE|
|:----|:----|
|**Layer**|Front-end|
|**Description**|Occurs before every recalculation of the amounts in the document.|
|**Version**|Introduced: 2025 <br/> Updated: -|

This event occurs before every recalculation of the amounts in the **logistic documents**. It can be used in the headers of documents, the rows with prices and amounts, and the additional amounts for documents.

The recalculation occurs at different times depending on the key **DisableDocumentRecalculationOnIdle**.

- If **DisableDocumentRecalculationOnIdle <> 1**, it happens after entering each row as well as when certain fields in the header are changed.
- If **DisableDocumentRecalculationOnIdle = 1**, it happens upon saving the document.

**BEFORERECALCULATE**  would be to used it in rules for additional amounts in documents, such as applying discounts or changing the VAT rate depending on other fields in the document.

> [!NOTE]
> 
> It should be noted that BEFORERECALCULATE can only be used in **Front-End** rules.