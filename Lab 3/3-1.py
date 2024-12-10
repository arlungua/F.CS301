class Solution:
    def majorityElement(self, nums):
        def majority_helper(left, right):
            if left == right: 
                return nums[left]
            
            mid = (left + right) // 2
            
            left_majority = majority_helper(left, mid)
            right_majority = majority_helper(mid + 1, right)
  
            if left_majority == right_majority:
                return left_majority
            
            left_count = sum(1 for i in range(left, right + 1) if nums[i] == left_majority)
            right_count = sum(1 for i in range(left, right + 1) if nums[i] == right_majority)
          
            return left_majority if left_count > right_count else right_majority

        return majority_helper(0, len(nums) - 1)

solution = Solution()
nums = [2, 2, 1, 1, 1, 2, 2]
print(solution.majorityElement(nums)) 
