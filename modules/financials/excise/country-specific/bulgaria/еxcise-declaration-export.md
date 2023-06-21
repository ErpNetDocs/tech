# Export of Excise Declaration file

The xml file of Excise Declaration is exported from the Excise declaration.

https://docs.erp.net/model/entities/Finance.Excise.ExciseDeclarations.html

The table below lists the sources for the tags of the Excise declaration xml file:

|**Excise declaration tags**|**Source**|
| ------------------------------------------------------------ | ------------------- |
|**Declaration**||
| KindOfDeclaration |IF (@Exc_KindOfDeclaration != Null, @Exc_KindOfDeclaration, "EXC00")|
| TypeOfDeclaration| IF (@Exc_TypeOfDeclaration != Null, @Exc_TypeOfDeclaration, "EXC002BG") |
| IsCorrectionDeclaration | IF (RefNumberOfCorrectedDeclaration != Null, True, False) |
| RefNumberOfCorrectedDeclaration| @Exc_RefNumberOfCorrectedDeclaration                         |
| IsDelayedReporting | IF(@Exc_DelayReferenceNumber != Null, True, False)           |
|DelayReferenceNumber| @Exc_DelayReferenceNumber |
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
| BrandName | ExciseDeclarationLine.Product.ExciseProductType.<span>@</span>Exc_BrandName.Value |
| Trademark | ExciseDeclarationLine.Product.Name |
|  APCode | ExciseDeclarationLine.ExciseProduct.Code |
| CNCode  | ExciseDeclarationLine.Product.ExciseProductType.CommodityCode.CommodityCodeField |
| Measure |	ExciseDeclarationLine.ExciseQuantityUnit.Name|
| AdditionalCode | If(ExciseDeclarationLine.Product.ProductCodes. ProductCodeField(Where CodingSystem. Name=”ExciseAdditionalCode”) != Null, ExciseDeclarationLine.Product.ProductCodes. ProductCodeField(Where CodingSystem. Name=”ExciseAdditionalCode”) , ExciseDeclarationLine.Product.PartNumber) |
| QuantityOfGoods | ExciseDeclarationLine.ExciseQuantity |
| IntendedUseOfProduct | ExciseDeclarationLine.Document.<span>@</span>Exc_Purpose.Value |
| Purpose | ExciseDeclarationLine.ExcisePurposeCode.Code |
| DutyAmount | ExciseDeclarationLine.ExciseAmount |
| Payment | ExciseDeclarationLine.<span>@</span>Exc_Payment.Value + "-" + ExciseDeclarationLine.<span>@</span>Exc_Payment.Description |
| PaidDuty | IF(PaidDuty = 10 or PaidDuty = 40, ExciseDeclarationLine.ExciseAmount, "0.00") |
| Pieces | ExciseDeclarationLine.Product.ExciseProductType.Capacity |
| NumberOfPackages | ExciseDeclarationLine.Quantity |
| Degree | If (ExciseDeclarationLine.ExciseAlcoholicStrength is not Null, ExciseDeclarationLine.ExciseAlcoholicStrength, 0) |
| TaxBase | ExciseDeclarationLine.ExciseAmountBase |
| | |
|**WarehouseStockLog**||
| WarehouseGoods| |
| WarehouseGood| |
| BrandName | Product.<span>@</span>Exc_BrandName.Value |
| TradeName | Product.ProductName |
| CNCode | Product.IntrastatCommodityCode.CommodityCodeField |
| AdditionalCode | If(ExciseDeclarationLine.Product.ProductCodes. ProductCodeField(Where CodingSystem. Name=”ExciseAdditionalCode”) != Null, ExciseDeclarationLine.Product.ProductCodes. ProductCodeField(Where CodingSystem. Name=”ExciseAdditionalCode”) , ExciseDeclarationLine.Product.PartNumber) |
| APCode | ExciseProduct.Code |
| Degree| **AverageDegree** = If (InitialQuantity + QuantityInPeriod) == 0 Then  ExciseProductType.AlcoholicStrength  Else  (InitialDegree + AverageDegreeInPeriod)/(InitialQuantity + QuantityInPeriod) <BR><BR> **Where** <BR><BR> **InitialDegree** = (IF ExciseAdministrativeDocument.Direction =  "R" AND ExciseAdministrativeDocument.DocumentDate < FromDate THEN SUМ(ExciseQuantity\*ExciseAlcoholicStrength)   IF ExciseAdministrativeDocument.Direction =  "I" ExciseAdministrativeDocument.DocumentDate < FromDate THEN SUМ(ExciseQuantity\*ExciseAlcoholicStrength)) <br><br> **InitialQuantity** = (IF ExciseAdministrativeDocument.Direction =  "R" AND ExciseAdministrativeDocument.DocumentDate < FromDate THEN SUМ(ExciseQuantity)               IF ExciseAdministrativeDocument.Direction =  "I" ExciseAdministrativeDocument.DocumentDate < FromDate THEN SUМ(ExciseQuantity)) <br><br> **AverageDegreeInPeriod** = IF ExciseAdministrativeDocument.Direction =  "R" AND ExciseAdministrativeDocument.DocumentDate >= FromDate AND ExciseAdministrativeDocument.DocumentDate <= ToDate THEN SUМ(ExciseQuantity\*ExciseAlcoholicStrength)  <br><br> **QuantityInPeriod** = IF ExciseAdministrativeDocument.Direction =  "R" AND ExciseAdministrativeDocument.DocumentDate >= FromDate AND ExciseAdministrativeDocument.DocumentDate <= ToDate THEN SUМ(ExciseQuantity)|
| Pieces| IF EXISTS(MeasurementUnit((IsDefaultUnit == True) && (MeasurementCategory == ExciseAdministrativeDocumentLine.Product.BaseMeasurementCategory) && (MeasurementUnitCode == "PCE"))<br/>
THEN    ExciseDeclarations.WarehouseGoods.Pieces = ExciseAdministrativeDocumentLine.Product.ExciseProductTypes.Capacity     and is exported
ELSE   NOT exported|
| Measure | ExciseQuantityUnit.Code |
| InitialAmount | SUM(QuantityBase) WHERE For Each Product <br/> - ExciseAdministrativeDocument.DocumentDate <  ExciseDeclaration.FromDate <br/> - ExciseAdministrativeDocument is Non Voided And Status >= 30 <br/> - If ExciseAdministrativeDocument.Direction = "I" THEN SUM(-QuantityBase)|
| FinalAmount | SUM(ExciseQuantity) WHERE For Each Product <br/> - ExciseAdministrativeDocument.DocumentDate <=  ExciseDeclaration.ToDate <br/> - ExciseAdministrativeDocument is Non Voided And Status >= 30 <br/> - If ExciseAdministrativeDocument.Direction = "I" THEN SUM(-QuantityBase) <br/> -(ExciseAdministrativeDocumentLine.@Exc_EAD_For_Difference <> NULL OR "") AND (ExciseAdministrativeDocumentLine.@Exc_EAD_For_Not_Received <> NULL OR "")|
| IntroducedAmount | SUM(QuantityBase) WHERE For Each Product <br/> - ExciseAdministrativeDocument.DocumentDate >=  ExciseDeclaration.FromDate <br/> - ExciseAdministrativeDocument.DocumentDate <=  ExciseDeclaration.ToDate <br/> - ExciseAdministrativeDocument is Non Voided And Status >= 30 <br/> - ExciseAdministrativeDocument.Direction = "R" |
| RemovedAmount | RemovedAmount = SUM(QuantityBase) WHERE For Each Product <br/> - ExciseAdministrativeDocument.DocumentDate >=  ExciseDeclaration.FromDate <br/> - ExciseAdministrativeDocument.DocumentDate <=  ExciseDeclaration.ToDate <br/> - ExciseAdministrativeDocument.@Exc_Purpose <> 27,90 or 97 (all others except these three) <br/> - ExciseAdministrativeDocument is Non Voided And Status >= 30 <br/> - ExciseAdministrativeDocument.Direction = "I" <br/> -(ExciseAdministrativeDocumentLine.@Exc_EAD_For_Difference <> NULL OR "") AND (ExciseAdministrativeDocumentLine.@Exc_EAD_For_Not_Received <> NULL OR "") |
| TransportationLosses | 0 |
| StorageLosses | 0 |
| | |
| **StoredGoods** | |
| StoredGood | |
| DeclaredGoodsQuantity | ExciseQuantity |
| ActualStoredGoods |  ExciseQuantity |
| DocumentType | ExciseAdministrativeDocument.DocumentType.@Exc_AAD_Type |
| DocumentNumber | If **AdministrativeReferenceCode** is not NULL THEN<br/> <br/> DocumentNumber = ExciseAdministrativeDocument.**AdministrativeReferenceCode**<br/> <br/> ELSE<br/> <br/> DocumentNumber = ExciseAdministrativeDocument.DocumentNumber<br/> |
| DocumentDate | If ReferenceDate is not NULL THEN <br/> DocumentDate = ExciseAdministrativeDocument.ReferenceDate ELSE  <br/> DocumentDate = ExciseAdministrativeDocument.DocumentDate|
| ControlPoint | ExciseAdministrativeDocumentLine.MeasuringTransaction.MeasuringDeviceCode |
| TransactionNumber | ExciseAdministrativeDocumentLine.MeasuringTransaction.TransactionNumber|
| RealDateIn | ExciseAdministrativeDocument.DocumentDate |
| GoodsEntryMethod | ExciseAdministrativeDocument.DocumentType.@Exc_EntryMethod |
| GoodProperty | 0 |
| OwnerShip | Null |
| NumberOfPackages | IF ExciseAdministrativeDocumentLine.Product.BaseMeasurementCategory.DefaultMeasurementUnits.Code = "PCE" THEN  NumberOfPackages = „QuantityBase" <br/> IF Product.BaseMeasurementCategory.DefaultMeasurementUnits.Code <> "PCE", THEN NumberOfPackages = Null |
| | |
| **RemovedGoods** |  |
| RemovedGood | |
| QuantityToRemove | ExciseQuantity |
| DocumentType | ExciseAdministrativeDocument.DocumentType.@Exc_AAD_Type |
| DocumentNumber | ExciseAdministrativeDocument.DocumentNumber |
| DocumentDate | ExciseAdministrativeDocument.DocumentDate |
| ControlPoint | ExciseAdministrativeDocumentLine.MeasuringTransaction.MeasuringDeviceCode |
| TransactionNumber | ExciseAdministrativeDocumentLine.MeasuringTransaction.TransactionNumber |
| ProductPurpose | ExciseAdministrativeDocument.@Exc_Purpose|
| GoodProperty | 0 |
| PaidAkcizQuantity | PaidAkcizQuantity = SUM(ExciseAdministrativeDocumentLines.QuantityToRemove) WHERE  <br/>  ExciseAdministrativeDocumentLines.ExciseAdministrativeDocument.AccrueExciseDuty = True <br/> ExciseAdministrativeDocumentLines.ExciseAdministrativeDocument.Direction = "I"  DetermineLine(ExciseAdministrativeDocumentLines.@Exc_EAD_For_Not_Received) = Current(ExciseAdministrativeDocumentLine)|
| OwnerShip | Null |
| DocumentReturnDate | Null |
| Difference | Difference = SUM(ExciseAdministrativeDocumentLines.QuantityToRemove) WHERE <br/>   ExciseAdministrativeDocumentLines.ExciseAdministrativeDocument.AccrueExciseDuty= True <br/> ExciseAdministrativeDocumentLines.ExciseAdministrativeDocument.Direction = "I" <br/> DetermineLine(ExciseAdministrativeDocumentLines.@Exc_EAD_For_Difference) = Current(ExciseAdministrativeDocumentLine) |
| ADDNoForDifference | ADDNoForDifference = FIRST(ExciseAdministrativeDocumentLines.ExciseAdministrativeDocument.DocumentNumber) WHERE <br/> ExciseAdministrativeDocumentLines.ExciseAdministrativeDocument.AccrueExciseDuty = True <br/> ExciseAdministrativeDocumentLines.ExciseAdministrativeDocument.Direction = "I" <br/> DetermineLine(ExciseAdministrativeDocumentLines.@Exc_EAD_For_Difference) = Current(ExciseAdministrativeDocumentLine)|
| ADDDateForDifference | ADDDateForDifference = FIRST(ExciseAdministrativeDocumentLines.ExciseAdministrativeDocument.DocumentDate) WHERE <br/> ExciseAdministrativeDocumentLines.ExciseAdministrativeDocument.AccrueExciseDuty = True <br/> ExciseAdministrativeDocumentLines.ExciseAdministrativeDocument.Direction = "I" <br/> DetermineLine(ExciseAdministrativeDocumentLines.@Exc_EAD_For_Difference) = Current(ExciseAdministrativeDocumentLine)|
| PaidAkcizDocument | PaidAkcizDocument = FIRST(ExciseAdministrativeDocumentLines.ExciseAdministrativeDocument.DocumentNumber) WHERE <br/> ExciseAdministrativeDocumentLines.ExciseAdministrativeDocument.AccrueExciseDuty = True <br/>  ExciseAdministrativeDocumentLines.ExciseAdministrativeDocument.Direction = "I" <br/> DetermineLine(ExciseAdministrativeDocumentLines.@Exc_EAD_For_Not_Received) = Current(ExciseAdministrativeDocumentLine) |
| PaidAkcizDocDate | PaidAkcizDocDate = FIRST(ExciseAdministrativeDocumentLines.ExciseAdministrativeDocument.DocumentDate) WHERE <br/>          ExciseAdministrativeDocumentLines.ExciseAdministrativeDocument.AccrueExciseDuty = True <br/>  ExciseAdministrativeDocumentLines.ExciseAdministrativeDocument.Direction = "I" <br/> DetermineLine(ExciseAdministrativeDocumentLines.@Exc_EAD_For_Not_Received) = Current(ExciseAdministrativeDocumentLine) |
| NumberOfPackages | IF ExciseAdministrativeDocumentLine.Product.BaseMeasurementCategory.DefaultMeasurementUnits.Code = "PCE" THEN  NumberOfPackages = „QuantityBase" <br/> IF Product.BaseMeasurementCategory.DefaultMeasurementUnits.Code <> "PCE", THEN NumberOfPackages = Null|
| DocumentNumberForReducedRate | Null |
| | |
| **ExciseLabels**||
| ExciseLabel | |
| LabelType | ExciseStampOperationLines.ExciseStampType.Category |
| CNCode | ExciseStampOperationLines.ExciseProductType.CommodityCode.CommodityCodeField |
| APCode | ExciseStampOperationLines.ExciseProductType.ExciseProduct.Code |
| TradeName | ExciseStampOperationLines.ExciseProductType.@Exc_BrandName |
| MeasureUnit | ExciseStampOperationLines.ExciseProductType.MeasurementUnit |
| Capacity | ExciseStampOperationLines.ExciseProductType.Capacity |
| AlcoholicStrength | ExciseStampOperationLines.ExciseProductType.AlcoholicStrength |
| AvailableNotGluedBeginningCount | Box1_Availabulity_Begin = SUM(ExciseStampOperationLines.Quantity if  ExciseStampOperation.ExciseStampOperationType.Box1Effect = 'Plus' And  ExciseStampOperation.DocumentDate < ExciseDeclarations.FromDate And ExciseStampOperation.State >=30 And ExciseStampOperation.Void = False + ExciseStampOperationLines.Quantity*(-1) if ExciseStampOperation.ExciseStampOperationType.Box1Effect = 'Minus' And  ExciseStampOperation.DocumentDate < ExciseDeclarations.FromDate And ExciseStampOperation.State >=30 And ExciseStampOperation.Void = False)|
| AvailableNotGluedEndCount | Box1_Availabulity_End = SUM(ExciseStampOperationLines.Quantity if  ExciseStampOperation.ExciseStampOperationType.Box1Effect = 'Plus' And  ExciseStampOperation.DocumentDate <= ExciseDeclarations.ToDate And ExciseStampOperation.State >=30 And ExciseStampOperation.Void = False + ExciseStampOperationLines.Quantity*(-1) if ExciseStampOperation.ExciseStampOperationType.Box1Effect = 'Minus' And  ExciseStampOperation.DocumentDate <= ExciseDeclarations.ToDate And ExciseStampOperation.State >=30 And ExciseStampOperation.Void = False) |
| AvailableGluedBeginningCount | Box2_Availabulity_Begin = SUM(ExciseStampOperationLines.Quantity if  ExciseStampOperation.ExciseStampOperationType.Box2Effect = 'Plus' And  ExciseStampOperation.DocumentDate < ExciseDeclarations.FromDate And ExciseStampOperation.State >=30 And ExciseStampOperation.Void = False + ExciseStampOperationLines.Quantity*(-1) if ExciseStampOperation.ExciseStampOperationType.Box2Effect = 'Minus' And  ExciseStampOperation.DocumentDate < ExciseDeclarations.FromDate And ExciseStampOperation.State >=30 And ExciseStampOperation.Void = False)|
| AvailableGluedEndCount | Box2_Availabulity_End = SUM(ExciseStampOperationLines.Quantity if  ExciseStampOperation.ExciseStampOperationType.Box2Effect = 'Plus' And  ExciseStampOperation.DocumentDate <= ExciseDeclarations.ToDate And ExciseStampOperation.State >=30 And ExciseStampOperation.Void = False + ExciseStampOperationLines.Quantity*(-1) if ExciseStampOperation.ExciseStampOperationType.Box2Effect = 'Minus' And  ExciseStampOperation.DocumentDate <= ExciseDeclarations.ToDate And ExciseStampOperation.State >=30 And ExciseStampOperation.Void = False) |
| AvailableOutsideCountryBeginningCount | Box3_Availabulity_Begin = SUM(ExciseStampOperationLines.Quantity if  ExciseStampOperation.ExciseStampOperationType.Box3Effect = 'Plus' And  ExciseStampOperation.DocumentDate < ExciseDeclarations.FromDate And ExciseStampOperation.State >=30 And ExciseStampOperation.Void = False + ExciseStampOperationLines.Quantity*(-1) if ExciseStampOperation.ExciseStampOperationType.Box3Effect = 'Minus' And  ExciseStampOperation.DocumentDate < ExciseDeclarations.FromDate And ExciseStampOperation.State >=30 And ExciseStampOperation.Void = False) |
| AvailableOutsideCountryEndCount | Box3_Availabulity_End = SUM(ExciseStampOperationLines.Quantity if  ExciseStampOperation.ExciseStampOperationType.Box3Effect = 'Plus' And  ExciseStampOperation.DocumentDate <= ExciseDeclarations.ToDate And ExciseStampOperation.State >=30 And ExciseStampOperation.Void = False + ExciseStampOperationLines.Quantity*(-1) if ExciseStampOperation.ExciseStampOperationType.Box3Effect = 'Minus' And  ExciseStampOperation.DocumentDate <= ExciseDeclarations.ToDate And ExciseStampOperation.State >=30 And ExciseStampOperation.Void = False) |
| | |



The symbol "." is used to indicate that a field or data type is being referenced.

The symbol "@xxxx" is used to indicate a custom property with the code "xxxx". If no field reference is specified after it, the custom property's value is used.

The symbol "*" denotes multiplication.

The symbol "<>" means different from.

The " <=" symbol means less than or equal to.

The " >=" symbol means greater than or equal to.
