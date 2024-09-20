import numpy as np

def get_matrix_input():
    """Function to take matrix input from the user."""
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    print("Enter the matrix elements row-wise (separated by spaces):")
    matrix = []
    for _ in range(rows):
        row = list(map(float, input().split()))
        if len(row) != cols:
            print(f"Error: Expected {cols} columns, but got {len(row)}.")
            return None
        matrix.append(row)
    return np.array(matrix)

def matrix_operations():
    """Function to perform matrix operations based on user input."""
    print("Matrix Operations Library")
    
    while True:
        print("\nMenu:")
        print("1. Matrix Addition")
        print("2. Matrix Subtraction")
        print("3. Matrix Multiplication")
        print("4. Matrix Transpose")
        print("5. Matrix Determinant")
        print("6. Matrix Inverse")
        print("7. Exit")
        
        choice = input("\nSelect an operation (1-7): ")
        
        if choice == '1':
            print("\nMatrix Addition")
            print("Enter first matrix:")
            matrix1 = get_matrix_input()
            print("Enter second matrix:")
            matrix2 = get_matrix_input()
            if matrix1 is not None and matrix2 is not None:
                if matrix1.shape == matrix2.shape:
                    print("Result of Addition:\n", matrix1 + matrix2)
                else:
                    print("Error: Matrices must be of the same size for addition.")
        
        elif choice == '2':
            print("\nMatrix Subtraction")
            print("Enter first matrix:")
            matrix1 = get_matrix_input()
            print("Enter second matrix:")
            matrix2 = get_matrix_input()
            if matrix1 is not None and matrix2 is not None:
                if matrix1.shape == matrix2.shape:
                    print("Result of Subtraction:\n", matrix1 - matrix2)
                else:
                    print("Error: Matrices must be of the same size for subtraction.")
        
        elif choice == '3':
            print("\nMatrix Multiplication")
            print("Enter first matrix:")
            matrix1 = get_matrix_input()
            print("Enter second matrix:")
            matrix2 = get_matrix_input()
            if matrix1 is not None and matrix2 is not None:
                if matrix1.shape[1] == matrix2.shape[0]:
                    print("Result of Multiplication:\n", np.dot(matrix1, matrix2))
                else:
                    print("Error: Number of columns in the first matrix must equal the number of rows in the second matrix.")
        
        elif choice == '4':
            print("\nMatrix Transpose")
            print("Enter a matrix:")
            matrix = get_matrix_input()
            if matrix is not None:
                print("Transpose of the matrix:\n", np.transpose(matrix))
        
        elif choice == '5':
            print("\nMatrix Determinant")
            print("Enter a square matrix:")
            matrix = get_matrix_input()
            if matrix is not None:
                if matrix.shape[0] == matrix.shape[1]:
                    print("Determinant of the matrix:", np.linalg.det(matrix))
                else:
                    print("Error: Matrix must be square (n x n) to calculate the determinant.")
        
        elif choice == '6':
            print("\nMatrix Inverse")
            print("Enter a square matrix:")
            matrix = get_matrix_input()
            if matrix is not None:
                if matrix.shape[0] == matrix.shape[1]:
                    try:
                        print("Inverse of the matrix:\n", np.linalg.inv(matrix))
                    except np.linalg.LinAlgError:
                        print("Error: Matrix is singular and cannot be inverted.")
                else:
                    print("Error: Matrix must be square (n x n) to calculate the inverse.")
        
        elif choice == '7':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice! Please select a valid operation (1-7).")

if __name__ == "__main__":
    matrix_operations()
