def Minimum_opp(nums,k):
    nums.sort()
    nums=nums[::-1]
    n=len(nums)
    if(k in nums):
        print(nums,nums.index(k)+1)
Minimum_opp([3,2,5,3,1],5)
