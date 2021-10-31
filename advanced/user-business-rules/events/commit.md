# COMMIT
## Event summary
|Name|COMMIT
|:----|:----
|**Layer**|**Back-End**
|**Description**|**Occurs when saving a change of the object.**
|**Version**|**Introduced: 2017.1  <br>Updated: -**
 
Occurs when data is saved into the database. It is used for all kinds of data types - definitions, documents and more.

Every time an object change is saved, the rule is activated (if it meets the conditions).

The COMMIT event may be used, for example, to validate that all the necessary data of a product is entered. If not - throw an error (by using [FAIL](https://docs.erp.net/tech/advanced/user-business-rules/action-types/fail.html) action) and do not save the product in the database until the entered data is correct.
