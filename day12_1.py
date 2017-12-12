import sys

def main():
    if len(sys.argv) == 2:
        group = {0}
        group_size = len(group) + 1

        while group_size != len(group):
            group_size = len(group)

            for line in open(sys.argv[1]):

                line_parts = line.replace(",","").split()
                del line_parts[1]
                line_parts = [int(x) for x in line_parts]

                add = False

                for i in line_parts:
                    if i in group:
                        add = True

                if add:
                    for i in line_parts:
                        group.add(i)
                
        print(group_size)

if __name__ == "__main__":
    sys.exit(main())
