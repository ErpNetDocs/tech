# Excise Initial Setup

 

## I.           Prerequisites 

1. The measurement units codes should be defined acording the CL1 nomencature

![img](file:///C:/Users/I6DC4~1.IVA/AppData/Local/Temp/msohtmlclip1/01/clip_image002.jpg)

 

2. The Base measurement unit of products should be same as measurement unit used in article 28 and article 29 from law on excises and tax warehouses

3. It must be defined custom properties with the following codes 

3.1. Products

\-     **Exc_BrandName** - Търговско наименование – Позволени стойности от номенклатура CL175 – Само от позволените стойности

\-     **Exc_Volume** – Вместимост – Десетично число

\-     **Exc_LabelPrice** – Цена по бандерол – Само някой специфични продукти имат такава – Десетично число

3.2. Documents

\-     **Exc_Purpose** – Предназначение – Позволени стойности от номенклатура CL200 – Само от позволените стойности

\-     **Exc_Driver** – Водач – в Стойност се попълва ЕГН, а в Описание – Името на водача на превозното средство

3.3. ExciseAdministrativeDocumentLines

\-     **Exc_Payment** – Плащане - Позволени стойности от номенклатура CL163– Само от позволените стойности

3.4. Parties

\-     **Exc_Country** – Държава – Позволени стойности от номенклатура CL8

\-     **Exc_Region** – Област - Позволени стойности от номенклатура – CL1101

\-     **Exc_Municipality** – Община - Позволени стойности от номенклатура – CL1102

\-     **Exc_City** – Град - Позволени стойности от номенклатура – CL1103

\-     **Exc_District** – Квартал - Позволени стойности от номенклатура – CL1104

\-     **Exc_Street** – Улица / Адрес – Текст

3.5. DocumentTypes

\-     **Exc_DocumentType** – Тип документ – Позволени стойности CL2305

\-     **Exc_OperationType** – Тип на извеждането от акцизен склад – 1021,1029

II.          Other specific nomenclatures

 