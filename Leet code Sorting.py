def isMonotonic(nums):
        num3=[]
        for i in nums:
            num3.append(i)
        num3.sort()
        if((nums[0]<=nums[1] and nums[1]<=nums[2]) or nums[0]<=nums[-1]):
            if (nums==num3):
                return "true"
            return "false"
        else:
            num2=num3[::-1]
            if(nums==num2):
                return "true"
            return "false"
        return "Hello Guys"
nums=[1,3,2]
isMonotonic(nums)
