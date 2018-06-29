class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phoneDict = {"2":["a","b","c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"], "5": ["j", "k", "l"], "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"], "8": ["t","u","v"], "9": ["w","x","y","z"]}
        # Use memoization, recursive DFS
        if not digits:
            return []
        kc = phoneDict
        
        def letterComboMemo(digits, knownCombo):
            if digits in knownCombo:
                return knownCombo[digits]
            
            subCombos=[]
            for x in knownCombo[digits[0]]: #2 -> a,b,c
                subCombos += [x + subCombo for subCombo in letterComboMemo(digits[1:], knownCombo)]
            
            knownCombo[digits] = subCombos
            return subCombos
        
        return letterComboMemo(digits, kc)
