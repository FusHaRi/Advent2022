def separate_elves(input_file: str):
    bags = []
    with open(input_file) as elves_bags:
        for treats in elves_bags:
            if treats.strip():
                bags.append(int(treats))
            elif bags:
                yield bags
                bags = []

        if bags:
            yield bags


def main():
    total_cals = []
    for i in separate_elves("elves_goodies.txt"):
        i = sum(i)
        total_cals.append(i)

    total_cals = sorted(total_cals, reverse=True)

    print(f"Day 1 answer 1: {max(total_cals)}")

    print(f"Day 1 answer 2: {sum(total_cals[:3])}")


main()
