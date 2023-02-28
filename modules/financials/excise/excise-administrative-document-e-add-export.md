# Excise administrative document: e-ADD export

EU Excise

|**e-ADD tags**                                               |**Excise Product Code**|
| ------------------------------------------------------------ | ------------------- |
|**Header**                                             |
|DocumentNumber                                       | Document.DocumentNumber    |
| DocumentDate             | Document.DocumentDate               |
| IsDelayedReporting                                       |IsDeferredSubmission     |
| IsExciseNote                                                       | @Exc_Purpose  |
| TotalAmountOfExciseDuty |SUM(Lines.ExciseAmount)           |
|                                                                                 |
|**PlaceOfIssue**       |
|Region                                       | TaxWarehouse.First(Store.@Exc_Region)   |
| Ethyl alcohol                                                | S300                |
| Partially denatured alcohol                                  | S400                |
| Other products containing ethyl alcohol                      | S500                |
| Vegetable and animal oils (energy products)<br />Products  falling within CN codes 1507 to 1518, if these are intended for use as  heating fuel or motor fuel | E200                |
| Mineral oils (energy products) <br />Products  failing within CN codes 2707 10, 2707 20, 2707 30, and 2707 50 | E300                |
| Leaded petrol                                                | E410                |
| Unleaded petrol                                              | E420                |
| Gasoil, unmarked                                             | E430                |
| Gasoil, marked                                               | E440                |
| Kerosene, unmarked                                           | E450                |
| Kerosene, marked                                             | E460                |
| Heavy fuel oil                                               | E470                |
| Products failing within CN codes 2710 11 21, 2710 11 25, 2710 19  29 in bulk commercial movements | E480                |
| Products failing within CN codes 2710 11 to 2710 19 69, not  specified above | E490                |
| Liquefied petroleum gases and other gaseous hydrocarbons (LPG) | E500                |
| Saturated acyclic hydrocarbons                               | E600                |
| Cyclic hydrocarbons                                          | E700                |
| Methanol (methyl alcohol)                                    | E800                |
| Mixture of acyclic hydrocarbons - "FAMAE"                    | E910                |
| Mixture of acyclic hydrocarbons - others                     | E920                |
