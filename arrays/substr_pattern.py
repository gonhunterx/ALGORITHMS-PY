class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # get the entire length of the string
        n = len(s)
        # for loop that starts at 1 because the minimum size of the substring
        # since range is not inclusive of the end num we add 1
        for i in range(1, n // 2 + 1):
            # checking if the len can divide
            if n % i == 0:
                # creating a substring that goes up to i
                substring = s[:i]
                # checking if repeating the substring a certain num
                # of times will equal the original string
                if substring * (n // i) == s:
                    return True
        # if none of the conditions are possible return False
        return False
