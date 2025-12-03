from idParser import idParser

def solve_toy(toy_data, key1, key2):
    parser = idParser()
    values = idParser.make_data_list(parser, toy_data)
    answer1 = idParser.parse1(parser, values, tb=True)
    answer2 = idParser.parse2(parser, values, tb=True)
    return [not answer1-key1, not answer2-key2]

def solve(data):
    parser = idParser()
    values = idParser.make_data_list(parser, data)
    answer1 = idParser.parse1(parser, values, tb=False)  # SOLVED: 19386344315
    answer2 = idParser.parse2(parser, values, tb=False)
    return [answer1, answer2] 

toy_data = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

with open("scripts/day2/input.txt", "r") as f:
    data = f.read().strip()

print(f"Toy solved: {solve_toy(toy_data, 1227775554, 4174379265)}")
print(f"Solutions: {solve(data)}")