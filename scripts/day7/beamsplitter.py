import re


class BeamSplitter:
    def __init__(self):
        pass

    def find_splits(self, data_list, method):
        n_splits = 0
        paths = []
        for line in data_list:
            split_indices = set([c.start(0) for c in re.finditer("[^.]", line.strip())])
            if "S" in line:
                beam_indices = split_indices
            else:
                if len(split_indices) > 0:
                    for i in sorted(list(split_indices & beam_indices)):
                        beam_indices.remove(i)
                        beam_indices.update((i - 1, i + 1))
                        n_splits += 1
        return n_splits if method == 1 else len(paths)
