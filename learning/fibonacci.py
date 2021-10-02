if __name__ == '__main__':
    n = int(input())
    if n == 0:
        print(0)
    else:
        n1, n2 = 0, 1
        i = 1
        while n2 <= n:
            if n2 == n:
                print(i)
                break
            n1, n2 = n2, n1 + n2
            i += 1
        else:
            print(-1)
