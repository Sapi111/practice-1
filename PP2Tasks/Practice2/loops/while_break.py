#1
i = 1
while i <= 10:
    if i == 5:
        break
    print(i)
    i += 1
#2
while True:
    x = int(input())
    if x == 0:
        break
    print(x)
#3
nums = [1, 3, 5, 7]
i = 0

while i < len(nums):
    if nums[i] == 5:
        break
    print(nums[i])
    i += 1
#4
while True:
    password = input()
    if password == "1234":
        break
#5
i = 10
while True:
    print(i)
    if i == 1:
        break
    i -= 1