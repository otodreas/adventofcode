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
        paths = {0: []}
        paths_count = 0
        for line in data_list:
            split_indices = [c.start(0) for c in re.finditer("[^.]", line.strip())]
            if "S" in line:
                beam_indices = split_indices
                paths[paths_count] = beam_indices
                print(paths[0])
            else:
                if len(split_indices) > 0:
                    for i in beam_indices:
                        if i not in split_indices:
                            # paths[-1] = paths[-1].append(i)
                            pass
                        else:
                            # print(paths[paths_count])
                            # print(paths[paths_count].append(i-1)) if paths_count < 2 else None
                            paths_count += 1
                            paths[paths_count] = [1]#paths[paths_count-1]


                            # paths[paths_count] = paths[paths_count].append(i-1)
                            # print(paths)
                            beam_indices.pop(beam_indices.index(i))
                            beam_indices.append(i - 1); beam_indices.append(i + 1)
                            
                            
                            print(paths)
                            # paths[paths_count] = paths[paths_count - 1]
                            # paths[paths_count] = paths[paths_count].append(i+1)
                            # paths_count += 1
                            # paths[paths_count] = paths[paths_count - 1].append(i-1)
                            


# initialize queue with starting beam(s)
# while queue not empty:
#     pop a beam
#     if this beam hits a splitter:
#         create two new beams (left/right) with extended path history
#         push them to queue
#     else:
#         record that this beam is a completed path
