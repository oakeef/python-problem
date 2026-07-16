import sys

threshold = float(sys.argv[1])
limit = float(sys.argv[2])

print(f"threshold: {threshold}, limit: {limit}")

for line in sys.stdin:
    if not line:
        continue

    input_value = float(line)

    output = input_value - threshold

    if output < 0.0:
        output = 0.0
    
    print(f"value: {output}")