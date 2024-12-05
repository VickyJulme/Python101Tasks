# If a, b and c are three sides of a triangle. Then,
#Herons fromula
# s = (a+b+c)/2
# area = (s*(s-a)*(s-b)*(s-c)) **5

input1 =float(input("Enter First Side   :"))
input2 =float(input("Enter Second Side   :"))
input3 =float(input("Enter Third Side   :"))


areaFinder =(input1 + input2 + input3) /2


area =( areaFinder*(areaFinder - input1)*(areaFinder - input2)*(areaFinder - input3)) **0.5

print(area)