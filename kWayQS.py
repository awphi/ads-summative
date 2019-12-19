import sys

def read_input(filename):
    A = []
    
    try:
        myfile = open(filename, 'r')
    except OSError:
        print('cannot open', filename)
        sys.exit(0)
        
    for line in myfile:
        A = A + [int(line.strip())]
    myfile.close()
    return A


def insertionsort(A):
    for j in range(1, len(A)):
        x = A[j]
        i = j - 1
        while (i >= 0) and (A[i] > x):
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = x
    return A
   
    
def partition(A, k):
    n = len(A)
    piv = n - k
    pivots = A[piv:piv + k]
    for pivot in pivots:
        left = []
        right = []
        for j in A:
            if(j > pivot):
                right.append(j)
            elif(pivot > j):
                left.append(j)
        A = left + [pivot] + right

    B = []
    runner = []
    for a in A:
        if(a in pivots):
            if(len(runner) > 0):
                B.append(runner)
            B.append([a])
            runner = []
        else:
            runner.append(a)
    B.append(runner)
    return B


    

def quicksort(A, k):
    parts = partition(A, k)
    for i in range(0, len(parts)):
        n = len(parts[i])
        
        if(n <= 1):
            continue;
        elif(n < 2 * k):
            parts[i] = insertionsort(parts[i])
        else:
            parts[i] = quicksort(parts[i], k)

    return sum(parts, [])
    

def main():
    k = int(sys.argv[1])
    filename = sys.argv[2]
    A = read_input(filename)
    print(quicksort(A,k))
    
if __name__ == "__main__":
    main()