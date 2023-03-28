# Excise declaration export

The table below lists the sources for the tags of the e-ADD xml file:

|**Excise declaration tags **|**Source**|
| ------------------------------------------------------------ | ------------------- |
|**Declaration**||
| KindOfDeclaration |EXC00|
| TypeOfDeclaration| EXC002BG |
| IsCorrectionDeclaration|IsCorrectionDeclaration = !(IsNullOrEmptyValue(RefNumberOfCorrectedDeclaration ))|
| RefNumberOfCorrectedDeclaration|RefNumberOfCorrectedDeclaration = ExcDeclarations.<span>@ </span>Exc_RefNumberOfCorrectedDeclaration.Value |
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
|**WarehouseStockLog**||
| WarehouseGoods| |
| WarehouseGood| |
| BrandName | Product.<span>@</span>Exc_BrandName.Value |
| TradeName | Product.ProductName |
| CNCode | Product.IntrastatCommodityCode.CommodityCodeField |
| AdditionalCode | Product.PartNumber |
| APCode | ExciseProduct.Code | 
| Degree| **AverageDegree** = (InitialDegree + AverageDegreeInPeriod)/(InitialQuantity + QuantityInPeriod) and InitialDegree = (IF ExciseAdministrativeDocument.Direction =  "R" AND ExciseAdministrativeDocument.DocumentDate < FromDate THEN SUМ(ExciseQuantity\*ExciseAlcoholicStrength)   IF ExciseAdministrativeDocument.Direction =  "I" ExciseAdministrativeDocument.DocumentDate < FromDate THEN SUМ(ExciseQuantity*ExciseAlcoholicStrength)) <br><br> **InitialQuantity** = (IF ExciseAdministrativeDocument.Direction =  "R" AND ExciseAdministrativeDocument.DocumentDate < FromDate THEN SUМ(ExciseQuantity)               IF ExciseAdministrativeDocument.Direction =  "I" ExciseAdministrativeDocument.DocumentDate < FromDate THEN SUМ(ExciseQuantity)) <br><br> **AverageDegreeInPeriod** = IF ExciseAdministrativeDocument.Direction =  "R" AND ExciseAdministrativeDocument.DocumentDate >= FromDate AND ExciseAdministrativeDocument.DocumentDate <= ToDate THEN SUМ(ExciseQuantity\*ExciseAlcoholicStrength)  <br><br> **QuantityInPeriod** = IF ExciseAdministrativeDocument.Direction =  "R" AND ExciseAdministrativeDocument.DocumentDate >= FromDate AND ExciseAdministrativeDocument.DocumentDate <= ToDate THEN SUМ(ExciseQuantity)|
| Pieces| Product.<span>@</span>Exc_Volume | 
| Measure | Product.BaseMeasurementCategory.MeasurementUnits.Code(MeasurementUnits.IsDefaultUnit=True) | 
| InitialAmount | SUM(QuantityBase) WHERE For Each Product <br/> - ExciseAdministrativeDocument.DocumentDate <  ExciseDeclaration.FromDate <br/> - ExciseAdministrativeDocument is Non Voided And Status >= 30 <br/> - If ExciseAdministrativeDocument.Direction = "I" THEN SUM(-QuantityBase)|
| FinalAmount | SUM(ExciseQuantity) WHERE For Each Product <br/> - ExciseAdministrativeDocument.DocumentDate <=  ExciseDeclaration.ToDate <br/> - ExciseAdministrativeDocument is Non Voided And Status >= 30 <br/> - If ExciseAdministrativeDocument.Direction = "I" THEN SUM(-QuantityBase) <br/> -(ExciseAdministrativeDocumentLine.@Exc_EAD_For_Difference <> NULL OR "") AND (ExciseAdministrativeDocumentLine.@Exc_EAD_For_Not_Received <> NULL OR "")|
| IntroducedAmount | SUM(QuantityBase) WHERE For Each Product <br/> - ExciseAdministrativeDocument.DocumentDate >=  ExciseDeclaration.FromDate <br/> - ExciseAdministrativeDocument.DocumentDate <=  ExciseDeclaration.ToDate <br/> - ExciseAdministrativeDocument is Non Voided And Status >= 30 <br/> - ExciseAdministrativeDocument.Direction = "R" |
| RemovedAmount | RemovedAmount = SUM(QuantityBase) WHERE For Each Product <br/> - ExciseAdministrativeDocument.DocumentDate >=  ExciseDeclaration.FromDate <br/> - ExciseAdministrativeDocument.DocumentDate <=  ExciseDeclaration.ToDate <br/> - ExciseAdministrativeDocument.@Exc_Purpose <> 27,90 or 97 (all others except these three) <br/> - ExciseAdministrativeDocument is Non Voided And Status >= 30 <br/> - ExciseAdministrativeDocument.Direction = "I" <br/> -(ExciseAdministrativeDocumentLine.@Exc_EAD_For_Difference <> NULL OR "") AND (ExciseAdministrativeDocumentLine.@Exc_EAD_For_Not_Received <> NULL OR "") |
| TransportationLosses | 0 | 
| StorageLosses | 0 |
| | |
| **StoredGoods** | |
| StoredGood | |
| DeclaredGoodsQuantity | QuantityBase |
| ActualStoredGoods |  QuantityBase |
| DocumentType | ExciseAdministrativeDocument.DocumentType.@Exc_AAD_Type | 
| DocumentNumber | ExciseAdministrativeDocument.DocumentNumber | 
| DocumentDate | If ReferenceDate is not NULL THEN <br/> DocumentDate = ExciseAdministrativeDocument.ReferenceDate ELSE  <br/> DocumentDate = ExciseAdministrativeDocument.DocumentDate|
| ControlPoint | ExciseAdministrativeDocumentLine.MeasuringTransaction?.MeasuringDeviceCode | 
| TransactionNumber | ExciseAdministrativeDocumentLine.MeasuringTransaction?.TransactionNumber|
| RealDateIn | ExciseAdministrativeDocument.DocumentDate |
| GoodsEntryMethod | ExciseAdministrativeDocument.DocumentType.@Exc_EntryMethod |
| GoodProperty | 0 |
