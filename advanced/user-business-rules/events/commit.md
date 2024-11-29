---
uid: commit
items: events
---

# COMMIT

<br>

|Name|COMMIT
|:----|:----
|**Layer**|Back-end
|**Description**|Occurs when saving a change of an object.
|**Version**|Introduced: 2017.1  <br>Updated: -

This event occurs when data is **saved** into a database. It's used for all kinds of data types - definitions, documents and more. When an object change is saved, the rule is activated, as long as it meets the conditions.

COMMIT may be used to **validate** that all necessary data of a product is entered. If not - an **error** could be thrown (with the help of **[FAIL](https://docs.erp.net/tech/advanced/user-business-rules/action-types/fail.html)**) and the product wouldn't be saved in the database until correct data is entered.
