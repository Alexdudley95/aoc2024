totalDistance = 0
remainder = 0
leftList = list()
rightList = list()
for line in open('aocd2024/day1/input.txt'):
  num1, num2 = line.split('   ')
  leftList.append(int(num1))
  rightList.append(int(num2))

leftList.sort()
rightList.sort()

for i in range(len(leftList)):
  if leftList[i] < rightList[i]:
    print(leftList[i])
    remainder = rightList[i] - leftList[i]
    totalDistance += remainder
  elif rightList[i] < leftList[i]:
    print("RIGHT")
    remainder = leftList[i] - rightList[i]
    totalDistance += remainder


print(totalDistance)