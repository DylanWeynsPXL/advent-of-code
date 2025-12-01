def count_zero_positions_from_file(filename):
    position = 50
    zero_count = 0

    with open(filename, "r") as f:
        for line in f:
            move = line.strip()
            if not move:
                continue

            direction = move[0]
            distance = int(move[1:])

            if position == 0:
                first = 100
            elif direction == 'R':
                first = 100 - position
            else: 
                first = position

            if distance >= first:
                zero_count += 1 + (distance - first) // 100


            if direction == 'L':
                position = (position - distance) % 100
            else:
                position = (position + distance) % 100

    return zero_count

file_path = 'advent-output.txt'
print('Times passed or landed on 0:', count_zero_positions_from_file(file_path))