# Excise declaration export

The table below lists the sources for the tags of the e-ADD xml file:

|**Excise declaration**|**Source**|
| ------------------------------------------------------------ | ------------------- |
|**Declaration**||
| KindOfDeclaration |EXC00|
| TypeOfDeclaration| EXC002BG |
| IsCorrectionDeclaration|IsCorrectionDeclaration = !(IsNullOrEmptyValue(RefNumberOfCorrectedDeclaration ))|
| RefNumberOfCorrectedDeclaration|RefNumberOfCorrectedDeclaration = /ExcDeclarations.@Exc_RefNumberOfCorrectedDeclaration.Value |
| IsDelayedReporting |IF NOT(IsNullOrEmpty(@Exc_RefNumberOfCorrectedDeclaration)) <br/>THEN {RefNumberOfCorrectedDeclaration = @Exc_RefNumberOfCorrectedDeclaration.Value; IsCorrectionDeclaration = True} <br><br>IF IsNullOrEmpty(@Exc_RefNumberOfCorrectedDeclaration) <br/>THEN  {RefNumberOfCorrectedDeclaration - MISSING; IsCorrectionDeclaration = false}|IF IsNullOrEmpty(@Exc_DelayReferenceNumber ) <br/>THEN (DelayReferenceNumber - MISSING; IsDelayedReporting = false}|
|DelayReferenceNumber| IF NOT(IsNullOrEmpty(@Exc_DelayReferenceNumber)) <br/>THEN {DelayReferenceNumber = @Exc_DelayReferenceNumber.Value; IsDelayedReporting = True} <br><br>IF IsNullOrEmpty(@Exc_DelayReferenceNumber ) <br/>THEN (DelayReferenceNumber - MISSING; IsDelayedReporting = false}|
| PreparationDate | ExciseDeclaration.DocumentDate |
| CustomsOffice | ExciseDeclaration.TaxWarehouse.CustomsOffice|
| TotalAmountOfExciseDuty| SUM ExciseGoods ( If Payment = 10, DutyAmount; If Payment = 40, - DutyAmount; IF Payment<> 10 and 40, 0) |
|                                                                                   ||
|**Customer**||
| LegalEntity | TWH |
| ExciseNumber | ExciseDeclaration.TaxWarehouse.TaxWarehouseExciseNumber  |
| SIC   |MISSING|
| NotificationNumber|MISSING|
|                                                                                    ||
|**Declarer**||
| Name | ExciseDeclaration.ReportingPerson.PartyName.GetLanguageStringOrAny("bg") |
| EGN | ExciseDeclaration.ReportingPerson.NationalNumber |
|                                                                                    ||
|**ReportingPeriod**||
| ReceivingDate|MISSING|
| TaxPeriod| |
| Start|ExciseDeclaration.FromDate |
| End | ExciseDeclaration.ToDate |
|                                                                                    ||
|**AppliedDocuments**||
| AppliedDocument||
| DocumentType |10|
| PurposeOfeAD |MISSING|
| Description | MISSING|
| DocumentNumber| EXC102BG|
| DocumentDate | ExciseDeclaration.ToDate|
|||
| **ExciseGoods**| |
| ExciseGood | |
| BrandName | ExciseDeclarationLine.Product.ExciseProductType.CustomProperties("Exc_BrandName")?.Value |
| Trademark | ExciseDeclarationLine.Product.Name.GetLanguageStringOrAny("bg") |
|  APCode | ExciseDeclarationLine.ExciseProduct?.Code |
| CNCode  | ExciseDeclarationLine.Product.ExciseProductType.CommodityCode.CommodityCodeField |
| Measure |	ExciseDeclarationLine.ExciseQuantityUnit.Name.GetLanguageStringOrAny("bg")|
| AdditionalCode | ExciseDeclarationLine.Product.PartNumber | 
| QuantityOfGoods | ExciseDeclarationLine.ExciseQuantity.Value | 
| IntendedUseOfProduct | ExciseDeclarationLine.Document.CustomProperties("Exc_Purpose")?.Value |
| Purpose | ExciseDeclarationLine.ExcisePurposeCode?.Code |
| DutyAmount | ExciseDeclarationLine.ExciseAmount.Value | 
| Payment | ExciseDeclarationLine.CustomProperties("Exc_Payment")?.Value + "-" + ExciseDeclarationLine.CustomProperties("Exc_Payment")?.Description | 
| PaidDuty | IF(<Payment> in (10,40)) THEN ExciseDeclarationLine.ExciseAmount.Value  ELSE  "0.00" | 
| Pieces | ExciseDeclarationLine.Product.ExciseProductType?.Capacity | 
| NumberOfPackages | ExciseDeclarationLine.Quantity.Value | 
| Degree | ExciseDeclarationLine.ExciseAlcoholicStrength ?? 0 |
| TaxBase | ExciseDeclarationLine.ExciseAmountBase |
| | | 
|**WarehouseStockLog** ||

