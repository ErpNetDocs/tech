# Excise Declaration

The excise declaration is the document that reports a certain period to the customs authorities. 

https://docs.erp.net/model/entities/Finance.Excise.ExciseDeclarations.html

### 1. Entering Excise Declaration

The following basic fields are entered:

**DocumentDate** - Date of declaration preparation.

**DocumentType** - Type of document.

**DocumentNo** - Serial number of the document.

**TaxWarehouse** - Tax warehouse for which the report is made.

**ReportingPerson** - The person submitting the declaration.

**FromDate** - Start date of the period for which the declaration is made.

**ToDate** - End date of the period for which the declaration is made.

### 2. Export of Excise Declaration

The export of the XML file is made from the web panel in the excise document with the following address:

**{$rooturl}/legal/customs/excdecl/{Id}**

Where **/legal** is the relative URL of the Legal BG website.

An active Legal BG website is required to export e-ADD files.

