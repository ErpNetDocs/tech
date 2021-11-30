# R30055 Is repository aggregate root

<br>

|Code|R30055
|:-------|:------
|**Entity**| UserBusinessRuleEvent
|**Name**| IsRepositoryAggregateRoot
|**Attribute**| EventType 
|**Layer**| Back-end 
|**Events**| COMMIT
|**Priority**|Normal
|**Modify**|NO
|**Applicabale legislation**|ALL // no condition needed
|**Action**|If EventType == **[AGGREGATECLIENTCOMMIT](https://docs.erp.net/tech/advanced/user-business-rules/events/aggregate-client-commit.html)**, validate that: <br> GetAggregateRoot(UserBusinessRule.RepositoryName.Entity) = **null**
|**Description**|Used for triggering user business rules for objects which are an aggregate root. This happens when there's a change for the object itself and/or when it's edited by some of its referent objects. Such a rule can be specified **only** for repositories which are aggregate roots.
|**Message**|_The Event Type field in the event of user business rule with code '{UserBusinessRule.Code}' has an invalid value. Aggregate client commit event type can be used only for repositories that are a root of the aggregate. The root of the currently specified repository is: <br>'{UserBusinessRule.RepositoryName.Entity.AggregateRoot.EntityName}'._
|**Version**|Introduced: in implementation <br> Updated: -
|**Revocable**|NO
