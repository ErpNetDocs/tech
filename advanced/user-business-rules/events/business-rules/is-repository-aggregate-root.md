# R30055 Is repository aggregate root

|Code|R30055
|:-------|:------
|**Entity**| UserBusinessRuleEvent
|**Name**| IsRepositoryAggregateRoot
|**Attribute**| EventType 
|**Layer**| Back-End 
|**Events**| COMMIT
|**Priority**|Normal
|**Modify**|NO
|**Applicabale legislation**|ALL // no condition needed
|**Action**|If (EventType == AGGREGATECLIENTCOMMIT), validate that <br> GetAggregateRoot(UserBusinessRule.RepositoryName.Entity) = null
|**Description**|The Aggregate Client Commit is used for triggering user business rules for objects which are an aggregate root, not only when there is a change for the object itself, but also when it is edited by some of its referent objects. For this reason such rules can only be specified for repositories which are aggregate roots. For more information about the Aggregate Client Commit event, see [AGGREGATE CLIENT COMMIT](https://docs.erp.net/tech/advanced/user-business-rules/events/aggregate-client-commit.html).
|**Message**|The *Event Type* field in the event of user business rule with code '{UserBusinessRule.Code}' has an invalid value.<br> Aggregate client commit event type could be used only for repositories that are a root of the aggregate. The aggregate root of the currently specified repository is <br>'{UserBusinessRule.RepositoryName.Entity.AggregateRoot.EntityName}'.
|**Version**|Introduced: in implementation <br> Updated: -
|**Revocable**|NO
