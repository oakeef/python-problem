import sys

threshold = float(sys.argv[1])
limit = float(sys.argv[2])

total = 0

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    input_value = float(line)

    output_value = input_value - threshold

    if output_value < 0.0:
        output_value = 0.0

    budget = limit - total

    if output_value > budget:
        output_value = budget

    total += output_value
    
    print(round(output_value,1))

print(round(total,1))