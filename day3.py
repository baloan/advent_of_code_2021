#!python3
# Created 12 Dec 2021
# @author: andreas


def part_one():
    with open("inp3.txt") as f:
        inps = [s.strip('\n') for s in f] 
    
    bit_count = [0, ] * len(inps[0])
    
    for s in inps:
        # print("[", s, "]")
        for n, c in enumerate(s):
            # print(n, c)
            match c:
                case "0":
                    bit_count[n] -= 1
                case "1":
                    bit_count[n] += 1
                case _:
                    raise
    
    print(bit_count)
    gamma = mcb(bit_count)
    epsilon = lcb(bit_count)
    
    print(f"{gamma} x {epsilon} = {gamma*epsilon}")


def mcb(bit_count):
    res = 0
    for n in bit_count:
        res = res * 2 + (1 if n > 0 else 0)
    return res


def lcb(bit_count):
    res = 0
    for n in bit_count:
        res = res * 2 + (1 if n < 0 else 0)
    return res


def part_two():
    with open("inp3.txt") as f:
        inps = [s.strip('\n') for s in f] 

    oxy = rating(inps, "most common value")
    co2 = rating(inps, "least common value")
    print(f"{oxy} x {co2} = {oxy*co2}")

def rating(src, mode="most common value"):
    n = 0
    while len(src) > 1:
        ones = list()
        zeros = list()
        bit_count = 0
        print(len(src))
        for s in src:
            match s[n]:
                case "0":
                    bit_count -= 1
                    zeros.append(s)
                case "1":
                    bit_count += 1
                    ones.append(s)
                case _:
                    raise
        if mode == "most common value":
            if bit_count >= 0:
                src = ones
            else:
                src = zeros
        else:
            # least common value, co2
            if bit_count >= 0:
                src = zeros
            else:
                src = ones
        n += 1
    print(src[0])
    return int(src[0], 2)


# part_one()
part_two()
