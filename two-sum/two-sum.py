class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        
        for i,val in enumerate(nums):
            if target-val not in dictionary:
                dictionary[val] = i
            else:
                return i,dictionary[target-val]
        