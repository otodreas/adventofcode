import numpy as np
from rollaccess import RollAccess

r = RollAccess()
start_arr = r.make_matrix("scripts/day4/input4.txt")
nrolls, arr = r.get_rolls(start_arr)
print(nrolls)  # Print number of rolls accessed first time

total_rolls_pulled = nrolls
while True:
    nrolls, arr_updated = r.get_rolls(arr)
    total_rolls_pulled += nrolls
    if not np.array_equal(arr, arr_updated):
        arr = arr_updated
    else:
        break
print(total_rolls_pulled)  # Print all possible rolls to get
