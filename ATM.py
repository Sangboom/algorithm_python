n = int(input())
A=input()
A_list = A.split()
A_list = list(map(int, A_list))
A_list.sort()
sum = 0
total = 0
for i in range(n):
    sum += A_list[i]
    total += sum
print(total)