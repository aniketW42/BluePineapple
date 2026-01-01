# Write a function to find eulerian number a(n, m).

''' Eulerian numbers satisfy: a(n,m)=(n-m)a(n-1,m-1)+(m+1)a(n-1,m) '''

def eulerian_number(n: int, m: int) -> int:

    if m < 0 or m >= n:
        return 0

    if n == 1:
        return 1 if m == 0 else 0

    return (n - m) * eulerian_number(n - 1, m - 1) + (m + 1) * eulerian_number(n - 1, m)


if __name__ == '__main__':
    print(eulerian_number(3,1))
    print(eulerian_number(4,2))
    print(eulerian_number(5,3))

    
