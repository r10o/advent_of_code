import sys

def main():
    if len(sys.argv) == 2:
        count = 0

        passphrase = True

        for line in open(sys.argv[1]):
            words = line.strip().split()

            lead_iter = 0
            while passphrase and lead_iter < len(words):

                i = lead_iter + 1
                while passphrase and i < len(words):

                    if sorted(list(words[lead_iter])) == sorted(list(words[i])):
                        passphrase = False

                    i += 1

                lead_iter += 1

            if passphrase:
                count += 1
            else:
                passphrase = True

        print(count)

if __name__ == "__main__":
    sys.exit(main())
