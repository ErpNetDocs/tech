---
uid: defining-vat-and-base-for-vat-entries
---

# Defining VAT and Base for VAT Entries

The current article describes how the numeric values are defined - base and VAT, which are saved in the VAT Entries when this document is created automatically from other documents in EnterpriseOne. 
Currently the documents which creates VAT Entries are:

- Invoices (they create records in the VAT sales ledger entries);
- Transactions (they create records in the VAT sales ledger entries)

The calculations are performed in three stages:

1. Defining which document rows participate in the calculation.
2. Defining the deal types for each row.
3. Defining the base and the VAT for each deal type.

## 1. Defining The Participating Rows

Which rows participate in the calculation of the base and the VAT is defined for each document individually. 
The set of rows also depends on that if the document creates VAT sales or purchases ledger entries.

In **Invoices** *all rows* participate in the calculation.

In **Purchase Invoices** which create VAT purchases ledger entries *all rows* participate, too.

In **Purchase Invoices** which create VAT sales ledger entries there are two cases:

- if the document header has value in *Sale Deal Type* field, then *all rows* participate in the calculation;
- if the document header no value in Sales Deal Type field, then *only the rows which has value* in the *Sale Line Deal Type* field (this is the same field but in the document rows).

In **Transactions** all rows participate in the calculation.

## 2. Defining The Deal Types

For each row which participate in the calculation, a unique identification of the deal type of the row must be defined.
If for any of the rows this definition is impossible, the calculation process is interrupted and error message is displayed.

The deal type definition for a row depends on the document which it is part of and on that if the document creates VAT sales or purchases ledger entries.

For Invoice row - if the row has value in the *Line* *Deal Type* field, then the deal type is defined by this value. Otherwise, the value in the document header is used.

For Purchase Invoice (which creates VAT purchases ledger entries) row - the principle is the same as in the Invoice rows - if the row has value in *Line Deal Type* field, the deal type is defined by this value, otherwise - the *Deal Type* from the document header is used.

For Purchase Invoice (which creates VAT sales ledger entries) row - the same combination of corresponding fields from the rows and the document header is used, except the fields here are *Sales Line Deal Type* (in the rows) and *Sales Deal Type* (in the document header).

In Transactions all rows use a specific property of the document flows - *Deal Type* field from table "Transaction Entry Template". 
There are no specified fields in the document rows and header for the Deal Type.

## 3. Defining Base And VAT For Each Deal Type

All bases and VAT amounts are calculated only in base currency.

For all deal types, defined in stage 2, two values are calculated - [base] and [VAT]. 
To calculate them for the current deal type the rows, which has such deal type defined in stage 2, are used. 

### Example 1:

There is an Invoice with 7 rows:

- row #10, *Line Deal Type* = "DealType1", LineAmount = 32 EUR;
- row #20, *Line Deal Type* = "DealType2", LineAmount = 17 EUR;
- row #30, *Line Deal Type* = "DealType3", LineAmount = 41 EUR;
- row #40, *Line Deal Type* = "DealType1", LineAmount = 45 EUR;
- row #50, *Line Deal Type* = "DealType3", LineAmount = 55 EUR;
- row #60, *Line Deal Type* = "DealType3", LineAmount = 29 EUR;
- row #70, *Line Deal Type* = "DealType1", LineAmount = 24 EUR.

Thus, in the previous stage for the rows three deal types are defined - DealType1, DealTyope2 and DealType3.
Thus, three bases and three VATs must be calculated - [DealType1:base], [DealType2:base], [DealType3:base], [DealType1:VAT], [DealType2:VAT], [DealType3:VAT].
To calculate base and VAT for DealType1 the data from row #10, row #40 and row #70 are used. 
For the base and VAT of DealType2 only row #20 is used, and for DealType3 - row #30, row #50 and row# 60.

The VAT additional amount is set in the Enterprise Company definition (see [Additional Amounts](../advanced/documents/additional-amounts.md)) of the current document.
Id the document does not contain the specified VAT additional amount (or there is no such in the EnterpriseOne company definition),the calculation is interrupted by error message. 

The distributed additional amount on the rows are used in the calculation of the VAT amounts. 
And to calculate the bases amounts - the distributed VAT additional amounts which are added to the base and also the line amounts (but only if in the VAT additional amount Base On Lines is true).

The bases and VATs calculations are performed in three steps:

1. The amounts for each deal type is formed.
2. The rest of the VAT is processed.
3. VAT, which is calculated/distributed incorrectly, is re-distributed.

## Step 1

For each deal type two values are calculated - base and VAT. So a list of couples is formed, which has as much elements as deal types there are.
This is processed only if the VAT in the document is distributed by the current document (it is possible to distribute on other documents - if so, this step is skipped; it is possible to distribute both on the current document and on different documents - then this step is performed). 
If the step is skipped, then the list is empty.

So, for each deal type all rows, which has the specified deal type, are summed up and from each row the distributed VAT is extracted, the distributed amounts which are added to the Base also, and the line amounts, if the VAT is based on lines.
The value of [VAT] for the current deal type is the sum of the distributed VAT for all rows with this deal type.
And the value of [base] is the sum of the distributed amounts which are added to the VAT base and the line amounts (if the VAT is based on lines).

### Example 2:

Let's use the Invoice from **Example 1**. 
There is an additional amount VAT, which is 32.32 EUR and it is based on the line amounts and second additional amount "Loyal Customer Discount".
The discount amount is 40 EUR and the distribution of both additional amounts is as follows:

- row #10, distributed discount -7 EUR, distributed VAT 5 EUR;
- row #20, distributed discount -1 EUR, distributed VAT 1.12 EUR;
- row #30, distributed discount -14 EUR, distributed VAT 0 EUR;
- row #40, distributed discount -0 EUR, distributed VAT 9 EUR;
- row #50, distributed discount -11 EUR, distributed VAT 0 EUR;
- row #60, distributed discount -3 EUR, distributed VAT 5.2 EUR;
- row #70, distributed discount -4 EUR, distributed VAT 4 EUR.

Also the VAT amount is distributed not only on the current document but on other document row which has no other additional amounts and line amount of 40 EUR and the distributed VAT is 8 EUR.

Then the following calculations for base and VAT for the different deal types of the current document are received:

[DealType1: base] = 32 EUR + -7 EUR + 45 EUR + 0 EUR + 24 EUR + -4 EUR = 90 EUR;

[DealType2: base] = 17 EUR + -1 EUR = 16 EUR;

[DealType3: base] = 41 EUR + -14 EUR + 55 EUR + -11 EUR + 29 EUR + -3 EUR = 97 EUR;

[DealType1: VAT] = 5 EUR + 9 EUR + 4 EUR = 18 EUR;

[DealType2: VAT] = 1.12 EUR;

[DealType3: VAT] = 0 EUR + 0 EUR + 5.2 EUR = 5.2 EUR;

## Step 2

If any of the following is true:

- the list of couples of values from Step 1 is empty (this is possible if the VAT is not distributed on the current document);
- or the VAT is distributed on other documents also or either not the whole VAT is used when forming the VAT amounts in step 1 or not the whole VAT base is used when forming the bases.

Then the creation of a new couple of values is necessary - base and VAT. 
The deal type for this couple is extracted from the deal type field in the document header (and if the document is Transaction - then it is extracted from the document flow).
In the base and VAT for this deal type the remaining values from the base and VAT, which are not distributed in Step 1 from the other deal types, are recorded.

### Example 3:

Lets use the data from **Example 2** and the Invoice has a deal type in its header - DealType4. 
The VAT in the document is 32.32 EUR, and [DealType1: VAT] + [DealType2: VAT] + [DealType3: VAT] = 24.32 EUR. So there are 8 EUR remaining.

Also the total VAT base (from both documents) is 243 EUR, and [DealType1: base] + [DealType2: base] + [DealType3: base] = 203 EUR. 
So the remaining base is 40 EUR.

So a new couple of values is formed for DealType4:

[DealType4: base] = 40 EUR

[DealType4: VAT] = 8 EUR

## Step 3

At the end, there is a newly formed list of couples of values - base and VAT - for a number of deal types.
If one of those deal types does not support VAT and its calculated VAT in the list is not a zero, then a need of correction of those VATs and bases calculated by now, appears.

The correction is performed by resetting the VATs of all deal types, which VAT is distributed incorrectly in the documents, and these VATs are distributed amongst the other deal types, proportionally to their bases (if after this re-distribution there is still remaining amount because of roundings, then this small amount is distributed to the last deal type which supports VAT).

### Example 4:

Lets use the data from the previous examples and DealType1, DealType2 and DealType4 support VAT, and DealType3 does not.
So there is incorrectly distributed VAT of [DealType3:VAT] = 5.2 EUR. So the 5.25 EUR must be relocated to the rest of the deal types - the following correction is achieved:

[DealType3: VAT] = 0 EUR;

[DealType1: VAT] = 18 EUR + 5.2 EUR * 90 EUR / (90 EUR + 16 EUR + 40 EUR) = 21.21 EUR;

[DealType2: VAT] = 1.12 EUR + 5.2 EUR * 16 EUR / (90 EUR + 16 EUR + 40 EUR) = 1.69 EUR;

[DealType4: VAT] = 8 EUR + 5.2 EUR * 40 EUR / (90 EUR + 16 EUR + 40 EUR) = 9.42 EUR.
