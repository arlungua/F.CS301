def rob(nums):
    n = len(nums)
    
    if n == 0:
        return 0
    if n == 1:
        return nums[0]
    if n == 2:
        return max(nums[0], nums[1])
    
    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    
    for i in range(2, n):
        dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
    
    return dp[-1]

# Example usage
nums1 = [1, 2, 3, 1]
print(rob(nums1))  # Output: 4

nums2 = [2, 7, 9, 3, 1]
print(rob(nums2))  # Output: 12
