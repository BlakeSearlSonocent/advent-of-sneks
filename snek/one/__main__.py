from snek.file_utils import file_to_string_list

if __name__ == "__main__":
    depths = [int(x) for x in file_to_string_list("one/input.txt")]
    decreases = [sum(x < y for x, y in zip(depths, depths[i:])) for i in [1, 3]]
    print(decreases)
