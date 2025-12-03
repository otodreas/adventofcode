raw_data = "18623-26004,226779-293422,65855-88510,868-1423,248115026-248337139,903911-926580,97-121,67636417-67796062,24-47,6968-10197,193-242,3769-5052,5140337-5233474,2894097247-2894150301,979582-1016336,502-646,9132195-9191022,266-378,58-91,736828-868857,622792-694076,6767592127-6767717303,2920-3656,8811329-8931031,107384-147042,941220-969217,3-17,360063-562672,7979763615-7979843972,1890-2660,23170346-23308802"

import math


xxx = [111111, 222222]
xx = range(xxx[0], xxx[1] + 1)

# xx = (range(1234, 1236))

# print(len(x)%2)

# for x in xx:
#     x = str(x)
#     for i in range(2, math.floor(len(x)/2)+1):        
#         if len(x)%i == 0:           

#             slices = []
#             for j in range(int(len(x)/i)):
#                 slices.append(x[j*i:(j+1)*i])
#             if len(set(slices)) == 1:
#                 print(x)
#                 break



class idParser:
    def __init__(self):
        pass

    def make_data_list(self, txt_data):
        self.txt_data = txt_data
        txt_data_list = txt_data.split(sep=",")

        values = []
        for d in txt_data_list:
            pair = d.split(sep="-")
            for i in [0, 1]:
                pair[i] = int(pair[i])
            values.append(range(pair[0], pair[1] + 1))

        return values
    
    def parse1(self, values, tb = False):
        self.values = values
        self.tb = tb
        sum_invalid_ids = 0

        for pair in values:
            ids = list(pair)
            for id in ids:
                id = str(id)
                if len(id) % 2 == 0:
                    midpoint = int(len(id)/2)
                    front = id[:midpoint]
                    back = id[midpoint:]
                    if front == back:
                        sum_invalid_ids += int(id)
                        if tb:
                            print(int(id))

        return sum_invalid_ids
    
    def parse2(self, values, tb=False):
        self.values = values
        self.tb = tb
        sum_invalid_ids = 0

        for pair in values:
            ids = list(pair)
            for id in ids:
                id = str(id)
                for i in range(1, math.floor(len(id)/2)+1):
                    if len(id) % i == 0:
                        slices = []
                        for j in range(int(len(id)/i)): 
                            slices.append(id[j*i:(j+1)*i])
                        if len(set(slices)) == 1:
                            sum_invalid_ids += int(id)
                            if tb:
                                print(int(id))
                            break

        return(sum_invalid_ids)                         





# for x in xx:
#     x = str(x)
#     for i in range(1, math.floor(len(x)/2)+1):
#         if len(x)%i == 0:
#             slices = []
#             for j in range(int(len(x)/i)):
#                 slices.append(x[j*i:(j+1)*i])
#             if len(set(slices)) == 1:
#                 print(x)
#                 break

# print(x[:f])
# print(x[f:])
# for i in range(1, (math.floor(len(x)/2)) + 1):
#     for j in range()
    
    
#     y = x[0:i]
#     z = x[i:i*2]
#     if y == z:
#         print(y, z, "match")
#     else:
#         print(y, z)

# raw_data_list = raw_data.split(sep=",")

# values = []
# for d in raw_data_list:
#     pair = d.split(sep="-")
#     for i in [0, 1]:
#         pair[i] = int(pair[i])
#     values.append(range(pair[0], pair[1]))

# sum_invalid_ids = 0

# for pair in values:
#     ids = list(pair)
#     for id in ids:
#         id = str(id)
#         if len(id) % 2 == 0:
#             midpoint = int(len(id)/2)
#             front = id[:midpoint]
#             back = id[midpoint:]
#             if front == back:
#                 sum_invalid_ids += int(id)



# for pair in values:
#     ids = list(pair)
#     for id in ids:
#         id = str(id)
#         for i in range(2, math.floor(len(id)/2)+1):
#             if len(id)%i == 0:
#                 slices = []
#                 for j in range(int(len(id)/i)):
#                     slices.append(id[j*i:(j+1)*i])
#                 if len(set(slices)) == 1:
#                     sum_invalid_ids += int(id)
#                     # print(id)
#                     break

# print(sum_invalid_ids)