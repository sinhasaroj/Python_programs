# Using HashMaps

def twoSum(nums,target):

    '''
        :type nums: List[int]
        :type target: int
        :rtype : List[int]
    '''
    hashMap = {}
    for i in range(len(nums)):
        print(hashMap)

        
        diff = target - nums[i]
        if nums[i] in hashMap:
            return [hashMap[nums[i]],i]
        else:
            hashMap[diff] = i



target = 26
nums = [2,7,11,15]

# f1 = twoSum(nums,target)
# print(f1)


 #Using BruteForce
def bruteForceTwoSum(nums,target):

    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            sum_ = nums[i] + nums[j]
            if sum_ == target:
                return [i,j]

print(bruteForceTwoSum(nums,target)) 


