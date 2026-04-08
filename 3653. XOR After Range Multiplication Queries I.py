class Solution:
    def bitwiseXor(self, nums: List[int], i:int=0 )-> int:
        if i+1 == len(nums):
            return nums[i]^0
        return nums[i]^self.bitwiseXor(nums,i+1)

    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        for (l,r,k,v) in queries:
            idx=l
            while idx<=r:
                nums[idx] = (nums[idx] * v) % (10**9 + 7)
                idx += k
        
        return self.bitwiseXor(nums) 
        

