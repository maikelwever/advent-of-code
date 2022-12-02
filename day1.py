#!/usr/bin/env python3


def main():
    input_file = 'day1.txt'
    sums = []
    with open(input_file) as f:
        temp = 0

        for line in f.readlines():
            if line.strip():
                temp += int(line)
            else:
                sums.append(temp)
                temp = 0

    print(max(sums))
    print(sums)

    sorted_sums = sorted(sums, reverse=True)

    top_x = 0
    for i in range(3):
        top_x += sorted_sums[i]

    print(top_x)


if __name__ == "__main__":
    main()

