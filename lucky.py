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
        filtered_rows = list(sorted(filter(lambda x: len(x) > 0, splitted_str), key=len, reverse=True))

        if filtered_rows:
            return filtered_rows[0]
        else:
            return str(0)

    # def luckySeq2(self, sequence: str) -> str:
    #
    #     if len(sequence) <= 1:
    #         return '0'
    #
    #     splitted_str = re.split(r'[^56]', sequence)
    #     filtered_rows = list(sorted(filter(lambda x: len(x) > 0, splitted_str), key=len, reverse=True))
    #
    #     if filtered_rows:
    #         return filtered_rows[0]
    #     else:
    #         return str(0)


sol = Solution()
possible_sq = ["4556432455665334", "5656556565", "565656565656565656565656565656565656565665",
               "234234234565652341234156666666", "235555555564355555556", "3434343438493493493434"]

print("***** V1 *****")
for sq in possible_sq:
    result = sol.luckySeq(sq)
    print(f' Sequence 1 -> {sq}\n\tlucky 1 -> {result}\n')

# print("***** V2 *****")
# for sq in possible_sq:
#     result = sol.luckySeq2(sq)
#     print(f' Sequence 1 -> {sq}\n\tlucky 1 -> {result}\n')
