

###############################################
# ÖDEV 3: List Comprehension Applications
###############################################

##############################################################################################

# Task- 1: Capitalize the names of the numeric variables in the "car_crashes" dataset and add "NUM" to the beginning.
    # Note: Non-numeric names should also be capitalized.

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

##############################################################################################

# Task 2: Write "FLAG" at the end of the names of the variables that do not contain "no" in the Column Name.
    # Note: All variable names must be uppercase.


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

##############################################################################################

# Task 3: Create a new dataframe (new_df) by selecting the names of the variables that ara differen from the variable names given below list.

og_list = ["abbrev", "no_previous"]

# Expected Output:

# new_df.head()
#
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

 