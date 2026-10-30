# Progressive Electricity Billing (Case Study 2)

## 1. Problem Statement
A household's electricity bill depends on slabs: the more units used, the higher the rate per unit. A fixed charge, a surcharge for high consumption and a rebate for low consumption are also applied. Bills of several months must be compared to find unusual increases.

## 2. Objectives
- Calculate slab-wise energy charges for each month.
- Add the fixed charge and surcharge, and subtract the rebate.
- Compare each month with the previous month (percentage change).
- Identify months with an unusual increase.

## 3. Assumptions
- Slabs: first 100 units at Rs.3.00, next 100 at Rs.4.50, next 100 at Rs.6.00, above 300 at Rs.7.50.
- Fixed charge Rs.50 every month.
- Surcharge of 5% of energy charge if units > 300; rebate of Rs.25 if units <= 100.
- An increase of more than 40% over the previous month is called unusual.
- Units are non-negative numbers; there are six months of data.

## 4. Algorithm
1. Store tariff values, month names and units used.
2. For each month, charge the first three slabs one by one using a loop; charge remaining units at the top rate.
3. Calculate surcharge (if units > 300) and rebate (if units <= 100).
4. Total = energy + fixed + surcharge - rebate.
5. For months after the first, find percentage change from the previous total; if it is above 40%, mark UNUSUAL.
6. Print the table and the list of unusual months.
 
## 5. Conclusion
The program applies a slab-based tariff using a loop, handles fixed charge, surcharge and rebate with conditions, and finds months with unusual increases by comparing with the previous bill. Keeping rates in lists and variables makes the program easy to change when the tariff changes.
