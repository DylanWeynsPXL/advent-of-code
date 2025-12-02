def is_invalid_id(n):
    s = str(n)
    length = len(s)

    #must be even length
    if length % 2 != 0:
        return False

    half = length // 2
    first = s[:half]
    second = s[half:]

    return first == second


def sum_invalid_ids_from_file(filename):
    total = 0

    with open(filename, "r") as f:
        line = f.read().strip()

        ranges = line.split(",")

        for r in ranges:
            if "-" not in r:
                continue

            start, end = r.split("-")
            start = int(start)
            end = int(end)

            for num in range(start, end + 1):
                if is_invalid_id(num):
                    total += num

    return total


file_path = "advent-output.txt"
print("Sum of invalid IDs:", sum_invalid_ids_from_file(file_path))