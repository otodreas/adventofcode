import re


class BeamSplitter:
    def __init__(self):
        self.split_indices = set()

    def find_splits(self, data_list, method):
        n_splits = 0
        n_paths = 0
        for line in data_list:
            beam_indices = set([c.start(0) for c in re.finditer("[^.]", line.strip())])
            if "S" in line:
                self.split_indices = beam_indices
            else:
                if len(beam_indices) > 0:
                    for i in beam_indices & self.split_indices:
                        self.split_indices.remove(i)
                        self.split_indices.update((i - 1, i + 1))
                        n_splits += 1
        return n_splits if method == 1 else n_paths
