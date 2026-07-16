import sys

threshold = float(sys.argv[1])
limit = float(sys.argv[2])

print(f"threshold: {threshold}, limit: {limit}")

total = 0

for line in sys.stdin:
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
    
    print(f"value: {input_value}, output: {output_value}, total: {total}")