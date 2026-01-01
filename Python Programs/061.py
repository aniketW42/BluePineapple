#Write a python function to count number of substrings with the sum of digits equal to their length.

def count_substr_with_sum_equals_len(string):
    count = 0
    for i in range(len(string)):
        sum = 0
        for j in range(i, len(string)):
            sum = sum + int(string[j])
            if sum== j - i + 1:
                # print(string[i:j+1])
                count+=1

    return count

print(count_substr_with_sum_equals_len("003112"))
print(count_substr_with_sum_equals_len("111111"))
print(count_substr_with_sum_equals_len("123456"))



            
