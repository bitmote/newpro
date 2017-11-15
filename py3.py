def largestNumber( nums):
    # write your code here
    # sort
    for i in range(len(nums) - 1):
        for j in range(len(nums) - 1 - i):
            if not cmp(nums[j], nums[j + 1]):
                temp = nums[j + 1]
                nums[j + 1] = nums[j]
                nums[j] = temp
    strnum = ''
    for num in nums:
        strnum += str(num)
    if int(strnum) == 0:
        return '0'
    return strnum


def cmp( m, n):
    resm = int(str(m) + str(n))
    resn = int(str(n) + str(m))
    if resm >= resn:
        return True
    else:
        return False


nums = [1,20,23,4,8]

print  largestNumber(nums)

