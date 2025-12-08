import re


class BeamSplitter:
    def __init__(self):
        pass

    def count_splits(self, data_list):
        n_splits = 0
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
        return n_splits

    def count_paths(self, data_list):
        paths = []
        for i, line in enumerate(data_list):
            split_indices = set([c.start(0) for c in re.finditer("[^.]", line.strip())])
            if "S" in line:
                beam_indices = split_indices
                paths.append(list(beam_indices))
            else:
                if len(split_indices) > 0:
                    for i in sorted(list(split_indices & beam_indices)):
                        beam_indices.remove(i)
                        beam_indices.update((i - 1, i + 1))
                        updated_paths = []
                        for p in paths:
                            if p[-1] == i:
                                updated_paths.append(p + [p[-1] + 1])
                                updated_paths.append(p + [p[-1] - 1])
                            else:
                                updated_paths.append(p)
                        paths = updated_paths
        return len(paths)