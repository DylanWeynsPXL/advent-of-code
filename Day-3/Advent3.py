
def max_joltage_for_bank(bank):
    max_jolt = 0
    length = len(bank)
    for first_idx in range(length):
        for second_idx in range(first_idx + 1, length):
            first_digit = int(bank[first_idx])
            second_digit = int(bank[second_idx])
            jolt = first_digit * 10 + second_digit
            if jolt > max_jolt:
                max_jolt = jolt
    return max_jolt


def sum_max_joltage_from_file(filename):
    total = 0
    with open(filename, "r") as f:
        for line in f:
            bank = line.strip()
            total += max_joltage_for_bank(bank)
    return total


file_path = "advent-output.txt"
print("Sum of max joltage:", sum_max_joltage_from_file(file_path))