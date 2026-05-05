---
items: UserBusinessRuleExamples
---

# How to auto-create and release a sales order when an offer is released?

Releasing an offer typically marks customer acceptance - the negotiated terms become firm, and the natural next step is to start fulfilling the deal as a sales order. Automating this transition removes a manual conversion step, guarantees that the sales order inherits the exact header from the accepted offer (customer, company, currency, salesperson, document type), and keeps the two documents traceably linked through the `Parent` relationship.

This example shows how to automatically create a sales order from an offer at the moment the offer is released, and have that sales order auto-released as well.

The pattern uses two cooperating user business rules - one creates the sales order, the other releases it.

> [!IMPORTANT]
>
> **COMMITTED is the only event in which the newly created document is actually persisted in the database.**
> All earlier events (`CREATENEW`, `COMMIT`, `STATECHANGED`, ...) operate on in-memory state only.
> Since `ChangeState` runs in a **separate transaction**, it requires the document to already exist in the database - which makes COMMITTED the only viable event for the auto-release.
>
> Note that `ObjectState` does not change at commit. A row inserted by the just-committed transaction stays at `ObjectState == 'Added'` while being fully persisted. That combination - *persisted, yet still `Added`* - is the marker the second rule uses to recognize the freshly inserted document.

For the example, the source entity is [Offers](https://docs.erp.net/model/entities/Crm.Presales.Offers.html) and the target entity is [SalesOrders](https://docs.erp.net/model/entities/Crm.Sales.SalesOrders.html).

## First user business rule - create the sales order on STATECHANGED

|Repository|
|:----|
|Crm.Presales.Offers|

|Events|
|:----|

|Event type|Event parameter|Execution priority|
|:----|:----|:----|
|STATECHANGED|RELEASED|Normal|

- **Script Language:** JavaScript
- **Script Text:**

    ```javascript
    var newOrder = Domain.Crm.Sales.SalesOrdersRepository.createNew();
    newOrder.DocumentType = subject.DocumentType;
    newOrder.EnterpriseCompany = subject.EnterpriseCompany;
    newOrder.EnterpriseCompanyLocation = subject.EnterpriseCompanyLocation;
    newOrder.DocumentCurrency = subject.DocumentCurrency;
    newOrder.Customer = subject.Customer;
    newOrder.SalesPerson = subject.SalesPerson;
    newOrder.Parent = subject;
    // ... more props 
    // loop and create the document lines based on your business requirements
    ```

`newOrder.Parent = subject` links the new sales order back to the offer that triggered its creation.

## Second user business rule - release the sales order on COMMITTED

|Repository|
|:----|
|Crm.Sales.SalesOrders|

|Events|
|:----|

|Event type|Event parameter|Execution priority|
|:----|:----|:----|
|COMMITTED| |Normal|

- **Script Language:** JavaScript
- **Script Text:**

    ```javascript
    if (subject.State == 'New' &&
        subject.ObjectState == 'Added' &&
        subject.Parent && 
        subject.Parent.DocumentType.Id == "SPECIFIC-OFFER-TYPE-ID-HERE") {
        subject.ChangeState('Released');
    }
    ```

The conditions, taken together, ensure the rule fires only on sales orders just inserted by the offer-release flow:

- `ObjectState == 'Added'` - the order was inserted by the just-committed transaction.
- `State == 'New'` - the order has not been released yet.
- `Parent && Parent.DocumentType.Id == "..."` - the order originates from an offer of the specific document type.

-------------

## See more

- **[User business rules](../index.md)**
- **[Scripting in user business rules](../scripting/index.md)**
- **[STATECHANGED event](../events/statechanged.md)**
- **[Document states](../../../concepts/documents/states.md)**
