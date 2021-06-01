

################################# List Comprehension Applications ########################################

# Example - 1:

# Task- 1: Capitalize the names of the numeric variables in the "car_crashes" dataset and add "NUM" to the beginning.
    # Note: Non-numeric names should also be upper case.

# Expected output:
# ['NUM_TOTAL',
#  'NUM_SPEEDING',
#  'NUM_ALCOHOL',
#  'NUM_NOT_DISTRACTED',
#  'NUM_NO_PREVIOUS',
#  'NUM_INS_PREMIUM',
#  'NUM_INS_LOSSES',
#  'ABBREV']

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.head()
df.columns
df.dtypes

df.columns = ["NUM_" + col.upper() if df[col].dtype != "O" else col.upper() for col in df.columns]

###########################################

# Task 2: Write "FLAG" at the end of the names of the variables that do not contain "no" in the Column Name.
    # Note: All variable names must be upper case.

# Expected output:

# ['TOTAL_FLAG',
#  'SPEEDING_FLAG',
#  'ALCOHOL_FLAG',
#  'NOT_DISTRACTED',
#  'NO_PREVIOUS',
#  'INS_PREMIUM_FLAG',
#  'INS_LOSSES_FLAG',
#  'ABBREV_FLAG']

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.head()

df.columns = [col.upper() + "_FLAG" if "no" not in col else col.upper() for col in df.columns]
df.columns

"""
for col in df.columns:
    if "no" in col:
        print(col.upper())
    else:
        print(col.upper() + "_FLAG")
"""
#########################

# Task 3: Create a new dataframe (new_df) by selecting the names of the variables that ara different from the variable names given below list.

og_list = ["abbrev", "no_previous"]

# Expected Output:

# new_df.head()

#    total  speeding  alcohol  not_distracted  ins_premium  ins_losses
# 0 18.800     7.332    5.640          18.048      784.550     145.080
# 1 18.100     7.421    4.525          16.290     1053.480     133.930
# 2 18.600     6.510    5.208          15.624      899.470     110.350
# 3 22.400     4.032    5.824          21.056      827.340     142.390
# 4 12.000     4.200    3.360          10.920      878.410     165.630


import pandas as pd
pd.options.display.float_format = '{:.3f}'.format

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

og_list = ["abbrev", "no_previous"]
new_cols = [col for col in df.columns if col not in og_list]
new_df = df[new_cols]
new_df.head(3)

########################

# Task 4: Prefix the names of categorical variables with "CAT" and also convert all variable names to upper case.

import seaborn as sns
df = sns.load_dataset("car_crashes")

["CAT_" + col.upper() if df[col].dtype == "O" else col.upper() for col in df.columns]

################################# #################################### ########################################
################################# Dictionary Comprehension Applications #######################################


# Example - 1:

## "salary_dict" shows amounts of the employees. Let's calculate new salaries of the employees after the salary increase by using dictionary comprehension.
    # Note : If the salary amount is 7500 TL or more, 15% raise, , otherwise 20% increase will be applied.
    # Now, let's create a dictionary (new_dictionary) using dictionary comprehension.

salary_dict = {'John': 5000, 'Mark': 3000, 'Venessa': 6000, 'Mariam': 10000, 'Sam' : 7500}
new_dictionary = {k : (v + v * 0.15) if v >= 7500 else (v + v * 0.20)  for (k, v) in salary_dict.items() }
print(new_dictionary)

#################################

# Example - 2:

## Filter even numbers in dictionary values by using dictionary comprehension:

dict = {'jack': 38, 'john': 33, 'michael': 48, 'guido': 57}
new_dict = {k : v for (k, v) in dict.items() if v % 2 == 0 }
print(new_dict)

#################################
# Example - 3:

## Here is an example about create a dictionary where string value of the number as key and the number as values.

# Task - 1: Derive a list named "numbers_list" consisting of numbers from 1 to 12.

numbers_list = [n for n in range(1, 12)]
numbers_list

# Task - 2 : Create a dictionary by using "numbers_list" where string value of the odd numbers as key and the square of the odd numbers as values.

dict_odd = {x : x**2 for x in numbers_list if x % 2 == 1}
print(dict_odd)

#################################

# Example - 4:

# Task - 1 : Import Titanic dataset using Seaborn library.
# Task - 2 : Create a dictionary by using titanic dataframe where the "PassengerId" values is the key and the list of numeric variables is the value


# Task - 1 : Load Titanic dataset using Seaborn library.
# Task - 2 : Create a dictionary by using titanic dataframe where the values of the variable "PassengerId" is the key and the list of numeric variables is the value


# before
  PassengerId  Survived  ...  Parch     Fare
# 0            1         0  ...      0   7.2500
# 1            2         1  ...      0  71.2833
# 2            3         1  ...      0   7.9250
# 3            4         1  ...      0  53.1000
# 4            5         0  ...      0   8.0500


# after:
# {1: [1, 0, ..., 7.2500],
#  2: [2, 1, ..., 71.2833],
#  4: [3, 1, ..., 7.9250],
#  5: [4, 1, ..., 53.1000],
#  6: [5, 0, ..., 8.0500] }


import pandas as pd
df = pd.read_csv('titanic.csv')
df.head()

# We should create a new dataframe that includes only numerical variables and PassengerId column.
num_cols = [col for col in df.columns if (df[col].dtypes != "O" or "Passenger" in col)]

# Let's fill null values with 0 for now.
df[num_cols] = df[num_cols].fillna(0)

new_dict = {col[0] : [int(c) for c in col[1:]] for col in df[num_cols].values}
print(new_dict)


