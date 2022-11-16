'''https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/description/'''

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        
        arr = preorder.split(",")
        slot = 1
        for i in arr:
            if slot == 0:
                return False
            
            if i == "#":
                slot -= 1
            
            else:
                slot += 1
        return slot == 0