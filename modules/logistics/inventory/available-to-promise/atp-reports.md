---
uid: ATP-reports
---

# ATP Reports

In Version 2018.2, we introduced two new reports – <b>Available to promise</b> and <b>Available to promise (by lots)</b>. These reports show the quantities available to promise (ATP) (by product or by product lot) from a current or future date, but not only as a calculated number. The reports allow us to see the separate records for all planned movements and therefore the projected available balance (PAB) for the different dates. Using it, we can see which numbers are behind the value of (ATP) and how it is calculated for the different periods.

# Details

The ATP available on a given date is the quantity that can be promised to orders scheduled for shipment (for more information, see topic [Available to promise](https://docs.erp.net/tech/modules/logistics/planning/available-to-promise/index.html?q=Available%20To%20Promise)) from that date to the date of the next planned movement. That is why the ATP in the reports is calculated from each scheduled date. In @@name, this is the planned release date of the store orders. The records represent the chronology of the unfulfilled parts of non-voided store orders, which has statuses from planned to released included. There is a separate record for each combination of <b>date, product, enterprise company and store</b>. In the available to promise (by lots) report, the records are also separated by a <b>lot</b>.

The calculation of ATP is based not only on the data of the <b>chronology of the store orders which are not executed</b>, but also on the information of the current stock holds (see topic [Available to promise](https://docs.erp.net/tech/modules/logistics/planning/available-to-promise/index.html?q=Available%20To%20Promise)). However, for the particular product or store, there may not be any unfulfilled shipments or deliveries and therefore those records won’t exist in the reports. For this reason, the reports start with an auxiliary line with a fictive “From date” which is equal to 01.01.2000 and contains the information for the starting availability, i.e. the <b>current availability</b>.
 
<b>As mentioned above, the rest of the records represent the chronology of the store orders which are not executed</b>. 

They contain information for:

- <b><i>Movements base</b></i> - The sum of the quantity of all planned stock movements (issue and receipt) on this date in base measurement unit. 

- <b><i>Movements to date base</b></i> - A running total of the quantity of all planned stock movements (issue and receipt) until this date (inclusive) in base measurement unit.

- <b><i>Projected availability</b></i> -  Projected Availability in base measurement unit on a particular date. A running total of the projected/expected available quantity calculated by adding supply or subtracting demand in chronological order in base measurement unit. The value includes all expected stock movements (issue and receipt) until this date (inclusive) and the current availability.

- <b><i>ATP Base</b></i> - Indicates the promissory amount in base unit valid from a specified date to the date of the next stock movement. This is the minimum quantity available for use for future issuing operations (sales, use in production, etc.), and which will not violate the planned issue operations.
