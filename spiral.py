n = int(input())
d = [[0 for i in range(n)]for j in range(n)]
k = 0
for i in range(0, int((n/2 + n % 2)+1), 1):
    k += 1
    for j in range(k-1, (n-(k-1))):
        if i == 0:
            d[i][j]=d[i][j]+(j+1)
        else:
            d[i][j] = d[i][k-2] + j - (k-2)
        if j == (n-(k-1)-1):
            for i in range(k,(n-(k-1)),1):
                if j == n-1:
                    d[i][j] = d[k-1][j] + i
                else:
                    d[i][j]=d[k-1][j] + (i-(k-1))
                if i == (n-(k-1)-1):
                    for j in range (n-(2+(k-1)),k-2,-1):
                        d[i][j]=d[n-k][n-k]+(i-j)
                        if j == k-1:
                            if int((n/2 + n % 2)-1) == (k - 1):
                                break
                            else:
                                for i in range(n-(2+(k-1)), k-1, -1):
                                    d[i][j]=d[n-k][k-1]+((n-k)-i)
for i in d:
    for j in i:
        print(j, end = ' ')
    print()