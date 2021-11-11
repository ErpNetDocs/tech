---
items: CalculatedAttributeExamples
---

# Check whether the releasing of the document is first or not

Sometimes, you may want to know whether the 'Released' state of document is selected for the first time or not. 

For example, a business case may require a certain business rule to be executed only upon first releasing of the document. 

The calculated attributes are a tool which, upon trigger, performs its calculation in **real-time**. If you use a calculated attribute as a condition for a business rule, the condition may be fulfilled today, but not tomorrow. If you reselect the document state, it may trigger actions that are no longer needed for this record (for more information, see **How to start a business rule only on first releasing**).

To avoid such an occurrence, you can use a calculated attribute to define whether the releasing of the document is first or not:

```
10: IIF  EXP:20 CONST:false CONST:true
20: EQUAL EXP:30 CONST:30                                  
30: CAST ATTRIB:State CONST:System.Int32         

```

**Explanation:**

- 10: Check if EXP:20 is true or false. If EXP:20 is true - the calculated attribute displays 'True', else - 'False'.
- 20: Check if EXP:20 is equal to '30'.
- 30: Cast the state of the document to integer. State 'Released' is stored as '30'.<br> 


For more information, see **[DocumentState enumeration](https://restdev.erp.bg/model/html/243d08d2-1bd6-f223-c454-1c488e51648f.htm)**.
