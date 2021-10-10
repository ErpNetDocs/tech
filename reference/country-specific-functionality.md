---
uid: applicable-legislations
---

# Country specific functionality



@@name contains some country, region, or other specific functionalities that are needed in order to meet legal or regulatory requirements. Such functionality is the creation of VAT returns and the VAT export files for submission to the National Revenue Agency (Bulgaria), for example.

## Party applicable legislations 

In Parties, there is a child table with the Applicable legislations for the particular Party. The table contains information about the countries, states, unions, or other entities whose regulations apply to the Party. The records in this table are used when determining if a business rule must be activated when, for example, it incorporates rules that are specific for the particular country's laws.

### Bulgaria (BG)

#### List of the System deal types and their correlation with the Sales and Purchases ledger's columns

The VAT declaration in @@name  is a document that serves as a basis for the creation of a VAT return and the VAT export files for submission to the National Revenue Agency. The information in the VAT declaration is based on the VAT Entries created in the system for the particular period.

The Entries amounts (Amount Base and VAT Amount Base) are entered in different columns of the Sales and Purchases ledger of the VAT declaration depending on their Deal type (for more information about Entries' deal type and amount calculation, see todo: (Defining VAT and base for VAT Entries)).

This article contains information about the correlation between the system Deal types and the columns of the Sales and Purchases ledgers according to which the Entries amounts are distributed to those columns.

**Sales Ledger**

| Column        | Column Name (EN)                                | Column Name (BG)                                             | Deal Type (BG)                                               | Additional Conditions    |
| ------------- | ----------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------ |
| Column9_Data  | Total Base Amount                               | Общ размер на данъчните основи                               | ВОД                                                          | -                        |
| Column9_Data  | Total Base Amount                               | Общ размер на данъчните основи                               | Доставка по чл. 163а от ЗДДС част I (отпадъци) на Приложение 2 | -                        |
| Column9_Data  | Total Base Amount                               | Общ размер на данъчните основи                               | Доставка по чл. 163а от ЗДДС част II (земеделска продукция) на Приложение 2 | -                        |
| Column9_Data  | Total Base Amount                               | Общ размер на данъчните основи                               | Доставка по чл.140,146,173(1) или 173(4)                     | -                        |
| Column9_Data  | Total Base Amount                               | Общ размер на данъчните основи                               | Износ по глава трета от ЗДДС                                 | -                        |
| Column9_Data  | Total Base Amount                               | Общ размер на данъчните основи                               | Начисляване на ДДС в др. случаи                              | Apply_Date >= '20160201' |
| Column9_Data  | Total Base Amount                               | Общ размер на данъчните основи                               | Облагаеми доставки 7/9%                                      | -                        |
| Column9_Data  | Total Base Amount                               | Общ размер на данъчните основи                               | Облагаеми сделки                                             | -                        |
| Column9_Data  | Total Base Amount                               | Общ размер на данъчните основи                               | Самоначисляване на ДДС по чл.82,ал.2-5                       | -                        |
| Column9_Data  | Total Base Amount                               | Общ размер на данъчните основи                               | Самоначисляване на ДДС при ВОП                               | -                        |
| Column10_Data | Total VAT Amount                                | Всичко начислен ДДС                                          | Начислен ДДС при ползване за лични нужди                     | Apply_Date >= '20160201' |
| Column10_Data | Total VAT Amount                                | Всичко начислен ДДС                                          | Начисляване на ДДС в др. случаи                              | -                        |
| Column10_Data | Total VAT Amount                                | Всичко начислен ДДС                                          | Облагаеми доставки 7/9%                                      | -                        |
| Column10_Data | Total VAT Amount                                | Всичко начислен ДДС                                          | Облагаеми сделки                                             | -                        |
| Column10_Data | Total VAT Amount                                | Всичко начислен ДДС                                          | Самоначисляване на ДДС по чл.82,ал.2-5                       | -                        |
| Column10_Data | Total VAT Amount                                | Всичко начислен ДДС                                          | Самоначисляване на ДДС при ВОП                               | -                        |
| Column11_Data | Base Amount 20 Percent                          | Данъчна основа 20%                                           | Доставка по чл. 163а от ЗДДС част I (отпадъци) на Приложение 2 | -                        |
| Column11_Data | Base Amount 20 Percent                          | Данъчна основа 20%                                           | Доставка по чл. 163а от ЗДДС част II (земеделска продукция) на Приложение 2 | -                        |
| Column11_Data | Base Amount 20 Percent                          | Данъчна основа 20%                                           | Начисляване на ДДС в др. случаи                              | Apply_Date >= '20160201' |
| Column11_Data | Base Amount 20 Percent                          | Данъчна основа 20%                                           | Облагаеми сделки                                             | -                        |
| Column12_Data | VAT Amount 20 Percent                           | Начислен ДДС 20%                                             | Начисляване на ДДС в др. случаи                              | Apply_Date >= '20160201' |
| Column12_Data | VAT Amount 20 Percent                           | Начислен ДДС 20%                                             | Облагаеми сделки                                             | -                        |
| Column13_Data | Base Amount EUPurchase                          | Данъчна основа на ВОП                                        | Самоначисляване на ДДС при ВОП                               | -                        |
| Column14_Data | Base Amount VATL Article 82                     | Данъчна основа на доставките по чл.82, ал. 2 - 5             | Самоначисляване на ДДС по чл.82,ал.2-5                       | -                        |
| Column15_Data | VAT Amount EUPurchase VATL Article 82           | Начислен ДДС за ВОП и доставките по чл.82, ал. 2 - 5         | Самоначисляване на ДДС по чл.82,ал.2-5                       | -                        |
| Column15_Data | VAT Amount EUPurchase VATL Article 83           | Начислен ДДС за ВОП и доставките по чл.82, ал. 2 - 5         | Самоначисляване на ДДС при ВОП                               | -                        |
| Column16_Data | VAT amout in case of personal use               | Начислен данък при ползване за лични нужди                   | Начислен ДДС при ползване за лични нужди                     | Apply_Date >= '20160201' |
| Column16_Data | VAT amout in case of personal use               | Начислен данък при ползване за лични нужди                   | Начисляване на ДДС в др. случаи                              | Apply_Date < '20160201'  |
| Column17_Data | Base Amount 9 %                                 | Данъчна основа 9 %                                           | Облагаеми доставки 7/9%                                      | -                        |
| Column18_Data | VAT Amount 9 %                                  | Начислен ДДС 9 %                                             | Облагаеми доставки 7/9%                                      | -                        |
| Column19_Data | Base Amount 0 Percent VATL Chapter 3            | Данъчна основа 0 % по глава трета от ЗДДС                    | Износ по глава трета от ЗДДС                                 | -                        |
| Column20_Data | Base Amount 0 Percent EUSale                    | Данъчна основа 0 % на ВОД                                    | ВОД                                                          | -                        |
| Column21_Data | Base Amount 0 Percent VATL Articles 140 146 173 | Данъчна основа 0 % по чл. 140, чл. 146 ал. 1 и чл. 173, ал. 1 и 4 | Доставка по чл.140,146,173(1) или 173(4)                     | -                        |
| Column22_Data | Base Amount Service Sales VATL Article 21       | Данъчна основа на услугите по чл. 21, ал. 2                  | Доставка по чл.21(2) в друга държава членка                  | -                        |
| Column23_Data | Base Amount VATL Article 69                     | Данъчна основа почл. 69, ал. 2                               | Доставка по чл.69(2) и дистанц. продажба към др.членка       | -                        |
| Column24_Data | Base Amount Exempted Sales And EUPurchases      | Данъчна основа на освободени доставки и ВОП                  | Освб. дост. по чл. 21(2), в рамките на ЕС                    | -                        |
| Column24_Data | Base Amount Exempted Sales And EUPurchases      | Данъчна основа на освободени доставки и ВОП                  | Освободени ВОД, извън територията на България                | -                        |
| Column24_Data | Base Amount Exempted Sales And EUPurchases      | Данъчна основа на освободени доставки и ВОП                  | Освободени доставки и освободени ВОП                         | -                        |
| Column25_Data | Base Amount Third Party Operation               | Данъчна основа от посредник в тристранна операция            | Доставки като посредник при тристранна операция              | -                        |
| Column25_Data | Base Amount Third Party Operation               | Данъчна основа от посредник в тристранна операция            | Доставки като посредник при тристранна операция (авансови плащания) | -                        |



**Purchases Ledger**

| Column        | Column Name (EN)                    | Column Name (BG)                                  | Deal Type (BG)                                        | Additional Conditions |
| ------------- | ----------------------------------- | ------------------------------------------------- | ----------------------------------------------------- | --------------------- |
| Column9_Data  | Base Amount Without Tax Credit      | Данъчна основа без право на данъчен кредит        | Сделки, внос и ВОП без право на данъчен кредит        | -                     |
| Column10_Data | Base Amount With Full Tax Credit    | Данъчна основа с право на пълен данъчен кредит    | Сделки, внос и ВОП с право на пълен данъчен кредит    | -                     |
| Column11_Data | VAT Amount With Full Tax Credit     | ДДС с право на пълен данъчен кредит               | Сделки, внос и ВОП с право на пълен данъчен кредит    | -                     |
| Column12_Data | Base Amount With Partial Tax Credit | Данъчна основа с право на частичен данъчен кредит | Сделки, внос и ВОП с право на частичен данъчен кредит | -                     |
| Column13_Data | VAT Amount With Partial Tax Credit  | ДДС с право на частичен данъчен кредит            | Сделки, внос и ВОП с право на частичен данъчен кредит | -                     |
| Column14_Data | Annual Correction                   | Годишна корекция                                  | Годишна корекция                                      | -                     |
| Column15_Data | Base Amount Third Party Operation   | Данъчна основа от посредник в тристранна операция | Придобиване от посредник в тристранна операция        | -                     |
