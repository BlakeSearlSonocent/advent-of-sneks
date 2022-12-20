from snek.file_utils import empty_line_separated_group_to_string_lists


def part_one():
    bingo = empty_line_separated_group_to_string_lists("four/input.txt")
    calls = [int(x) for x in bingo.pop(0)[0].split(",")]
    cards = [[[(int(x), False) for x in line.split()] for line in card] for card in bingo]

    for call in calls:
        for card in cards:
            rows, cols = len(card), len(card[0])
            mark_card(call, card)
            if is_complete(card):
                print(sum([(card[j][i])[0] for i in range(cols) for j in range(rows) if not (card[j][i])[1]]) * call)
                return


def part_two():
    bingo = empty_line_separated_group_to_string_lists("four/input.txt")
    calls = list(reversed([int(x) for x in bingo.pop(0)[0].split(",")]))
    cards = [[[(int(x), True) for x in line.split()] for line in card] for card in bingo]

    for call in calls:
        for card in cards:
            rows, cols = len(card), len(card[0])
            mark_card(call, card, False)
            if not is_complete(card):
                print(
                    (sum([(card[j][i])[0] for i in range(cols) for j in range(rows) if not (card[j][i])[1]]) - call)
                    * call
                )
                return


def is_complete(card) -> bool:
    return check_rows(card) or check_cols(card)


def check_rows(card) -> bool:
    return any(all([match[1] is True for match in row]) for row in card)


def check_cols(card) -> bool:
    _, cols = len(card), len(card[0])
    return any([all([(card[y][x])[1] for y in range(cols)]) for x in range(cols)])


def mark_card(call, card, mark=True):
    rows, cols = len(card), len(card[0])
    for i in range(cols):
        for j in range(rows):
            val, _ = card[j][i]
            if val == call:
                card[j][i] = (val, mark)


if __name__ == "__main__":
    part_one()
    part_two()
