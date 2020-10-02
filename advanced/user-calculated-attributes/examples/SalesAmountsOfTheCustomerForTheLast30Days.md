# Sales Amounts Of The Customer For The Last 30 Days

Let's say the user want to show a field in the Sales Order  which calculates the sales amounts of the selected customer for the last 30 days.

Such calculated attribute actually represents a report  with specific filters. If a user tries to get the sales of a client for  the last 30 days, he would open Sales Order Lines report and set the  following filters:

- Client
- Enterprise Company
- Enterprise Company Location (eventually)
- DocumentState (at least Released)
- Void (he probably won't need voided documents)
- Document Date

So the calculated attribute must [SELECT](select.md) the Sales Order Lines table and filter the records as described above.  Such calculated attribute would have the following parameters:

```
Repository Name: Crm.Sales.SalesOrders
Name: SOAmountsForTheLast30days
```

And the Calculated Attribute expressions are as follows:

```
10: SUM EXP:20 ATTRIB:LineAmountValue
20: SELECT REPO:Crm.Sales.SalesOrderLines EXP:30
30: WHERE EXP:40 EXP:90
40: AND EXP:50 EXP:70
50: EQUAL EXP:60 CONST:30
60: CAST EXP:61 CONST:System.Int32
61: GETOBJVALUE REF:Document ATTRIB:State
70: EQUAL EXP:80 CONST:False
80: GETOBJVALUE REF:Document ATTRIB:Void
90: AND EXP:100 EXP:130
100: AND EXP:101 EXP:160
101: EQUAL EXP:110 EXP:120
110: GETOBJVALUE REF:SalesOrder ATTRIB:CustomerId
120: GETOBJVALUE INPUT:10 ATTRIB:CustomerId
130: GTE EXP:140 EXP:150
140: GETOBJVALUE REF:SalesOrder ATTRIB:DocumentDate
150: ADDDAYS EXP:151 CONST:-30
151: GETOBJVALUE INPUT:10 ATTRIB:DocumentDate
160: EQUAL EXP:170 EXP:180
170: GETOBJVALUE REF:SalesOrder ATTRIB:EnterpriseCompanyId
180: GETOBJVALUE INPUT:10 ATTRIB:EnterpriseCompanyId
```

> Explanation:
>
> 10: Sum all records from expression 20 by their attribute LineAmountValue
>
> 20: Select 'Sales Order Lines' filtered by expression 30
>
> 30: the filter is expression 40 AND expression 50
>
> 40: expression 50 AND expression 70
>
> 50: check if expression 60 is equal to expression 30
>
> 60: cast expression 61 to "System.Int32" (this is integer)
>
> 61: get the value of attribute State of the referent object Document
>
> 70: check if expression 80 is equal to "False"
>
> 80: get the value of attribute Void of the referent object Document
>
> 90: expression 100 AND expression 130
>
> 100: expression 101 AND expression 160
>
> 101: check if expression 110 is equal to expression 120
>
> 110: get the value of attribute CustomerId of the referent object SalesOrder
>
> 120:get the value of attribute CustomerId of the input object of expression 10
>
> 130:  check if expression 140 is greater than or equal to expression 150
>
> 140: get the value of attribute DocumentDate of the referent object SalesOrder
>
> 150: add to expression 151 the value of "-30"
>
> 151: get the value of attribute DocumentDate of the input object of expression 10
>
> 160: check if expression 170 is equal to expression 180
>
> 170: get the value of attribute EnterpriseCompanyId of the referent object SalesOrder
>
> 180: get the value of attribute EnterpriseCompanyId of the input object of expression 10