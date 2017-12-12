import sys
import math

def main():
    if len(sys.argv) == 2:
        num_string = open(sys.argv[1]).read()

        num = int(num_string)

        # Find the next integer square root greater than the input number
        num_sqrt = math.ceil(math.sqrt(num))

        # Make sure to find the next odd square root
        if num_sqrt % 2 == 0:
            num_sqrt += 1

        # Find the square, will be greater than the input number
        num_square = num_sqrt ** 2

        # Calculate the number of steps:
        # Find the nearest corner of the square in which the input number falls
        # Take the difference between the corner and the input number
        # The number of steps from the corner is always the sqrt of the largest number in the square - 1
        # Subtract the difference of the input number and the nearest corner and subtract it from the number of steps from the corner
        steps = num_sqrt - 1 - ((num_square - num) % (num_sqrt - 1))

        print(steps)
        

if __name__ == "__main__":
    sys.exit(main())
