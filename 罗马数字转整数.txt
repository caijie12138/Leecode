class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        list = []
        dic1 = {"": "0",
                "I": "1",
                "IV": "4",
                "V": "5",
                "VI": "6",
                "IX": "9",
                "X": "10",
                "XL": "40",
                "L": "50",
                "XC": "90",
                "C": "100",
                "CD": "400",
                "D": "500",
                "CM": "900",
                "M": "1000"
                }

        for i in s:
            list.append(i)
        list.append("")

        num = 0
        j = 0
        while (j + 1) < len(list):
            if list[j] == "M":
                num += 1000
                j += 1
                continue
            if list[j] == "C" and list[j + 1] == "M":
                num += 900
                j += 2
                continue
            if list[j] == "C" and list[j + 1] == "D":
                num += 400
                j += 2
                continue
            if list[j] == "C" or list[j] == "D":
                num += int(dic1[str(list[j])])
                j += 1
                continue
            if list[j] == "X" and list[j + 1] == "L":
                num += 40
                j += 2
                continue
            if list[j] == "X" and list[j + 1] == "C":
                num += 90
                j += 2
                continue
            if list[j] == "X" or list[j] == "L":
                num += int(dic1[str(list[j])])
                j += 1
                continue
            if list[j] == "I" and list[j + 1] == "X":
                num += 9
                j += 2
                continue
            if list[j] == "I" and list[j + 1] == "V":
                num += 4
                j += 2
                continue
            if list[j] == "I" or list[j] == "V":
                num += int(dic1[str(list[j])])
                j += 1
                continue
        return num
        
