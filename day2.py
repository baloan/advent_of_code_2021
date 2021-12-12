#!python3
# Created 12 Dec 2021
# @author: andreas

def part_one():
    with open("inp2.txt") as f:
        inps = [s.split() for s in f]
    
    hpos = depth = 0

    for cmd, s in inps:
        match (cmd, int(s)):
            case ["forward", n]:
                hpos += n
            case ["down", n]:
                depth += n
            case ["up", n]:
                depth -= n
            case _:
                print(f"Sorry, I couldn't understand {cmd!r}")           
    
    print(f"{hpos} x {depth} = {hpos*depth}")


def part_two():
    with open("inp2.txt") as f:
        inps = [s.split() for s in f]
    
    aim = hpos = depth = 0

    for cmd, s in inps:
        match (cmd, int(s)):
            case ["forward", n]:
                hpos += n
                depth += aim * n
            case ["down", n]:
                aim += n
            case ["up", n]:
                aim -= n
            case _:
                print(f"Sorry, I couldn't understand {cmd!r}")           
    
    print(f"{hpos} x {depth} = {hpos*depth}")

# part_one()
part_two()
