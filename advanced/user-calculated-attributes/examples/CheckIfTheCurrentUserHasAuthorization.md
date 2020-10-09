---
items: CalculatedAttributeExamples
---

# Check If the Current User Has Authorization

If we want to determine if the user that is currently  logged in the system is authorized (to do, see, or edit an entity, for  example) we need to know which Group have such rights. When we have that information, we can simply create a calculated attribute that checks if the User is a part of this Group:

```
10: IIF  EXP: 20   CONST: True  CONST: False         
20: GTE EXP: 30  CONST: 1                                        
30: SUM  EXP: 40 CONST: 1                                       
40: SELECT  REPO: Systems.Security.UserGroups  EXP: 50                             
50: WHERE  EXP: 60  EXP:  80                                                                       
60: EQUAL  ATTRIB:  UserId  EXP : 70                                     
70: GETOBJVALUE  INPUT:10  SYS: UserId                                           
80: EQUAL  ATTRIB: GroupId  CONST: 5daf849d-9986-462f-9171-a23c1c5839b7                
     
```

> Explanation:
>
> 10: Check if EXP:20 is true or false. If EXP:20 is True - the calculated attribute displays the 'True' message, else - 'False'.
>
> 20: Check if the list EXP: 30 returns at least one record.
>
> 30: Return the count of records in the filtered list of EXP:40.
>
> 40: Select 'User Groups' filtered by EXP: 50.
>
> 50: The Filters are expression 60, expression 80...
>
> 60: Check if the UserId is equal to EXP:70.
>
> 70: Get the Id of the user that is currently editing the entity.
>
> 80: Check if the GroupId is equal to the Id of an authorized group.