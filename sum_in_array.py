# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 12:59:22 2022

@author: Okhrimchuk Roman & Maksym Veremchuk
for Sierentz Global Merchants


Test task
"""

from typing import List

class Solution:
    def SumInArray(self, nums: List[int], target: int) -> List[int]:
        """ variation for not sorted array """
        diff_dict = dict()
        for num in nums:

            diff = target - num

            if num in diff_dict:
                return [diff_dict[num], num]

            if diff not in diff_dict:
                diff_dict[diff] = num

        return [-1]

    def SumInArray2(self, nums: List[int], target: int) -> List[int]:
        """ variation for sorted array """
        first, last = 0, len(nums) - 1
        while first != last and nums[first] + nums[last] != target:
            if nums[first] + nums[last] < target:
                first += 1
            else:
                last -= 1

        if first != last:
            return [nums[first], nums[last]]
        else:
            return [-1]


sol = Solution()
result1 = sol.SumInArray([-3, 1, 4, 6], 7)
print(result1, '\n')

result2 = sol.SumInArray([2, 7, 11, 15], 9)
print(result2, '\n')

result3 = sol.SumInArray([-3, 1, 4, 6, 3], 7)
print(result3, '\n')

result3 = sol.SumInArray([-3, 1, 4, 6, 3], 20)
print(result3, '\n')

print('----'*9)

result1 = sol.SumInArray2([-3, 1, 4, 6], 7)
print(result1, '\n')

result2 = sol.SumInArray2([2, 7, 11, 15], 9)
print(result2, '\n')

result3 = sol.SumInArray2([-3, 1, 3, 4, 6], 7)
print(result3, '\n')

result3 = sol.SumInArray2([-3, 1, 3, 4, 6], 20)
print(result3, '\n')