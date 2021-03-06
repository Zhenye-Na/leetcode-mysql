class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """
    def __init__(self):
        self.int2letter = {
            "0": [" "],
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

    def letterCombinations(self, digits):
        # write your code here
        if not digits or len(digits) == 0 or "1" in digits:
            return []

        combinations = []
        self.digits = digits
        self._find_combinations(combinations, 0, "")
        return combinations

    def _find_combinations(self, combinations, idx, tmp):
        if len(tmp) == len(self.digits):
            combinations.append(tmp)
            return

        for char in self.int2letter[self.digits[idx]]:
            self._find_combinations(combinations, idx + 1, tmp + char)
