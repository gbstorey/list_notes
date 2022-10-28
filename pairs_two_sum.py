def pairs_two_sum(nums: list, target):
    for n in range(len(nums)):
        for j in range(n+1, len(nums)):
            if nums[n] == nums[j]:
                continue
            elif nums[n] + nums[j] == target:
                print(n, j)
myList = [1,2,3,2,3,4,5,6]
pairs_two_sum(myList, 6)