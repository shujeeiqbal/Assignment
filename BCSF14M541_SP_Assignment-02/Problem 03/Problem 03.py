"""
Shujee Iqbal
BCSF14M541
System Programming
Task 3: 2x2 matrix in 8x8
"""

def matrix8x8(): 
    matrix = [[1, 2, 3, 4, 5, 6, 7, 8], [6, 5, 4, 4, 3, 7, 1, 2], [3, 4, 5, 6, 4, 7, 8, 9], [2, 2, 2, 2, 2, 2, 2, 2], [4, 1, 5, 1, 5, 1, 5, 3], [3, 5, 7, 2, 5, 6, 4, 6], [3, 4, 5, 6, 7, 4, 5, 6], [4, 5, 1, 3, 4, 5, 6, 7]]
    return matrix

def main():
    matrix8 = matrix8x8()
    
    matrix2 = []

    for n in [0,1]:
        row = []
        for m in [0,1]:
            row_in = input("Enter an element ({0},{1}): ".format(n,m))
            row.append(int(row_in))        
        matrix2.append(row)

    for rows8 in range(0, 7):
        for col8 in range(0, 7):
            if matrix8[rows8][col8] == matrix2[0][0]:
                if matrix8[rows8][col8+1] == matrix2[0][1]:
                    if matrix8[rows8+1][col8] == matrix2[1][0]:
                        if matrix8[rows8+1][col8+1] == matrix2[1][1]:
                            print("2x2 matrix found in 8x8 at starting point ({0}, {1}).".format(rows8, col8))
                            exit()

    print("2x2 matrix not found.")

if __name__ == "__main__":
    main()
