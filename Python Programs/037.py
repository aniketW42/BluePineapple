# Write a function to sort a given mixed list of integers and strings.

def sort_list(li):
    
    for i in range(len(li)):
        min = i
        for j in range(len(li)-i):
            if(str(li[min])>str(li[j+i])):
                min = j+i
        ele = li[min]
        del li[min]
        li.insert(i,ele)

    return li

print(sort_list([5,6,1,3,'a','s','z',4,'r']))
print(sort_list(['pizza','sushi','wadapav','noodles','burger']))
print(sort_list([2,5,7,9,6,4,3,1]))