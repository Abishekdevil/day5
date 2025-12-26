
nums = list(map(int, input().split()))

max_count = 0
current_count = 0

for num in nums:
    if num == 1:
        current_count += 1
        if current_count > max_count:
            max_count = current_count
    else:
        current_count = 0

print( max_count)
