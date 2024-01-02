# data_cleaning_consulate_2024

most raw data that are handed down are often edited and modified from the top, and by the time it reaches us, tend to be errored or misformatted. 

However, as long as they belong to the same column (feature), they should hold the same foramt. 

Therefore, I created this repo to make my work easier by unifying certain String values to a certain format using regular expressions.


### Address


=> delete end past zip code (5 digit)

### Phone Number
=> clean country code (+NN)
=> check if the number is 10 digits
  => return None if false
