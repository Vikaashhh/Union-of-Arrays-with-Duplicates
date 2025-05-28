class Solution:    
    def findUnion(self, a, b):
        # Ek line mein: a aur b ko milaake set banao aur uska length return karo
        return len(set(a + b))
