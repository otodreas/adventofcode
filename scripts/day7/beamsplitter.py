import re

class BeamSplitter:
    def __init__(self):
        self.indices_in = set()

    def find_splits(self, data_list):
        n_splits = 0
        for line in data_list:
            beam_indices = set([c.start(0) for c in re.finditer("[^.]", line.strip())])
            if "S" in line:
                self.indices_in = beam_indices
            else:
                if len(beam_indices) > 0:
                    for i in beam_indices & self.indices_in:
                        self.indices_in.remove(i)
                        self.indices_in.update((i-1, i+1))
                        n_splits += 1
        return n_splits