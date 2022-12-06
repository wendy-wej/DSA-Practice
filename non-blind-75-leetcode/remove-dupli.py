def removeDuplicates(nums) -> int:
        x = 0
        i = 1
        count = 1
        f = len(nums)
        while i < f:
            if nums[x] == nums[i]:
                w = nums.pop(i)
                nums.append(w)
                f-=1
            else:
                count+=1 
                x+=1
                i+=1
        print(count)
        return nums
print(removeDuplicates([2,2,2,2,3,3,3,4,4,5,6,6,6,7]))
#[0,0,1,1,1,2,2,3,3,4]