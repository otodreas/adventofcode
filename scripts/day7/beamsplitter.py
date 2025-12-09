from collections import Counter#import re


class BeamSplitter:
    def __init__(self):
        pass

    def count_beams(self, data_list, method="paths"):
        """
        method = "paths"  → count number of valid paths using DP
        method = "splits" → count number of beam splits
        """

        counts = Counter()       # for DP path counting
        beam_indices = set()     # active beam positions (set of ints)
        n_splits = 0             # only used if method="splits"

        for line in data_list:
            line = line.strip()
            # FAST replacement for regex: positions where char != "."
            split_indices = {i for i, c in enumerate(line) if c != "."}

            # Initialize at the S-row
            if "S" in line:
                beam_indices = split_indices
                if method == "paths":
                    for idx in beam_indices:
                        counts[idx] = 1
                continue

            # Normal row processing
            if split_indices:
                # restrict beams to valid splits
                active = beam_indices & split_indices

                # ---------- method = "splits" ----------
                if method == "splits":
                    next_beams = set()
                    for i in active:
                        # a "split" happens for each i hit
                        n_splits += 1
                        # beam splits left and right:
                        next_beams.add(i - 1)
                        next_beams.add(i + 1)
                    beam_indices = next_beams
                    continue

                # ---------- method = "paths" ----------
                elif method == "paths":
                    new_counts = Counter()
                    new_beams = set()

                    for i in active:
                        ways = counts[i]
                        left = i - 1
                        right = i + 1
                        new_counts[left] += ways
                        new_counts[right] += ways
                        new_beams.add(left)
                        new_beams.add(right)

                    counts = new_counts
                    beam_indices = new_beams
                    continue

            # if split_indices empty: beams die here
            beam_indices = set()
            if method == "paths":
                counts = Counter()

        # Final return
        if method == "paths":
            return sum(counts.values())
        elif method == "splits":
            return n_splits
        else:
            raise ValueError("method must be 'paths' or 'splits'")



    # def count_splits(self, data_list):
    #     n_splits = 0
    #     for line in data_list:
    #         split_indices = set([c.start(0) for c in re.finditer("[^.]", line.strip())])
    #         if "S" in line:
    #             beam_indices = split_indices
    #         else:
    #             if len(split_indices) > 0:
    #                 for i in split_indices & beam_indices:
    #                     beam_indices.remove(i)
    #                     beam_indices.update((i - 1, i + 1))
    #                     n_splits += 1
    #     return n_splits

    # def count_paths(self, data_list):
    #     paths = []
    #     for n, line in enumerate(data_list):
    #         print(n)
    #         split_indices = set([c.start(0) for c in re.finditer("[^.]", line.strip())])
    #         if "S" in line:
    #             beam_indices = split_indices
    #             paths.append(list(beam_indices))
    #         else:
    #             if len(split_indices) > 0:
    #                 for i in split_indices & beam_indices:
    #                     beam_indices.remove(i)
    #                     beam_indices.update((i - 1, i + 1))
    #                     updated_paths = []
    #                     for p in paths:
    #                         if p[-1] == i:
    #                             updated_paths.append(p + [p[-1] + 1])
    #                             updated_paths.append(p + [p[-1] - 1])
    #                         else:
    #                             updated_paths.append(p)
    #                     paths = updated_paths
    #     return len(paths)
    



    # def count_paths(self, data_list):
    #     paths = []
    #     for n, line in enumerate(data_list):
    #         print(n)
    #         split_indices = set([c.start(0) for c in re.finditer("[^.]", line.strip())])
    #         if "S" in line:
    #             beam_indices = split_indices
    #             paths.append(list(beam_indices))
    #         else:
    #             if len(split_indices) > 0:
    #                 for i in split_indices & beam_indices:
    #                     beam_indices.remove(i)
    #                     beam_indices.update((i - 1, i + 1))
    #                     updated_paths = []
    #                     for p in paths:
    #                         if p[-1] == i:
    #                             updated_paths.append(p + [p[-1] + 1])
    #                             updated_paths.append(p + [p[-1] - 1])
    #                         else:
    #                             updated_paths.append(p)
    #                     paths = updated_paths
    #     return len(paths)