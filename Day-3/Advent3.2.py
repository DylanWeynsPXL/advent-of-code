
def max_joltage_for_bank(bank):
    number = 0
    num_digits = 12
    to_remove = len(bank) - num_digits
    answer = []
    for digit in bank:
        keep_removing = True
        while keep_removing:
            if len(answer) == 0:
                keep_removing = False
            elif to_remove == 0:
                keep_removing = False
            elif answer[-1] >= digit:
                keep_removing = False
            else:
                answer.pop()
                to_remove -= 1
        answer.append(digit)
    while len(answer) > num_digits:
        answer.pop()
    for digit in answer:
        number = number * 10 + int(digit)
    return number


def sum_max_joltage_from_file(filename):
    total = 0
    with open(filename, "r") as f:
        for line in f:
            bank = line.strip()
            total += max_joltage_for_bank(bank)
    return total


file_path = "advent-output.txt"
print("Sum of max joltage:", sum_max_joltage_from_file(file_path))