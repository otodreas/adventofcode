import numpy as np


class RollAccess:
    def __init__(self):
        pass

    def make_matrix(self, text):
        with open(text, "r") as f:
            lst = []
            for line in f:
                lst.append(list("." + line.strip() + "."))
            pad = [list("." * len(lst[0]))]
            return np.array(pad + lst + pad)

    def get_rolls(self, arr):
        accessible_rolls_count = 0
        arr_updated = np.copy(arr)
        # Loop through each position, not including pad positions
        for i in range(1, np.shape(arr)[0] - 1):
            for j in range(1, np.shape(arr)[1] - 1):
                # Check if the position contains a roll
                if arr[i, j] == "@":
                    frame = np.array([arr[i - 1 : i + 2, j - 1 : j + 2]])
                    kernel = np.array(
                        [["@", "@", "@"], ["@", "X", "@"], ["@", "@", "@"]]
                    )
                    # Update variables if there are 4 or more rolls around the position
                    if np.sum(frame == kernel) < 4:
                        accessible_rolls_count += 1
                        arr_updated[i, j] = "."

        return accessible_rolls_count, arr_updated
