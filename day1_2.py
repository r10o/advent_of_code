import sys
import logging

def main():
    if len(sys.argv) == 2:

        # The sum of the digits
        sum_digits = 0

        dat_file = open(sys.argv[1])
        digits = dat_file.read()

        offset = len(digits) // 2

        # Iterate over the string
        for i in range(0, len(digits)):
            num = digits[i]

            # Make sure to wrap the next digit around to the first one
            lead = digits[(i + offset) % (len(digits) - 1)]

            if num == lead:
                sum_digits += int(num)

        print(sum_digits)


if __name__ == "__main__":
    sys.exit(main())
