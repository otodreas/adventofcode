import numpy as np

class FreshChecker:
    def __init__(self):
        pass

    def get_ranges(self, data):
        ranges = data
        range_indices_array = np.zeros((len(data), 2), dtype=np.int64)
        for i, r in enumerate(ranges):
            nums = r.split("-")
            range_indices_array[i] = np.array([nums[0], int(nums[1])+1])
    
        range_indices_array_sorted = np.sort(range_indices_array, 0)
        ranges = []
        for i, r in enumerate(range_indices_array_sorted):
            ranges.append(range(r[0], r[1]))
        
        self.ranges = ranges

    def check_fresh(self, id):
        for r in self.ranges:
            if id in r:
                return True
        return False
    
    def count_fresh_ids(self):
        non_overlapping_ranges = []
        for i, r in enumerate(self.ranges[:-1]):
            r0 = r
            r1 = self.ranges[i+1]
        sorted_ranges = []
        fresh_ids = []
        return len(fresh_ids)