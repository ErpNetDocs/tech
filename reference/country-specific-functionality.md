---
uid: applicable-legislations
---

# Country-specific functionality

@@name contains some country, region, or other specific functionalities that are needed in order to meet legal or regulatory requirements. Such functionality is the creation of VAT returns and the VAT export files for submission to the National Revenue Agency (Bulgaria), for example.

## Party applicable legislations 

In parties, there is a child table with the applicable legislations for the particular party. The table contains information about the countries, states, unions, or other entities whose regulations apply to the party. The records in this table are used when determining if a business rule must be activated when, for example, it incorporates rules that are specific for the particular country's laws.

### Bulgaria (BG)

#### List of the system deal types and their correlation with the sales and purchases ledger's columns

The VAT declaration in @@name is a document that serves as a basis for the creation of a VAT return and the VAT export files for submission to the National Revenue Agency. The information in the VAT declaration is based on the VAT entries created in the system for the particular period.

The entries amounts (_Amount base_ and _VAT amount base_) are entered in different columns of the sales and purchases ledger of the VAT declaration depending on their deal type. 

For more information about entries' deal type and amount calculation, see **Defining VAT and base for VAT Entries**.

This article contains information about the correlation between the system deal types and the columns of the sales and purchases ledgers according to which the entries amounts are distributed to those columns.

**Sales ledger**

| Column        | Column name (EN)                                | Column name (BG)                                             | Deal type (BG)                                               | Value       | Additional Conditions    |
| ------------- | ----------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ----------- | ------------------------ |
| Column8a_Data | Delivery, art. 163a, or Import, art. 167a       | Доставка по чл. 163а или внос по чл. 167а от ЗДДС            | Внос или вътреобщностно придобиване на хляб                  | 07          | Apply_Date >= '20220701' |
| Column8a_Data | Delivery, art. 163a, or Import, art. 167a       | Доставка по чл. 163а или внос по чл. 167а от ЗДДС            | Внос или вътреобщностно придобиване на брашно                | 08          | Apply_Date >= '20220701' |
| Column8a_Data | Delivery, art. 163a, or Import, art. 167a       | Доставка по чл. 163а или внос по чл. 167а от ЗДДС            | Доставки на хляб                                             | 07          | Apply_Date >= '20220701' |
| Column8a_Data | Delivery, art. 163a, or Import, art. 167a       | Доставка по чл. 163а или внос по чл. 167а от ЗДДС            | Доставки на брашно                                           | 08          | Apply_Date >= '20220701' |
| Column9_Data  | Total Base Amount                               | Общ размер на данъчните основи                               | ВОД                                                          | Base Amount | -                        |
| Column9_Data  | Total Base Amount                               | Общ размер на данъчните основи                               | Доставка по чл. 163а от ЗДДС част I (отпадъци) на Приложение 2 | Base Amount | -                        |
| Column9_Data  | Total Base Amount                               | Общ размер на данъчните основи                               | Доставка по чл. 163а от ЗДДС част II (земеделска продукция) на Приложение 2 | Base Amount | -                        |
| Column9_Data  | Total Base Amount                               | Общ размер на данъчните основи                               | Доставка по чл.140,146,173(1) или 173(4)                     | Base Amount | -                        |
| Column9_Data  | Total Base Amount                               | Общ размер на данъчните основи                               | Износ по глава трета от ЗДДС                                 | Base Amount | -                        |
| Column9_Data  | Total Base Amount                               | Общ размер на данъчните основи                               | Начисляване на ДДС в др. случаи                              | Base Amount | Apply_Date >= '20160201' |
| Column9_Data  | Total Base Amount                               | Общ размер на данъчните основи                               | Облагаеми доставки 7/9%                                      | Base Amount | -                        |
| Column9_Data  | Total Base Amount                               | Общ размер на данъчните основи                               | Облагаеми сделки                                             | Base Amount | -                        |
| Column9_Data  | Total Base Amount                               | Общ размер на данъчните основи                               | Самоначисляване на ДДС по чл.82,ал.2-5                       | Base Amount | -                        |
| Column9_Data  | Total Base Amount                               | Общ размер на данъчните основи                               | Самоначисляване на ДДС при ВОП                               | Base Amount | -                        |
| Column9_Data  | Total Base Amount                               | Общ размер на данъчните основи                               | Внос или вътреобщностно придобиване на хляб                  | Base Amount | Apply_Date >= '20220701' |
| Column9_Data  | Total Base Amount                               | Общ размер на данъчните основи                               | Внос или вътреобщностно придобиване на брашно                | Base Amount | Apply_Date >= '20220701' |
| Column9_Data  | Total Base Amount                               | Общ размер на данъчните основи                               | Доставки на хляб                                             | Base Amount | Apply_Date >= '20220701' |
| Column9_Data  | Total Base Amount                               | Общ размер на данъчните основи                               | Доставки на брашно                                           | Base Amount | Apply_Date >= '20220701' |
| Column10_Data | Total VAT Amount                                | Всичко начислен ДДС                                          | Начислен ДДС при ползване за лични нужди                     | VAT Amount  | Apply_Date >= '20160201' |
| Column10_Data | Total VAT Amount                                | Всичко начислен ДДС                                          | Начисляване на ДДС в др. случаи                              | VAT Amount  | -                        |
| Column10_Data | Total VAT Amount                                | Всичко начислен ДДС                                          | Облагаеми доставки 7/9%                                      | VAT Amount  | -                        |
| Column10_Data | Total VAT Amount                                | Всичко начислен ДДС                                          | Облагаеми сделки                                             | VAT Amount  | -                        |
| Column10_Data | Total VAT Amount                                | Всичко начислен ДДС                                          | Самоначисляване на ДДС по чл.82,ал.2-5                       | VAT Amount  | -                        |
| Column10_Data | Total VAT Amount                                | Всичко начислен ДДС                                          | Самоначисляване на ДДС при ВОП                               | VAT Amount  | -                        |
| Column10_Data | Total VAT Amount                                | Всичко начислен ДДС                                          | Внос или вътреобщностно придобиване на хляб                  | VAT Amount  | Apply_Date >= '20220701' |
| Column10_Data | Total VAT Amount                                | Всичко начислен ДДС                                          | Внос или вътреобщностно придобиване на брашно                | VAT Amount  | Apply_Date >= '20220701' |
| Column11_Data | Base Amount 20 Percent                          | Данъчна основа 20%                                           | Доставка по чл. 163а от ЗДДС част I (отпадъци) на Приложение 2 | Base Amount | -                        |
| Column11_Data | Base Amount 20 Percent                          | Данъчна основа 20%                                           | Доставка по чл. 163а от ЗДДС част II (земеделска продукция) на Приложение 2 | Base Amount | -                        |
| Column11_Data | Base Amount 20 Percent                          | Данъчна основа 20%                                           | Начисляване на ДДС в др. случаи                              | Base Amount | Apply_Date >= '20160201' |
| Column11_Data | Base Amount 20 Percent                          | Данъчна основа 20%                                           | Облагаеми сделки                                             | Base Amount | -                        |
| Column12_Data | VAT Amount 20 Percent                           | Начислен ДДС 20%                                             | Начисляване на ДДС в др. случаи                              | VAT Amount  | Apply_Date >= '20160201' |
| Column12_Data | VAT Amount 20 Percent                           | Начислен ДДС 20%                                             | Облагаеми сделки                                             | VAT Amount  | -                        |
| Column13_Data | Base Amount EUPurchase                          | Данъчна основа на ВОП                                        | Самоначисляване на ДДС при ВОП                               | Base Amount | -                        |
| Column13_Data | Base Amount EUPurchase                          | Данъчна основа на ВОП                                        | Внос или вътреобщностно придобиване на хляб                  | Base Amount | Apply_Date >= '20220701' |
| Column13_Data | Base Amount EUPurchase                          | Данъчна основа на ВОП                                        | Внос или вътреобщностно придобиване на брашно                | Base Amount | Apply_Date >= '20220701' |
| Column14_Data | Base Amount VATL Article 82                     | Данъчна основа на доставките по чл.82, ал. 2 - 5             | Самоначисляване на ДДС по чл.82,ал.2-5                       | Base Amount | -                        |
| Column15_Data | VAT Amount EUPurchase VATL Article 82           | Начислен ДДС за ВОП и доставките по чл.82, ал. 2 - 5         | Самоначисляване на ДДС по чл.82,ал.2-5                       | VAT Amount  | -                        |
| Column15_Data | VAT Amount EUPurchase VATL Article 83           | Начислен ДДС за ВОП и доставките по чл.82, ал. 2 - 5         | Самоначисляване на ДДС при ВОП                               | VAT Amount  | -                        |
| Column15_Data | VAT Amount EUPurchase VATL Article 83           | Начислен ДДС за ВОП и доставките по чл.82, ал. 2 - 5         | Внос или вътреобщностно придобиване на хляб                  | VAT Amount  | Apply_Date >= '20220701' |
| Column15_Data | VAT Amount EUPurchase VATL Article 83           | Начислен ДДС за ВОП и доставките по чл.82, ал. 2 - 5         | Внос или вътреобщностно придобиване на брашно                | VAT Amount  | Apply_Date >= '20220701' |
| Column16_Data | VAT amout in case of personal use               | Начислен данък при ползване за лични нужди                   | Начислен ДДС при ползване за лични нужди                     | VAT Amount  | Apply_Date >= '20160201' |
| Column16_Data | VAT amout in case of personal use               | Начислен данък при ползване за лични нужди                   | Начисляване на ДДС в др. случаи                              | VAT Amount  | Apply_Date < '20160201'  |
| Column17_Data | Base Amount 9 %                                 | Данъчна основа 9 %                                           | Облагаеми доставки 7/9%                                      | Base Amount | -                        |
| Column18_Data | VAT Amount 9 %                                  | Начислен ДДС 9 %                                             | Облагаеми доставки 7/9%                                      | VAT Amount  | -                        |
| Column19_Data | Base Amount 0 Percent VATL Chapter 3            | Данъчна основа 0 % по глава трета от ЗДДС                    | Износ по глава трета от ЗДДС                                 | Base Amount | -                        |
| Column19_Data | Base Amount 0 Percent VATL Chapter 3            | Данъчна основа 0 % по глава трета от ЗДДС                    | Доставки на хляб                                             | Base Amount | Apply_Date >= '20220701' |
| Column19_Data | Base Amount 0 Percent VATL Chapter 3            | Данъчна основа 0 % по глава трета от ЗДДС                    | Доставки на брашно                                           | Base Amount | Apply_Date >= '20220701' |
| Column20_Data | Base Amount 0 Percent EUSale                    | Данъчна основа 0 % на ВОД                                    | ВОД                                                          | Base Amount | -                        |
| Column21_Data | Base Amount 0 Percent VATL Articles 140 146 173 | Данъчна основа 0 % по чл. 140, чл. 146 ал. 1 и чл. 173, ал. 1 и 4 | Доставка по чл.140,146,173(1) или 173(4)                     | Base Amount | -                        |
| Column22_Data | Base Amount Service Sales VATL Article 21       | Данъчна основа на услугите по чл. 21, ал. 2                  | Доставка по чл.21(2) в друга държава членка                  | Base Amount | -                        |
| Column23_Data | Base Amount VATL Article 69                     | Данъчна основа почл. 69, ал. 2                               | Доставка по чл.69(2) и дистанц. продажба към др.членка       | Base Amount | -                        |
| Column24_Data | Base Amount Exempted Sales And EUPurchases      | Данъчна основа на освободени доставки и ВОП                  | Освб. дост. по чл. 21(2), в рамките на ЕС                    | Base Amount | -                        |
| Column24_Data | Base Amount Exempted Sales And EUPurchases      | Данъчна основа на освободени доставки и ВОП                  | Освободени ВОД, извън територията на България                | Base Amount | -                        |
| Column24_Data | Base Amount Exempted Sales And EUPurchases      | Данъчна основа на освободени доставки и ВОП                  | Освободени доставки и освободени ВОП                         | Base Amount | -                        |
| Column25_Data | Base Amount Third Party Operation               | Данъчна основа от посредник в тристранна операция            | Доставки като посредник при тристранна операция              | Base Amount | -                        |
| Column25_Data | Base Amount Third Party Operation               | Данъчна основа от посредник в тристранна операция            | Доставки като посредник при тристранна операция (авансови плащания) | Base Amount | -                        |



**Purchases ledger**

| Column        | Column name (EN)                          | Column name (BG)                                  | Deal type (BG)                                        | Value       | Additional conditions    |
| ------------- | ----------------------------------------- | ------------------------------------------------- | ----------------------------------------------------- | ----------- | ------------------------ |
| Column8a_Data | Delivery, art. 163a, or Import, art. 167a | Доставка по чл. 163а или внос по чл. 167а от ЗДДС | Внос или вътреобщностно придобиване на хляб           | 07          | Apply_Date >= '20220701' |
| Column8a_Data | Delivery, art. 163a, or Import, art. 167a | Доставка по чл. 163а или внос по чл. 167а от ЗДДС | Внос или вътреобщностно придобиване на брашно         | 08          | Apply_Date >= '20220701' |
| Column9_Data  | Base Amount Without Tax Credit            | Данъчна основа без право на данъчен кредит        | Сделки, внос и ВОП без право на данъчен кредит        | Base Amount | -                        |
| Column10_Data | Base Amount With Full Tax Credit          | Данъчна основа с право на пълен данъчен кредит    | Сделки, внос и ВОП с право на пълен данъчен кредит    | Base Amount | -                        |
| Column10_Data | Base Amount With Full Tax Credit          | Данъчна основа с право на пълен данъчен кредит    | Внос или вътреобщностно придобиване на хляб           | Base Amount | Apply_Date >= '20220701' |
| Column10_Data | Base Amount With Full Tax Credit          | Данъчна основа с право на пълен данъчен кредит    | Внос или вътреобщностно придобиване на брашно         | Base Amount | Apply_Date >= '20220701' |
| Column11_Data | VAT Amount With Full Tax Credit           | ДДС с право на пълен данъчен кредит               | Сделки, внос и ВОП с право на пълен данъчен кредит    | VAT Amount  | -                        |
| Column11_Data | VAT Amount With Full Tax Credit           | ДДС с право на пълен данъчен кредит               | Внос или вътреобщностно придобиване на хляб           | VAT Amount  | Apply_Date >= '20220701' |
| Column11_Data | VAT Amount With Full Tax Credit           | ДДС с право на пълен данъчен кредит               | Внос или вътреобщностно придобиване на брашно         | VAT Amount  | Apply_Date >= '20220701' |
| Column12_Data | Base Amount With Partial Tax Credit       | Данъчна основа с право на частичен данъчен кредит | Сделки, внос и ВОП с право на частичен данъчен кредит | Base Amount | -                        |
| Column13_Data | VAT Amount With Partial Tax Credit        | ДДС с право на частичен данъчен кредит            | Сделки, внос и ВОП с право на частичен данъчен кредит | VAT Amount  | -                        |
| Column14_Data | Annual Correction                         | Годишна корекция                                  | Годишна корекция                                      | VAT Amount  | -                        |
| Column15_Data | Base Amount Third Party Operation         | Данъчна основа от посредник в тристранна операция | Придобиване от посредник в тристранна операция        | Base Amount | -                        |
