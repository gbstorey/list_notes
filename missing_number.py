def find_missing(arr: list):
    n = len(arr)+1
    return int((n*(n+1)/2 - sum(arr)))

one_to_hundred = []
for n in range(1,101):
    one_to_hundred.append(n)

one_to_hundred.remove(13)

print(find_missing(one_to_hundred))
