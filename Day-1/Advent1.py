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

            if direction == 'L':
                position = (position - distance) % 100
            else: 
                position = (position + distance) % 100

            if position == 0:
                zero_count += 1

    return zero_count

file_path = "advent-output.txt"
print("Times ending at 0:", count_zero_positions_from_file(file_path))