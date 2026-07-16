import sys

threshold = sys.argv[1]
limit = sys.argv[2]

print(f"threshold: {threshold}, limit: {limit}")

for line in sys.stdin:
    if not line:
        continue

    
    print(f"value: {line}")