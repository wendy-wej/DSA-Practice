
nums = [0,1,2,3,4,3,5,3,7,3,9,3,7,9,1,0,2]
x = len(nums)
for i in range(0, len(nums)):
    for j in range(i+1, len(nums)):
        if j <= x :
            if nums[i] == nums[j]:
                nums.pop(j)
                print(nums)

