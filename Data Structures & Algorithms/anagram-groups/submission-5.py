class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for data in strs:
            count = [0] * 26
            for s in data:
                count[ord(s) - ord('a')] +=1
            key = tuple(count)
            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(data)
        return list(anagrams.values())