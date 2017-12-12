import sys

def main():
    if len(sys.argv) == 2:
        checksum = 0

        for line in open(sys.argv[1]):

            # convert to a sorted list of integers using map
            # also possible to use list comprehension
            # int_list = [int(i) for i in line.split()]
            int_list = sorted(list(map(int, line.split())))

            lead_iter = 0
            end_iter = len(int_list)

            divisible = False

            while not divisible and end_iter != 0:
                lead_iter = 0
                end_iter -= 1

                while lead_iter < end_iter and not divisible:
                    if int_list[end_iter] % int_list[lead_iter] == 0:
                        divisible = True
                    else:
                        lead_iter += 1

            checksum += int_list[end_iter] // int_list[lead_iter]

        print(checksum)

if __name__ == "__main__":
    sys.exit(main())
