import math
AB = int(input("enter AB :"))
BC = int(input("enter BC :"))
result = math.degrees(math.atan(AB/BC))
degree = u"\u00b0"
print(int(round(result)))
print degree

