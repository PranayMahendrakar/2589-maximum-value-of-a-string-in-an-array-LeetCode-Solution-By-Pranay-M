class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        result = 0
        for s in strs:
            if s.isdigit():
                result = max(result, int(s))
            else:
                result = max(result, len(s))
        return result