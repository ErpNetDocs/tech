---
items: UserBusinessRuleExamples
---

# Set DeliveryTerms in purchase invoice

The _DeliveryTerms_ field is of 'enum' type. Here, you can find values of different codes:

|Member name|Value|Description
|:-----|:-----|:-----
|ExWorks|0|ExWorks value. Stored as 'EXW'.
|FrancoCarrier|1|FrancoCarrier value. Stored as 'FCA'.
|FreeAlongsideShip|2|FreeAlongsideShip value. Stored as 'FAS'.
|FreeOnBoard|3|FreeOnBoard value. Stored as 'FOB'.
|CostAndFreightCF|4|CostAndFreightCF value. Stored as 'CFR'.
|CostInsuranceAndFreight|5|CostInsuranceAndFreight value. Stored as 'CIF'.
|CarriagePaidTo|6|CarriagePaidTo value. Stored as 'CPT'.
|CarriageAndInsurancePaidTo|7|CarriageAndInsurancePaidTo value. Stored as 'CIP'.
|DeliveredAtPlace|8|DeliveredAtPlace value. Stored as 'DAP'.
|DeliveredAtTerminal|9|DeliveredAtTerminal value. Stored as 'DAT'.
|DeliveredDutyPaid|10|DeliveredDutyPaid value. Stored as 'DDP'.

If you need to set a value in the _DeliveryTerms_ field of a purchase invoice, the action of the **[user business rule](https://docs.erp.net/tech/advanced/user-business-rules/index.html)** must set a casted value from a **[calculated attribute](https://docs.erp.net/tech/advanced/calculated-attributes/index.html)** in the *DeliveryTermsCode* attribute. The calculated attribute must cast an integer to type **Aloe.@@name.Model.Finance.Intrastat.DeliveryTerms**. 

**Example:** 

To set _DeliveryTermsCode_ on 'FOB' automatically, the user business rule must contain an action:

`1 SETVALUE ATTRIB:DeliveryTermsCode ATTRIB:#CA`

And the #CA should have an integer value casted to **Aloe.@@name.Model.Finance.Intrastat.DeliveryTerms**:

`10 CAST CONST:3 CONST:Aloe.@@name.Model.Finance.Intrastat.DeliveryTerms`

Having this rule set up, when an event happens, it would set the delivery terms of the purchase invoice to 'FOB'.
