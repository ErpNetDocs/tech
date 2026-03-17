---
items: CalculatedAttributeExamples
---

# Check whether the current user is in the Manager group

This  attribute can check whether the current logged-in user is a member of a specific security group. The result is determined by searching the user group memberships for a record where the user matches the current system user and the group matches the specified group.  

You can also use this attribute in a business rule or another formula when you need to apply logic based on whether the current user belongs to the Manager group. 

If a matching membership is found, the attribute returns Manager; otherwise, it returns Not Manager.  

```
10: IIF EXP:20 CONST:TRUE CONST:FALSE
20:  GTE EXP:30 CONST:1
30:  SUM EXP:40 CONST:1
40:  SELECT REPO:Systems.Security.UserGroups EXP:50
50:  WHERE EXP:60 EXP:80
60:  EQUAL ATTRIB:UserId  EXP:70
70:  GETOBJVALUE INPUT:10 SYS:UserId
80:  EQUAL ATTRIB:GroupId CONST:0284b5d1-904c-4ffd-b5c3-8f22f260f55c
```

**Explanation:**

10 (IIF): If EXP:20 is true → return Manager, else return Not Manager  
20 (GTE): Checks whether EXP:30 ≥ 1  
**This is the “does a membership exist?” test**   
30 (SUM): Sums CONST:1 for every record returned by EXP:40  
**This effectively counts matching records (a “COUNT” implemented via SUM of 1s)**  
40 (SELECT): Queries Systems.Security.UserGroups (user ↔ group memberships)  
50 (WHERE): Filters the memberships by two conditions:  
60: membership user = current user  
80: membership group = the specific group GUID  
70 (SYS UserId): Gets the current logged-in user id  
