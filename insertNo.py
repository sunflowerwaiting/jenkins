
def insert(nums, target):
    if target in nums :
        return nums.index(target)
    elif  nums[-1] < target :
        return len(nums)
    else:
        for i , value in enumerate(nums):
            if value > target:
                return i
            else:
                pass

print(insert([1,3,4], 5))