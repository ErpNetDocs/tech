---
items: CalculatedAttributeExamples
---

# Check whether the releasing of the document is first or not

Sometimes we may want to know whether the Released state of document is selected for a first time or not. For example, a business case may require a certain  business rule to be executed only when first releasing the document. The calculated attributes are a tool which when triggered perform their calculation in real time. This means that if we use a calculated attribute as a condition for a business rule, the condition may be fulfilled today, but not tomorrow and if we reselect the document state it may trigger actions that are no longer needed for this record (for more information, see **How to start a business rule only on first releasing**). To avoid such an occurrence, we can use a calculated attribute to define whether the releasing of the document is first or not.

```
10: IIF  EXP:20 CONST:false CONST:true
20: EQUAL EXP:30 CONST:30                                  
30: CAST ATTRIB:State CONST:System.Int32         

```

**Explanation:**

- 10: Check if EXP:20 is true or false. If EXP:20 is True - the calculated attribute displays 'True', else - 'False'.
- 20: Check if EXP:20 is equal to "30".
- 30: Cast the state of the document to integer. State 'Released' is stored as "30".<br> 


For more information, see **[DocumentState enumeration](https://restdev.erp.bg/model/html/243d08d2-1bd6-f223-c454-1c488e51648f.htm)**.
