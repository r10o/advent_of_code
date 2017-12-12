import sys

def main():
    if len(sys.argv) == 2:
        file_lines = open(sys.argv[1]).read().strip().replace(",", "").replace("<->", "").split('\n')

        groups = []

        while len(file_lines) != 0:
            grp = set()
            grp_len = len(grp) + 1

            while grp_len != len(grp):
                grp_len = len(grp)

                for line in file_lines:
                    int_line = [int(x) for x in line.split()]

                    if len(grp) == 0:
                        grp = set(int_line)
                        file_lines.remove(line)
                    elif len(set(int_line) & grp) != 0:
                        grp |= set(int_line)
                        file_lines.remove(line)

            groups.append(grp)

        print(len(groups))


if __name__ == "__main__":
    sys.exit(main())
