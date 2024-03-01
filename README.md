# data_cleaning_consulate_2024

most raw data that are handed down are often edited and modified from the top, and by the time it reaches us, tend to be errored or misformatted. 

However, as long as they belong to the same column (feature), they should hold the same format. 

Therefore, I created this repo to make my work easier by unifying certain String values to a certain format using regular expressions.



### Address


=> delete end past zip code (5 digit)

### Phone Number

First, we check the ITU country code for the number.

Because all the countries we have in the database are countries with ITU numbers of 2 digit, (there are countries with 3 digits ITU codes, but are not present in our database as they are mostly assigned to smaller countries) we limit the ITU code search to 2 numeric digits. 

Then, we assume all else remaining are correct, and remove all non-digit characters (such as . - / and whitespace) and join them together.
