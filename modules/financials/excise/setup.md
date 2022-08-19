# Initial Setup


## 1. The measurement units codes should be defined according the CL1 nomenclature

![image-20211209134740745](image-20211209134740745-16390593696201.png)

 

## 2. In the products must be defined Excise Product Type and the measurement unit in the Excise Product Type must be measurement unit used in article 28 and article 29 from law on excises and tax warehouses

## 3. It must be defined custom attributes with the following codes 

### 3.1. Excise Stamp Type

\-     **Exc_BrandName** - Allowed values from CL175 nomencature. Limited to alowed values

\-     **Exc_LabelPrice** – Price on label – Only for specific products – Decimal

### 3.2. Documents

\-      **Exc_Purpose** –  Allowed values from CL200 nomenclature. Limited to alowed values

\-      **Exc_Driver** – In Property Value is filling National number of the vehicle and in Property Decription  – Driver name

\-      **Exc_InputDocumentType** - Value for tag DocumentType in section MeasureValues in the export file

\-      **Exc_InputDocumentNumber** - Value for tag DocumentNumber in section MeasureValues in the export file for eADD

### 3.3. ExciseAdministrativeDocumentLines

\-     **Exc_Payment** – Allowed values from CL163 nomenclature. Limited to alowed values



### 3.4. Parties

\-     **Exc_Country** – Allowed values from CL8 nomenclature

\-     **Exc_Region** – Allowed values from CL1101 nomenclature

\-     **Exc_Municipality** – Allowed values from CL1102 nomenclature

\-     **Exc_City** – Allowed values from CL1103 nomenclature

\-     **Exc_District** – Allowed values from CL1104 nomenclature

\-     **Exc_Street** – Street, Number – Text

### 3.5. DocumentTypes

\-     **Exc_DocumentType** – Allowed values from CL2305 nomenclature

\-     **Exc_OperationType** – Type of output from Tax Warehouse (For example 1021,1029)



## 4. Custom attributes for e-AD

### 4.1.   Parties

**\-**     **Exc_Trader_Excise_Number** - Акцизен номер на търговеца

**\-     Exc_EORI** – EORI номер

**\-     Exc_StreetNumber** – Номер

**\-     Exc_Nad_Lng** – Код на език

**\-     Exc_Tax_Warehouse_Excise_Number** – Акцизен номер на данъчния склад

**\-     Exc_Custom_Office** – Номер на митническо управление

**\-     Exc_Member_State_Code** - Код на държава членка

**\-     Exc_Certificate_Of_Exemption** - Сериен номер на сертификат на освободената организация
     

 

### 4.2.    Documents

**\-     Exc_Commercial_Seal_Identification** - Идентификация на търговската пломба

**\-     Exc_TD_Complementary_Information** - Транспорт допълнителна информация

**\-     Exc_TD_Complementary_Information_LNG** – Транспорт език на допълнителната информация

**\-     Exc_Seal_Information** - Информация за пломбата

**\-     Exc_Seal_Information_LNG** - Език на информацията за пломбата

**\-     Exc_Invoice_Number** – Номер на фактурата

**\-     Exc_Invoice_Date** – Дата на фактурата

**\-     Exc_Origin_Type_Code** - Код на вида на произхода

**\-     Exc_Date_Of_Dispatch** - Дата на изпращане

**\-     Exc_Time_Of_Dispatch** – Час на изпращане

**\-     Exc_Import_SAD_Number** - Номер на митническа декларация за внос

**\-     Exc_Destination_Type_Code** - Код на типа мястото на получаване

**\-     Exc_Journey_Time** - Времетраене на транспорта

**\-     Exc_Transport_Arrangement** - Код на организацията на транспорта

**\-     Exc_TM_Complementary_Information** – Допълнителна информация за тип транспорт

**\-     Exc_TM_Complementary_Information_LNG** - Език на допълнителната информация за тип транспорт

**\-     Exc_Guarantor_Type_Code** - Код на вида на лицето, предоставящо обезпечение

**\-     Exc_EAD_LNG** - Език на e-AD

**\-     Exc_Dispatch_Import_Office** - Код на МУ на внос

**\-     Exc_Certificate_Document_Type** - Сертификат тип на документа

**\-     Exc_Certificate_Document_Reference** - Сертификат номер на документ

**\-     Exc_Certificate_Document_Description** - Сертификат описание на документа

**\-     Exc_Certificate_Reference_Of_Document** - Сертификат референция на документа

**\-     Exc_Tax_Warehouse_Other_Party** - Данъчен склад контрагент

**\-     Exc_Guarantor** - Търговец, предоставящ обезпечението

**\-     Exc_Transport_Arranger** - Търговец Организатор на транспорта
     




### 4.3.    ExciseAdministrativeDocumentLines

**\-     Exc_Gross_Weight** - Брутно тегло

**\-     Exc_Net_Weight**  - Нетно тегло

### 4.4.    ExciseProductType

**\-     Exc_Kind_Of_Packages** - Код на вида опаковка

**\-     Exc_Wine_Product_Category** - Категория на лозаро-винарския продукт

**\-     Exc_Wine_Growing_Zone_Code** - Код на лозарската зона

**\-     Exc_Third_Country_Of_Origin** - Трета държава на произход

**\-     Exc_Wine_Operation_Code** - Код на операция за вино

 

### 4.5. TransportationVehicles

**\-     Exc_Transport_Units_Code** - Код на транспортната единица





 
