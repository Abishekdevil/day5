
arr = list(map(int, input().split()))
target = int(input())

arr.sort()
result = []

def backtrack(start, path, total):
    if total == target:
        result.append(path[:])
        return
    if total > target:
        return

    for i in range(start, len(arr)):
        if i > start and arr[i] == arr[i - 1]:
            continue

        path.append(arr[i])
        backtrack(i + 1, path, total + arr  [i])
        path.pop()

backtrack(0, [], 0)


print(result)
