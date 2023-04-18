# Excise Administrative Document



The Excise Administrative Document or Excise Document is the primary document that describes the movement of excise goods in the tax warehouse for reporting purposes to the customs authorities.

It describes the receipts and issues in the tax warehouse, movements within the tax warehouse, as well as the calculation of the excise duty that needs to be paid to the customs authorities. It is also the basis for generating the necessary data for reporting purposes and for preparing the excise declaration for the period.



The following data are filled in the header:

[Administrative ReferenceCode](https://docs.erp.net/model/entities/Finance.Excise.ExciseAdministrativeDocuments.html#administrativereferencecode) - The reference code, returned the customs authorities, when the document  is exported to them or reference code in received documents.

[TaxWarehouse](https://docs.erp.net/model/entities/Finance.Excise.ExciseAdministrativeDocuments.html#taxwarehouse) - Our licensed tax warehouse for which we report to the customs authorities.

[Direction](https://docs.erp.net/model/entities/Finance.Excise.ExciseAdministrativeDocuments.html#direction) - The direction of the movement of goods. It determines whether the goods are entering or leaving the tax warehouse.

[AccrueExciseDuty](https://docs.erp.net/model/entities/Finance.Excise.ExciseAdministrativeDocuments.html#accrueexciseduty) - A checkbox that indicates that excise duty is accrued when the goods are removed from the tax warehouse.

[ReferenceDate](https://docs.erp.net/model/entities/Finance.Excise.ExciseAdministrativeDocuments.html#referencedate) - The date of the reference document when it is issued by an external organization. It is used mainly when receiving goods into the tax warehouse.

[ReferenceDocumentNo](https://docs.erp.net/model/entities/Finance.Excise.ExciseAdministrativeDocuments.html#referencedocumentno) - The number of the reference document when it is issued by an external organization. It is used mainly when receiving goods into the tax warehouse.

[IsDeferredSubmission](https://docs.erp.net/model/entities/Finance.Excise.ExciseAdministrativeDocuments.html#isdeferredsubmission) - Indicates whether the movement has begun under the cover of a paper administrative document.

[OtherParty](https://docs.erp.net/model/entities/Finance.Excise.ExciseAdministrativeDocuments.html#otherparty) - The other party, sending or receiving the goods. 

[DeliveryParty](https://docs.erp.net/model/entities/Finance.Excise.ExciseAdministrativeDocuments.html#deliveryparty) - Indicates the party where the goods are send/received. null means it is the same as Other Party. 

[TransportationCarrier](https://docs.erp.net/model/entities/Finance.Excise.ExciseAdministrativeDocuments.html#transportationcarrier) - The carrier used for the transportation of the goods. 

[TransportationVehicle](https://docs.erp.net/model/entities/Finance.Excise.ExciseAdministrativeDocuments.html#transportationvehicle) - The vehicle, used for the transportation of the goods. 

[ReportingPerson](https://docs.erp.net/model/entities/Finance.Excise.ExciseAdministrativeDocuments.html#reportingperson) - This is the person submitting the declaration. 



https://docs.erp.net/model/entities/Finance.Excise.ExciseAdministrativeDocuments.html





The following data is filled in the rows:

[Product](https://docs.erp.net/model/entities/Finance.Excise.ExciseAdministrativeDocumentLines.html#product) - The product that is input or output from the excise warehouse.

[Lot](https://docs.erp.net/model/entities/Finance.Excise.ExciseAdministrativeDocumentLines.html#lot) - The stock batch with which the corresponding product is booked in or out. It is copied from the parent stock receipt and is used to trace the movement in the warehouse - which batch was involved in which receipt and issue documents.

[Quantity](https://docs.erp.net/model/entities/Finance.Excise.ExciseAdministrativeDocumentLines.html#quantity) - Quantity in the unit of measure of the stock transaction in the Warehouse Management module.

[QuantityUnit](https://docs.erp.net/model/entities/Finance.Excise.ExciseAdministrativeDocumentLines.html#quantityunit) - Unit of measure of the stock transaction from the Warehouse Management module.

[QuantityBase](https://docs.erp.net/model/entities/Finance.Excise.ExciseAdministrativeDocumentLines.html#quantitybase) - Quantity in the base unit of measure of the product. The inventory is managed in the base unit of measure in the Warehouse Management module.

[ExciseQuantity](https://docs.erp.net/model/entities/Finance.Excise.ExciseAdministrativeDocumentLines.html#excisequantity) - Quantity in the Excise unit of measure.

[ExciseQuantityUnit](https://docs.erp.net/model/entities/Finance.Excise.ExciseAdministrativeDocumentLines.html#excisequantityunit) - Excise unit of measure. The record-keeping to the customs authorities is in this unit of measure. It is specified in the Excise Product Types, which is set in the product definition.

[MeasuringTransaction](https://docs.erp.net/model/entities/Finance.Excise.ExciseAdministrativeDocumentLines.html#measuringtransaction) - Transaction of product input or output, measured with specialized measuring device for excise purposes.

[ExciseProduct](https://docs.erp.net/model/entities/Finance.Excise.ExciseAdministrativeDocumentLines.html#exciseproduct) - The Excise product code defined by the taxation and customs authorities. It is specified in the Excise Product Types, which is set in the product definition. It is loaded automatically upon product selection, but can be changed manually.

[ExcisePurposeCode](https://docs.erp.net/model/entities/Finance.Excise.ExciseAdministrativeDocumentLines.html#excisepurposecode) - The Purpose codes specify the different purposes recognized by the authorities for determining the excise rate.

[ExciseAlcoholicStrength](https://docs.erp.net/model/entities/Finance.Excise.ExciseAdministrativeDocumentLines.html#excisealcoholicstrength) - The alcoholic strength, which will be used for Excise reporting purposes. If a Measuring Transaction is specified, it is taken automatically from it upon product selection. If not, it is taken from the Excise Product Types, which is set in the product definition. It can be changed manually.

[ExciseAmountBase](https://docs.erp.net/model/entities/Finance.Excise.ExciseAdministrativeDocumentLines.html#exciseamountbase) - The base on which the excise rate is calculated. It is automatically calculated using an algorithm defined in [Excise Product Categories](https://docs.erp.net/model/entities/Finance.Excise.ExciseProductCategories.html). Excise Product Categories are part of the definition of ExciseProduct.

[ExciseDutyRate](https://docs.erp.net/model/entities/Finance.Excise.ExciseAdministrativeDocumentLines.html#excisedutyrate) - A reference to the specific rate in the table [ExciseDutyRates](https://docs.erp.net/model/entities/Finance.Excise.ExciseDutyRates.html), which is determined based on the selected Excise Products, Excise Purpose Codes, and Excise Measurement Units.

[ExciseDutyRateValue](https://docs.erp.net/model/entities/Finance.Excise.ExciseAdministrativeDocumentLines.html#excisedutyratevalue) - The value of the determined excise rate [ExciseDutyRate](https://docs.erp.net/model/entities/Finance.Excise.ExciseAdministrativeDocumentLines.html#excisedutyratevalue).

[ExciseAmount](https://docs.erp.net/model/entities/Finance.Excise.ExciseAdministrativeDocumentLines.html#exciseamount) - The calculated amount of excise based on ExciseAmountBase and ExciseDutyRateValue.



https://docs.erp.net/model/entities/Finance.Excise.ExciseAdministrativeDocumentLines.html















