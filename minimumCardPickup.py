#Minimum Card pickup problem
#https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up
class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        dic = {}
        lowest = 1000000
        for i, card in enumerate(cards):
            if card in dic:
                value = dic.get(card)
                lowest = min(i - value + 1, lowest)
            dic[card] = i
        
        return lowest if lowest != 1000000 else -1
