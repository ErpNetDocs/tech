# How to set DeliveryTerms in Purchase invoice?

The DeliveryTerms is enum type so it is accessed specifically. The values of the codes are as follows:

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


If there is a need to set a value in the purchase invoice in the DeliveryTerms field, the action of the user business rule must set a casted value from a calculated attribute in the DeliveryTermsCode attribute. The calculated attribute must cast an integer to type <br>
'Aloe.@@name.Model.Finance.Intrastat.DeliveryTerms'. For example - if the user wants to set SeliveryTermsCode on 'FOB' automatically, the user business rule must contain an action:

1 SETVALUE ATTRIB:DeliveryTermsCode ATTRIB:#CA

And the #CA should have an integer value, casted to 'Aloe.@@name.Model.Finance.Intrastat.DeliveryTerms', for example:

10 CAST CONST:3 CONST:Aloe.@@name.Model.Finance.Intrastat.DeliveryTerms

Having this business rule set up, when the event happens, it would set the Delivery Terms of the Purchase invoice to 'FOB'.
