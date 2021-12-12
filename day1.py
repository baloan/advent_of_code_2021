#!python3
# Created 12 Dec 2021
# @author: andreas


def part_one():
    with open("inp1.txt") as f:
        inps = [int(s.strip()) for s in f]
    
    greater_count = sum([inps[n + 1] > inps[n] for n, _ in enumerate(inps[:-1])])
    
    print(greater_count)


def part_two():
    with open("inp1.txt") as f:
        inps = [int(s.strip()) for s in f]

    sliding_sum = [inps[n] + inps[n + 1] + inps[n + 2] for n in range(len(inps) - 2)]
    greater_count = sum([sliding_sum[n + 1] > sliding_sum[n] for n in range(len(sliding_sum) - 1)])
    
    print(greater_count)

# part_one()
part_two()
