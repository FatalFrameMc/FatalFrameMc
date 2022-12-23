# Micheal Cudd
# Module 04 Programming Assignment
# Part A

# Paolo's Pool Service offers pool cleaning and maintenance services for homeowner's with a pool in their back yard.
#  Write a program called pool_service.py to help customers choose a service plan. Prompt the user to input the following information:
# Pool depth # Number of cleaning visits per month # Number of "deep cleaning" visits per year

# Based on the input, use branching to recommend appropriate service plan options:
# A customer with a pool depth of 5 feet or less, with less than 4 visits per month and less than 3 deep cleanings per year should choose Plan A at $44 per month.
# A customer with a pool depth of 5 feet or less, with 4 or more visits per month OR 3 or more deep cleanings per year should choose Plan B at $54 per month.
# A customer with a pool depth of more than 5 feet, with less than 4 visits per month and less than 3 deep cleanings per year should choose Plan C at $58 per month.
# A customer with a pool depth of more than 5 feet, with 4 or more visits per month OR 3 or more deep cleanings per year should choose Plan D at $64 per month.

# plans and cost
plan_a = '$44 per month'
plan_b = '$54 per month'
plan_c = '$58 per month'
plan_d = '$64 per month'


# Pool depth
pool_depth = (int(input("What is the depth of your pool. ")))

# Number of cleaning visits per month
visits = (int(input("How many cleanings per month. ")))

# Number of "deep cleaning" visits per year
deep_clean = (int(input("How many deep cleanings per year. ")))

# make sure inputs work.
# print(pool_depth, visits, deep_clean)

# plan a
# pool depth of 5 feet or less, with less than 4 visits per month and less than 3 deep cleanings
if pool_depth <= 5 and visits < 4 and deep_clean < 3:
    print('You should choose plan a at', plan_a)

# plan b
#  pool depth of 5 feet or less, with 4 or more visits per month OR 3 or more deep cleanings per year
if (pool_depth <= 5 and visits >= 4) or (pool_depth <= 5 and deep_clean >= 3):
    print('You should choose plan b at', plan_b)

# plan c
#  Pool depth of more than 5 feet, with less than 4 visits per month and less than 3 deep cleanings
if pool_depth > 5 and visits < 4 and deep_clean < 3:
    print('You should choose plan c at', plan_c)

# plan d
#  pool depth of more than 5 feet, with 4 or more visits per month OR 3 or more deep cleanings
if (pool_depth > 5 and visits >= 4) or (pool_depth > 5 and deep_clean >= 3):
    print('You should choose plan d at', plan_d)
