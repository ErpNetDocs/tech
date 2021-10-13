# Period determination methods

## From next month to last month

## From current month to last but one month

## By days

### Method of calculation

First, the quota for each month is calculated:

Month quota = Depreciable amount / Int(Month(Depreciation End Date - Depreciation Start Date -1))

For the first month: First month Depreciation =  Month quota * ((Number of Days in First month - Depreciation Start Date)/Number of Days in First month)

For every next month but last one: Depreciation =  Month quota

For the last month: Depreciation = Month quota - First month Depreciation

> Example:
>
> Asset with Useful life = 6 months and Depreciable amount = 120
>
> Depreciation Plan = 14.01 - 14.07
>
> Month quota = 120 / 6 months = 20 
>
> First month Depreciation = 20 * ((31-14)/31) = 10.97
>
> For 2,3,4,5 and 6th month Depreciation = 20
>
> Last month Depreciation = 20 - 10.97 = 9.03
>
