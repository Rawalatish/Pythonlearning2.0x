# Continue
# Alternate for break

for num in range(1,10):
    if num % 2 == 0:
        print(f"Found even number {num}")
    else:
        print(f"Found odd number {num}")

print("=========")
# another way

for no in range(11,20):
    if no % 2 ==0:
        print(f"Found even number {no}")  # this is in the if loop
        continue
print(f"Found odd number {no}")  # this is in the for loop not in the if loop





