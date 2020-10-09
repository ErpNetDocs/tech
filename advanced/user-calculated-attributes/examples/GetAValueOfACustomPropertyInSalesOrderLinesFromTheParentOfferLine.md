---
items: CalculatedAttributeExamples
---

# Get a Value of a Custom Property in Sales Order Lines from the Parent Offer Line

With this attribute we can for example, determine what is  the value of a particular customer property which is set for the parent  offer line of the current sales order line. Currently, offer lines  customer properties are not automatically transferred to the sales  order. Thus, we can use this attribute in a [User Business Rule](https://docs.erp.net/tech/user-business-rules-35586099.html) to automate the process. For more information how to create a such [User Business Rule](https://docs.erp.net/tech/user-business-rules-35586099.html), see topic '[How to Use Business Rules to Set a Value into a Custom Property?](https://docs.erp.net/tech/how-to-use-business-rules-to-set-a-value-into-a-custom-property-57344004.html)'.



```
Repository: Crm.Sales.SalesOrderLines
```

```
                    
10:    GETOBJVALUE    EXP: 20    ATTRIB: @Propery1                 
20:    FIRST    EXP: 30                                                       
30:    FILTER    EXP: 70        EXP: 40                               
40:    EQUAL    ATTRIB: LineNo     EXP: 50                   
50:    CAST    EXP: 60    CONST: System.Int32                          
60:    GETOBJVALUE     INPUT: 10      ATTRIB: ParentLineNo                        
70:    GETOBJVALUE     EXP: 80     CHILD: Lines                          
80:    CAST    REF: ParentDocument     CONST: Aloe.EnterpriseOne.Model.Crm.Presales.Offer                
```



> Explanation:
>
> 10: Get the record of custom property "Propery1" from EXP: 20. 
>
> 20: Get the first value of EXP: 30.
>
> 30: Filter the list from EXP: 70 with the filters from EXP: 40.
>
> 40: Check in the LineNumber of the offer line is equal to the value from EXP: 50.
>
> 50: Cast EXP:60 to "System.Int32".
>
> 60: Get the”ParentLineNo“ of the sales order line which is an input for EXP:10.
>
> 70: Get the list of child line of the object of EXP: 80.
>
> 80: Cast the “Parent Document” of the sales order line to  "Aloe.EnterpriseOne.Model.Crm.Presales.Offer" in order to define the  type/entity of the parent document.