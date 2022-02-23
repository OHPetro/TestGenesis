import pandas as pd
import numpy as np
df = pd.DataFrame({'grps': list('aaabbcaabcccbbc'), 'vals': [12,345,3,1,45,14,4,52,54,23,235,21,57,3,87]})

print("The sum of the three largest values in the group")
for i in df.grps.unique():
    group = df.groupby(["grps"]).get_group(i).sort_values(by=['vals'])
    group_sum_of_largest_3 =group.tail(3).sum()
    print(i," = ",group_sum_of_largest_3.vals)
