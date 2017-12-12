import sys
import math

def main():
    if len(sys.argv) == 2:
        input_list = open(sys.argv[1]).read().strip().split(',')

        position = [0, 0, 0]

        max_dist = 0

        # map the 6 directions to 3 axes
        for d in input_list:
            if d == "n":
                position[0] += 1
                position[1] += 1
            elif d == "s":
                position[0] -= 1
                position[1] -= 1
            elif d == "ne":
                position[1] += 1
                position[2] += 1
            elif d == "sw":
                position[1] -= 1
                position[2] -= 1
            elif d == "nw":
                position[0] += 1
                position[2] -= 1
            elif d == "se":
                position[0] -= 1
                position[2] += 1

            # determine each positions distance since the max coordinate will be the tax cab distance
            new_max = max(math.fabs(position[0]), math.fabs(position[1]), math.fabs(position[2]))

            if new_max > max_dist:
                max_dist = new_max

        print(max_dist)

if __name__ == "__main__":
    sys.exit(main())
