import sys

def main():
    if len(sys.argv) == 2:
        num_string = open(sys.argv[1]).read().strip()

        num = int(num_string)


if __name__ == "__main__":
    sys.exit(main())
