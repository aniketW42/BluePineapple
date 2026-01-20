# Write a function to find nth smart number.
n = 50
prime=[]
for i in range(2, 50):
    j = 2
    flag = True
    while j * j <= i:
        if i % j == 0:
            flag = False
            break
        j += 1
    if flag:
        prime.append(i)
    
print(prime)
count = 1
for i in range(len(prime)):
    for j in range(i+1, len(prime)):
        for k in range(j+1, len(prime)):
            print(f"{count} -> {prime[i]} * {prime[j]} * {prime[k]} = ", prime[i]*prime[j]*prime[k])
            count+=1
            if count > 50:
                break
        if count > 50:
                break
    if count > 50:
                break

# def nth_smart_number(n: int) -> int:
#     pass

