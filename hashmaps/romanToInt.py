class Solution:
    def romanToInt(self, s: str) -> int:
        # use the tuple (s) for keys in a hashmap
        # equate them to the numerical value they represent for math
        roman_values = s

        print(roman_values)
        val_list = [1, 5, 10, 50, 100, 500, 1000]
        keys = ("I", "V", "X", "L", "C", "D", "M")
        values = tuple(val_list)
        # use a dictionary comprehension to set keys and values to a dictionary
        my_dict = {k: v for k, v in zip(keys, values)}

        print(my_dict)
