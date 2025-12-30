#Write a function to sort a list of elements using comb sort.

def comb_sort(li):
    gap = len(li)//1.3

    while gap>=1:
        for i in range(len(li)):
            j = int(i + gap)

            if j >= len(li) : 
                break

            if li[i] > li[j]:
                li[i] , li[j] = li[j], li[i]

        gap = gap//1.3

    return


li = [5,3,9,6,0,3,6,1]

comb_sort(li)

print(li)

