# Loop statement

for i in range(1,10):
    print(i, end=" ")         #1,2,3,4,5,6,7,8,9

for i in range(1, 10, 2):
    print(i)                  #1,3,5,7,9

for i in range(1,10, -2):
    print(i)                  # No output

i = 0
while i < 10:
    print(i)
    i = i+1
print("Done")

i = 10
while i >= 1:
    print(i)
    i = i-1
print("Done")