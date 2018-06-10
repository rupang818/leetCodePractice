class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        if len(candidates) is 1:
            if target % candidates[0] is 0:
                return [[candidates[0]]*int(target/candidates[0])]
            else:
                return []
        else:
            allCombos=[]
            if target % candidates[0] is 0: 
                allCombos+=[[candidates[0]]*int(target/candidates[0])]
            selfRepeatCount=0
            while candidates[0]*selfRepeatCount < target:
                repeatArr = [candidates[0]]*selfRepeatCount
                subCombos = self.combinationSum(candidates[1:],target-(candidates[0]*selfRepeatCount))
                for x in subCombos:
                    if len(repeatArr) > 0:
                        x+=repeatArr
                    allCombos.append(x)
                selfRepeatCount+=1
            return allCombos
