---
uid: ATP
---

# Available to promise

The available to promise (ATP) for a product and a date is the minimum quantity available for use in future issuing operations (sales, production, etc). It will not interfere with the issue operations, including this product, no matter if they are already planned, finished, or being executed just now. The calculation of the ATP is made by dates and it has meaning for the present or future dates. There is no use calculating it for past periods. Even more, the **[ATP algorithm](atp-algorithm.md)**, which is used for the calculation, is based on the fact that the ATP quantities are calculated for a date greater than or equal to today's date. This is because the current stock holds are used instead of their movements chronology.

The parameters, data, and **[ATP algorithm](atp-algorithm.md)** used for the ATP calculation are shown below. We will try to calculate the ATP for a specific date. Then, there is a detailed example of an ATP calculation for a long period (more than one date).

## Parameters

The main/required parameters are <b>product</b>, <b>own company</b>, and <b>date</b>. The ATP calculation is executed from the date and for the specified product and own company.

Additional parameters can be set as <b>store</b> and <b>lot</b>. If a store is specified, the calculation will be executed only for this store. Otherwise, the data is collected from all stores (as though it is limited by the product, the own company, and the date). The lot specification is similar.

## Data

For a standard ATP calculation, two types of data are used:

<b>1. Current stock holds</b>: 

It shows the availability of the product selected in the specified own company. If a store and a lot are provided, the data is filtered by them.

<b>2. Chronology of the store orders which are not executed</b>:

It loads the chronology of the unfulfilled parts of <i>non-voided</i> store orders, with statuses ranging from "Planned" to "Released". The data is filtered by the parameters entered for a product, own company, store, and lot. The chronology is sorted by the <i>Planned Release Date</i> field. The data in this field is fundamental for ATP calculations.

For example, let's assume that we have specified a <b>product</b>, <b>own company</b>, <b>store</b> and <b>lot</b>, and we want to calculate the ATP for date <b>2020/10/01</b>. The physical availability for this date is <b>13 pcs</b>, and before that date there are two unfulfilled, released store orders - one for receiving <b>7 pcs</b> with date <b>2020/09/28</b> and one for issuing <b>4 pcs</b> with date <b>2020/09/29</b>. The documents after <b>2020/10/01</b> are as follows:

- <b>2020/10/03</b> - released issuing store order for <b>5 pcs</b>, <b>3 pcs</b> of which are fulfilled with a store transaction on the same date, so the unfulfilled quantity is <b>2 pcs;</b>

- <b>2020/10/03</b> - released issuing store order for <b>5 pcs</b>, which is fulfilled with a store transaction marked as <i>single execution</i> and contains <b>2 pcs</b> from the same date, so the unfulfilled quantity is <b>0 pcs</b>;

- <b>2020/10/04</b> - planned receipt store order for <b>16 pcs</b>, unfulfilled;

- <b>2020/10/04</b> - planned issuing store order for <b>4 pcs</b>, unfulfilled;

- <b>2020/10/07</b> - planned issuing store order for <b>8 pcs</b>, unfulfilled;

- <b>2020/10/09</b> - planned issuing store order for <b>7 pcs</b>, unfulfilled;

- <b>2020/10/14</b> - planned receipt store order for <b>8 pcs</b>, unfulfilled;

- <b>2020/10/16</b> - planned receipt store order for <b>4 pcs</b>, unfulfilled;

- <b>2020/10/16</b> - planned issuing store order for <b>9 pcs</b>, unfulfilled;

- <b>2020/10/19</b> - planned issuing store order for <b>2 pcs</b>, unfulfilled;

The current availability is <b>8 pcs</b>. It is calculated by adding the two issuing store transactions with date <b>2020/10/03</b> to the availability from <b>2020/10/01</b>. The unfulfilled store orders chronology is as follows:

|<b>Date</b>|<b>Start quantity</b>|<b>Receipt quantity</b>|<b>Issue quantity</b>|<b>End quantity</b>
|:-|:-|:-|:-|:- 
|2020/10/01|3|-|-|3                 
|2020/10/03|-|-|2|1
|2020/10/04|-|16|4|13
|2020/10/07|-|-|8|5
|2020/10/09|-|-|7|-2
|2020/10/14|-|8|-|6
|2020/10/16|-|4|9|1
|2020/10/19|-|-|2|-1

The start quantity on <b>2020/10/01</b> is calculated by the two issuing store orders before <b>2020/10/01</b>. For the next dates, the unfulfilled store orders from the specific date are added.

Further reading:

- **[ATP algorithm](atp-algorithm.md)**

- **[ATP Reports](atp-reports.md)**
