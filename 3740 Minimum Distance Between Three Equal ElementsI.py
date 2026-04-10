class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        tupleDic = dict()
        ans = len(nums) + 1

        for idx, i in enumerate(nums):
            if i in tupleDic:
                tupleDic[i].append(idx)
            else:
                tupleDic[i] = [idx]
                
            if len(tupleDic[i]) >= 3 and tupleDic[i][-1] - tupleDic[i][-3] < ans:
                ans = tupleDic[i][-1] - tupleDic[i][-3]

        return -1 if ans == len(nums) + 1 else 2 * ans