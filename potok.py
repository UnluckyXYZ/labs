import threading

def matrix_multiply(A, B, result, row, col):
    total = 0
    for i in range(len(A[0])):
        total += A[row][i] * B[i][col]
    result[row][col] = total

def multiply_matrices(A, B):
    if len(A[0]) != len(B):
        raise ValueError("Number of columns in A must be equal to the number of rows in B")
    
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    threads = []
    
    for i in range(len(A)):
        for j in range(len(B[0])):
            thread = threading.Thread(target=matrix_multiply, args=(A, B, result, i, j))
            thread.start()
            threads.append(thread)
    
    for thread in threads:
        thread.join()
    
    return result

# Example usage
A = [[1, 2, 3],
     [4, 5, 6]]

B = [[7, 8],
     [9, 10],
     [11, 12]]

result = multiply_matrices(A, B)
for row in result:
    print(row)