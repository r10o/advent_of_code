import sys

def main():
    if len(sys.argv) == 2:
        count = 0

        for line in open(sys.argv[1]):
            if len(set(line.split())) == len(line.split()):
                count += 1

        print(count)

if __name__ == "__main__":
    sys.exit(main())
