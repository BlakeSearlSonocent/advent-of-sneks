from snek.file_utils import read_input

if __name__ == "__main__":
    fishes = list(map(int, read_input("six/input.txt").split(",")))
    counts = [fishes.count(i) for i in range(9)]
    for i in range(256):
        new_borns = counts.pop(0)
        counts[6] += new_borns
        counts.append(new_borns)

    print(sum(counts))
