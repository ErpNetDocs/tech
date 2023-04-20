# Initial Setup

## 1. System attributes

### 1.1. Measurement units

The measurement units codes of Excise Measurement Unit in Excise Product Type should be defined according the CL1 nomenclature.

Base Measurement Unit could be any. 

### 1.2. Excise Product Type

In the products must be defined Excise Product Type and the measurement unit in the Excise Product Type must be measurement unit used in article 28 and article 29 from law on excises and tax warehouses

### 1.3. Code system ”ExciseAdditionalCode”

It is used for Additional code.

## 3. Custom properties

It must be defined custom attributes with the following codes 

### 3.1. ExciseProductType

- **Exc_BrandName** - Allowed values from CL175 nomenclature. Limited to allowed values

- **Exc_LabelPrice** – Price on label – Only for specific products – Decimal

### 3.2. Documents

- **Exc_Purpose** - Allowed values from the CL200 nomenclature. Limited to allowed values. Used in the Excise Document. Mandatory.

- **Exc_Driver** - In the Property Value field, the national number of the vehicle is entered, and in the Property Description field, the name of the driver is entered. Used in the Excise Document. Mandatory.

- **Exc_InputDocumentType** - The value for the DocumentType tag in the MeasureValues section of the export file. Conditional.

- **Exc_InputDocumentNumber** - The value for the DocumentNumber tag in the MeasureValues section of the export file for eADD. Conditional.

- **Exc_RefNumberOfCorrectedDeclaration** - The number of the corrected declaration. Used in the Excise Declaration. Not mandatory.

- **Exc_DelayReferenceNumber** - The number of the resolution for delay. Used in the Excise Declaration. Not mandatory. 

  

### 3.3. ExciseAdministrativeDocumentLines

- **Exc_Payment** - Allowed values are from the CL163 nomenclature and are limited to the allowed values. Mandatory field.
- **Exc_InputDocumentTypeLine** - Type of the input document. Value for tag DocumentType in section MeasureValues in the export file. If empty, Exc_InputDocumentType from the header of the excise document is used. Conditional field.
- **Exc_InputDocumentNumberLine** - Number of the input document. Value for tag DocumentNumber in section MeasureValues in the export file for eADD. If empty, Exc_InputDocumentNumber from the header of the excise document is used. Conditional field.

The following two characteristics:

- **Exc_EAD_For_Difference** - Number of e-AD for differences. Conditional field.
- **Exc_EAD_For_Not_Received** - Number of e-AD for not received. Conditional field.

are used to fill in the following tags from the RemovedGood section of the Excise Declaration:

​		Difference

​		ADDNoForDifference

​		ADDDateForDifference

​		PaidAkcizDocument

​		PaidAkcizDocDate

​		PaidAkcizQuantity

The purpose is to indicate in the current e-ADD for differences or not received for which e-ADDs it is issued.

### 3.4. Parties

- **Exc_Country** – Allowed values from CL8 nomenclature
- **Exc_Region** – Allowed values from CL1101 nomenclature
- **Exc_Municipality** – Allowed values from CL1102 nomenclature
- **Exc_City** – Allowed values from CL1103 nomenclature
- **Exc_District** – Allowed values from CL1104 nomenclature
- **Exc_Street** – Street, Number – Text

### 3.5. DocumentTypes

- **Exc_AAD_Type** - За тага DocumentType в ***** RemovedGood и ***** StoredGood в WarehouseStockLog. Номенклатура CL164.

- **Exc_EntryMethod** - За тага GoodsEntryMethod в ***** StoredGood в WarehouseStockLog. Номенклатура CL165.



## 4. Custom attributes for e-AD

### 4.1.   Parties

- **Exc_Trader_Excise_Number** - Excise number of the trader
- **Exc_EORI** - EORI number
- **Exc_StreetNumber** - Number
- **Exc_Nad_Lng** - Language code
- **Exc_Tax_Warehouse_Excise_Number** - Excise number of the tax warehouse
- **Exc_Custom_Office** - Number of the customs office
- **Exc_Member_State_Code** - Code of the member state
- **Exc_Certificate_Of_Exemption** - Serial number of the certificate of exemption for the organization     

### 4.2.    Documents

- **Exc_Commercial_Seal_Identification** - Identification of commercial seal
- **Exc_TD_Complementary_Information** - Transport complementary information
- **Exc_TD_Complementary_Information_LNG** - Language of transport complementary information
- **Exc_Seal_Information** - Seal information
- **Exc_Seal_Information_LNG** - Language of seal information
- **Exc_Invoice_Number** - Invoice number
- **Exc_Invoice_Date** - Invoice date
- **Exc_Origin_Type_Code** - Code of origin type
- **Exc_Date_Of_Dispatch** - Date of dispatch
- **Exc_Time_Of_Dispatch** - Time of dispatch
- **Exc_Import_SAD_Number** - Customs declaration number for import
- **Exc_Destination_Type_Code** - Code of destination type
- **Exc_Journey_Time** - Duration of transport
- **Exc_Transport_Arrangement** - Code of transport arrangement organization
- **Exc_TM_Complementary_Information** - Transport type complementary information
- **Exc_TM_Complementary_Information_LNG** - Language of transport type complementary information
- **Exc_Guarantor_Type_Code** - Code of the type of guarantor
- **Exc_EAD_LNG** - Language of e-AD
- **Exc_Dispatch_Import_Office** - Code of import customs office
- **Exc_Certificate_Document_Type** - Certificate document type
- **Exc_Certificate_Document_Reference** - Certificate document number
- **Exc_Certificate_Document_Description** - Certificate document description
- **Exc_Certificate_Reference_Of_Document** - Certificate reference of document
- **Exc_Tax_Warehouse_Other_Party** - Tax warehouse counterparty
- **Exc_Guarantor** - Merchant providing the guarantee
- **Exc_Transport_Arranger** - Merchant Transport Organizer

​     




### 4.3.    ExciseAdministrativeDocumentLines

- **Exc_Gross_Weight** - Gross weight
- **Exc_Net_Weight** - Net weight

### 4.4.    ExciseProductType

- **Exc_Kind_Of_Packages** - Code of the kind of packaging
- **Exc_Wine_Product_Category** - Category of wine product
- **Exc_Wine_Growing_Zone_Code** - Code of the wine-growing zone
- **Exc_Third_Country_Of_Origin** - Third country of origin
- **Exc_Wine_Operation_Code** - Code of wine operation.

 

### 4.5. TransportationVehicles

- **Exc_Transport_Units_Code** - Transport unit code





 
