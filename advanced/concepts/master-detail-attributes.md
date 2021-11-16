---
uid: master-detail
---

# Master / Detail attributes

When a document has identical fields in its header and lines, these fields interact in a specific manner. 

An example is the *Store* field in the sales order header and lines.

If a field in the document header has a value, you need to make sure that the corresponding field in the document lines contains **the same** value. On the other hand, if the different lines contain different values, the document's header field should be **empty**.

When this principle isn't obeyed and the *Store* field in the document header contains a value despite the document lines having different store values, you may look in the header and think that this store applies to all of its lines as well, which may not be true.

### Concepts and rules

To make sure the main principle described above is followed, requirements and rules are applied to each set of Master/Detail fields. 
#### Concepts

- In order to allow different lines to contain different stores and at the same time follow the main principle, you need to make sure that the *Store* field in the document header contains **empty** (NULL) values. 

Such values are set only when the document lines have different values. In contrast, the value in the field in the document lines is **required/mandatory** (TRUE) and must always contain a value.

- The main/leading field is the required/mandatory field in the lines. It's set to always contain a value. 
 
For example, if you're generating a store order from a sale order, the _Store_ field taken into account is the one in the sales order lines. You need to create a **separate** store order for each store line in order to execute the sales order correctly. Keep in mind that in store orders, there's **only one** _Store_ field, and it's in the header.

- If the document doesn't contain any lines, then there's **no** limitation for the document header value. 
 
It doesn't matter if it's empty (NULL) or if it contains a value (not-NULL).
#### Front-end rules

- When the value of the document header's field is changed, this value is automatically set to **ALL** document lines.

- When all document lines have the same value in the *Store* field, the field in the document header must contain **the same** value. 
 
The presence of a value in the document header field makes it unnecessary to constantly monitor whether the lines have different values or not. For this reason, when editing the value in the _Line Store_ field or deleting lines, if it turns out that all lines contain the same _Store_ value, then this value is **automatically** set in the document header field.

- When different document lines have different values in the *Store* field, the field in the document header must be **empty** (NULL).

For this reason, after editing the value in the _Line Store_ field and when deleting lines, if it turns out that the line contains a different _Store_ value, then this value is **automatically** set as empty in the document header.

- When adding a new line, you're setting the default value in the _Line Store_ field, which **equals** the one in the document header (unless another default value is explicitly set).
 
If the document header value is empty (NULL), the value from the previous lines is considered as a default value in the new line. If this is impossible, then the default value remains **empty** (NULL).
#### Back-end rules

- When the document header is saved, the master/detail field's value is updated according to the value of the **lines** field. 

If all lines contain the same _Store_ value, this value is **automatically** set in the document header field.

If the lines contain different _Store_ values, the *Store* field in the document header is automatically set to **NULL**.

- When а document line is saved, the master/detail field's value is updated according to the value of the field in the **header**. 

- When the document's header and lines are saved, there is a final back-end validation. 
 
If it turns out that despite the rules above, the values of the master/detail fields are invalid, an error is thrown:

*The master attribute '{the name of the field in the header}' should have the same values as the detail '{the name of the field in the lines}' attribute for all lines or null, if there are different values through the lines.*
