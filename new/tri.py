nums = input().split(" ")
for z in nums:
    z = int(z)
if eval(nums[0]+nums[1]) == nums[2]:
    print("%s+%s=%s" % (str[0], str[1], str[2]))
if eval(nums[0]-nums[1]) == nums[2]:
    print("%s-%s=%s" % (str[0], str[1], str[2]))
if eval(nums[0]*nums[1]) == nums[2]:
    print("%s*%s=%s" % (str[0], str[1], str[2]))
if eval(nums[0]//nums[1]) == nums[2]:
    print("%s/%s=%s" % (str[0], str[1], str[2]))
