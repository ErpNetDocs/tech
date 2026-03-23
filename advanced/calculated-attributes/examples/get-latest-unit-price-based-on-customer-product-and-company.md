---
items: CalculatedAttributeExamples
---

# Get latest unit price based on customer, product and company

This attribute can get the latest unit price used for the same customer and product within the same company. The result is determined by searching existing sales order lines, keeping only the lines that match the current product, customer, and company, excluding void documents, considering only documents with state 30 or higher, sorting the results by document date in descending order, and returning the unit price from the most recent matching line.

You can also use this attribute in a business rule or another formula when you need to fill or compare the unit price based on the latest sales data for a specific customer and product combination.

```
Repository: Crm.Sales.SalesOrderLines
```

```
5:   GETOBJVALUE EXP:10 ATTRIB:UnitPriceValue
10:  FIRST EXP:20
20:  SORT  EXP:30 EXP:25 CONST:DESC
25:  GETOBJVALUE REF:Document ATTRIB:DocumentDate
30:  SELECT  REPO:Crm.Sales.SalesOrderLines EXP:31
31:  TOP CONST:1 EXP:32
32:  ORDERBY EXP:33 CONST:DESC EXP:40
33:  GETOBJVALUE REF:Document ATTRIB:DocumentDate
40:  WHERE EXP:45 EXP:105
45:  AND EXP:50 EXP:54 EXP:51
50:  EQUAL EXP:60 EXP:70
60:  GETVALUE ATTRIB:ProductId
70:  GETOBJVALUE INPUT:30 ATTRIB:ProductId
54:  AND EXP:46 EXP:56
46:  EQUAL EXP:48 CONST:FALSE
48:  GETOBJVALUE REF:Document ATTRIB:Void
56:  EQUAL EXP:80 EXP:90
80:  GETOBJVALUE REF:SalesOrder ATTRIB:CustomerId
90:  GETOBJVALUE INPUT:30 EXP:100
100: GETOBJVALUE REF:SalesOrder ATTRIB:CustomerId
51:  GTE EXP:52 CONST:30
52:  CAST EXP:53 CONST:System.Int32
53:  GETOBJVALUE REF:Document ATTRIB:State
105: EQUAL EXP:110 EXP:120
110: GETOBJVALUE REF:Document ATTRIB:EnterpriseCompanyId
120: GETOBJVALUE INPUT:30 EXP:130
130: GETOBJVALUE REF:Document ATTRIB:EnterpriseCompanyId
```

**Explanation:**

5: Returns the UnitPriceValue from the object produced by EXP:10 (the selected “latest matching” line)  
  Note: In the entity schema the price field is UnitPrice (Amount); UnitPriceValue in expressions typically refers to the numeric value part of that amount  
  
**Build “latest matching line”** 
30 → 40: Builds a query (SELECT) over Crm.Sales.SalesOrderLines and applies filters (WHERE)  
40 (WHERE): Applies two main conditions:  
EXP:45 → matching product/customer and validity conditions  
EXP:105 → same enterprise company  

**Filter:** same product, same customer, valid document  
50 (EQUAL): Candidate line product = current line product  
60: gets current line ProductId  
70: gets candidate line ProductId  
56 (EQUAL): Candidate line’s SalesOrder.Customer = current line’s SalesOrder.Customer  
46 (EQUAL … FALSE): Candidate line’s document is not void (Void = false)  
51 (GTE … 30): Candidate line’s document State ≥ 30 (Released or later)  

**Filter: same enterprise compan**   
105 (EQUAL): Candidate line’s document enterprise company matches the current line’s document enterprise company  

**Sort and take top 1**  
32 (ORDERBY): Sorts by Document.DocumentDate descending (latest first)  
31 (TOP 1): Takes only the first result  
20 (SORT) + 10 (FIRST): Ensures the result set is ordered and then picks the first record (effectively the same “latest” line)  
Finally 5 extracts the unit price from that line  
