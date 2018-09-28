class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        list = []
        dic1={"0":"",
             "1":"I",
             "2":"II",
             "3":"III",
             "4":"IV",
             "5":"V",
             "6":"VI",
             "7":"VII",
             "8":"VIII",
             "9":"IX",
             "10":"X",
             "20":"XX",
             "30":"XXX",
             "40":"XL",
             "50":"L",
             "60":"LX",
             "70":"LXX",
             "80":"LXXX",
             "90":"XC",
             "100":"C",
             "200":"CC",
             "300":"CCC",
             "400":"CD",
             "500":"D",
             "600":"DC",
             "700":"DCC",
             "800":"DCCC",
             "900":"CM",
             "1000":"M",
             "2000":"MM",
             "3000":"MMM"
            }

        for i in str(num):
            list.append(i)
        if len(list) == 1:
            return dic1[str(list[0])]
        elif len(list) == 2:
            return dic1[str(int(list[0])*10)]+dic1[str(list[1])]
        elif len(list) == 3:
            return dic1[str(int(list[0])*100)]+dic1[str(int(list[1])*10)]+dic1[str(list[2])]
        elif len(list) == 4:
            return dic1[str(int(list[0])*1000)]+dic1[str(int(list[1])*100)]+dic1[str(int(list[2])*10)]+dic1[str(list[3])]



        
