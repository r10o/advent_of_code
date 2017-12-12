import sys

def main():
    if len(sys.argv) == 2:
        checksum = 0

        for line in open(sys.argv[1]):

            # convert to a list of integers using map
            # also possible to use list comprehension
            # int_list = [int(i) for i in line.split()]
            int_list = list(map(int, line.split()))
            checksum += max(int_list) - min(int_list)

        print(checksum)

if __name__ == "__main__":
    sys.exit(main())
