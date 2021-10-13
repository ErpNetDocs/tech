---
uid: master-detail
---

# Master / Detail attributes

When a document has the same field in its header and lines then these two fields interact in a specific manner. An example of such fields is the Store field in the sales order header and line store in its sales order lines.

The common principle is that if the field in the document header has value, we have to ensure that the corresponding field all document lines contains the same value. On the other hand, if the different lines contain different values - the document's header field must be empty.

This principle is very important to avoid misleading the users. Otherwise, if the Store field in the document header could contain a value even if the document lines have different store values - the user may look only in the header and be misled that this store applies to all of its lines as well, which may not be true in all cases.

## Master / Detail attributes concepts and rules

In order to make sure that the main principle described above is followed, is created a set of requirements and rules that are applied for each set of Master/Detail fields. 

*The example for Store fields in document header/lines is used in the whole description for easy understanding.*

### Concepts

1. In order to allow that different lines may contain different stores and at the same time to follow the main principle - we have to make sure that the Store field in the document header may contain empty (NULL) values. Such value is set only when the document lines have different values. Opposite of this, the value in the field in the document lines is required/mandatory [Required = true] and must always contain a value.

2. It is accepted that the main/leading field is the field in the lines - it is required/mandatory, i.e. there is a guarantee that it always contains a value. For example, if we are generating a store orders from sales orders - the store field that is taken into account is the one in the sales order lines. We have to create separate store orders for each line store in order to execute the sales order correctly because in the store orders there is only one store field and it is in the header.

3. If the document does not contain any lines, then there is no limitation for the document header value - it doesn't matter if it is empty (NULL) and contains a value (not-NULL).

### Rules

- **FrontEnd rules**
1. When the value of the document header's field is changed, this value is automatically set to ALL document lines.

2. When all document lines have the same value in the Store field, then the field in the document header must contain the same value. The presence of a value in the document header field is an ease for the users - it is not necessary to constantly monitor whether the lines have different values or not.
<br/>For this reason - after editing the value in the Line Store field and when deleting lines - if it turns out that all lines contain the same Store value, then this value is automatically set in the document header field.

3. When the different document lines have different values in the Store field, then the field in the document header must be empty (NULL).
<br/>For this reason -  after editing the value in the Line Store field and when deleting lines, if it turns out that the line contains a different Store value, then the Store field in the document header is automatically set to an empty value (NULL).

4. When adding a new line, then in the Line Store field is set the default value that equal to the value from the document header (unless another default value is explicitly set). If the document header value is empty (NULL), then as a default value in the new line is considered the value from the previous lines. If this is impossible, hard or inapplicable - then the default value is empty (NULL).


- **BackEnd rules**
1. When the document header is saved, the master-detail field's value is updated according to the value of the lines field (if any lines). 
If all lines contain the same Store value, then this value is automatically set in the document header field.
If the line contains different Store values, then the Store field in the document header is automatically set to an empty value (NULL).

2. When а document line is saved, the master-detail field's value is updated according to the value of the field in the header. 

3. When the document's header and lines are saved there is a final back end validation. If it turns out that despite the rules above, the values of the master-detail fields do not comply with the rules and principles above is thrown an error:
<br/>*The master attribute '{the name of the field in the header}' should have the same values as the detail '{the name of the field in the lines}' attribute for all lines or null, if there are different values through the lines.*
