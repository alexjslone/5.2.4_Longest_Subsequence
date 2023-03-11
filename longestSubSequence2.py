#first_sequence = [2,7, 8, 3]
#second_sequence= [5,2, 8, 7]
#twoDimList= []

def lcs2(first_sequence, second_sequence):
#need to initialize a 2D array to store all the values
    twoDimList =  [[0 for j in range(len(second_sequence)+1)] for i in range(len(first_sequence)+1)]
    for i in range(len(first_sequence)-1, -1, -1):
        for j in range(len(second_sequence)-1, -1, -1):
            if first_sequence[i] == second_sequence[j]:
                twoDimList[i][j]= twoDimList[i+1][j+1]+1
            else: 
                twoDimList[i][j]= max(twoDimList[i+1][j], twoDimList[i][j+1])
    return twoDimList[0][0]

#print(lcs2(first_sequence, second_sequence))


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    print(lcs2(a, b))
