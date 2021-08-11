
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

#print(insert([1,3,4], 5))


def delnum(nums, val):
    #a = len(nums)-1
    for i ,value  in enumerate(nums):
        if value == val:
            nums.remove(value)
        else:
            pass
    print(nums)
    return len(nums)

def removeElement(nums, val):
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1
        print(nums)
        return len(nums)
#print(delnum([3,2,2,3],3))
print(delnum([0,1,2,2,3,0,4,2],2))
print(removeElement([0,1,2,2,3,0,4,2],2))