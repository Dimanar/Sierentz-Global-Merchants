# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 12:59:51 2022

@author: Okhrimchuk Roman & Maksym Veremchuk
for Sierentz Global Merchants


Test task
"""

import re


class Solution:
    def luckySeq(self, sequence: str) -> str:

        if len(sequence) <= 1:
            return '0'

        splitted_str = re.split(r'[^56]', sequence)
        filtered_rows = list(sorted(filter(lambda x: len(x) > 0 and len(set(x)) == 2, splitted_str),
                                    key=len, reverse=True))

        if filtered_rows:
            return filtered_rows[0]
        else:
            return str(0)

    def luckySeq2(self, sequence: str, lucky=("5", "6")) -> str:

        N = len(sequence)
        if N <= 1:
            return '0'

        i, j = 0, 0
        lucky_nums = []
        while i < N - 1:
            if sequence[i] not in lucky:
                i += 1
                j += 1
            else:
                while j < N:
                    if sequence[j] not in lucky or j == N - 1:
                        if j == N - 1:
                            temp = sequence[i: j + 1]
                        else:
                            temp = sequence[i: j]
                        if len(set(temp)) == 2:
                            lucky_nums.append(temp)
                        i = j
                        break
                    else:
                        j += 1

        # this return does not mean it will return the longest string, in such cases not working properly
        # return max(lucky_nums) if lucky_nums else '0'
        return sorted(lucky_nums, key=len, reverse=True)[0] if lucky_nums else "0"




sol = Solution()
possible_sq = ["4556432455665334", "5555", "5656556565", "565656565656565656565656565656565656565665",
               "234234234565652341234156666666", "235555555564355555556", "3434343438493493493434"]


for sq in possible_sq:
    result1 = sol.luckySeq(sq)
    result2 = sol.luckySeq2(sq)
    print("***** V1 *****")
    print(f' Sequence 1 -> {sq}\n\tlucky 1 -> {result1}')
    print("***** V2 *****")
    print(f' Sequence 1 -> {sq}\n\tlucky 1 -> {result2}')
