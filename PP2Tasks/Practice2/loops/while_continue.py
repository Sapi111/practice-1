#1
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
#2
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)
#3
nums = [2, -1, 4, -3, 6]
i = 0

while i < len(nums):
    if nums[i] < 0:
        i += 1
        continue
    print(nums[i])
    i += 1
#4
words = ["hi", "skip", "hello"]
i = 0

while i < len(words):
    if words[i] == "skip":
        i += 1
        continue
    print(words[i])
    i += 1
#5
while True:
    x = input()
    if x == "no":
        continue
    if x == "stop":
        break
    print(x)