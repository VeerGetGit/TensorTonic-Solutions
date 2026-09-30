import numpy as np

def calculate_eigenvalues(matrix: list) -> np.ndarray:
    """
    Returns a sorted NumPy array of real eigenvalues.
    """
    # Write code here
    matrix = np.asarray(matrix, dtype=float)
    eigenvalues= np.linalg.eigvals(matrix) 
    eigenvalues = eigenvalues.real

    return np.sort(eigenvalues)

    """
    np.linalg.eigvals(matrix) --> this gives eigenvalues only
                    OR
    np.linalg.eig(matrix)--> this return eigenvalues and eigenvectors
    so to ignore eigenvector we need to add _

    like:
    eigenvalues, _ = np.linalg.eig(matrix)   # returns both, ignores eigenvectors

    and eigenvalues.real remove imaginary part
    eigenvalues = [5.0 + 0.000000000001j,  2.0 + 0.0j]

    eigenvalues.real = [5.0, 2.0]   # imaginary parts gone
    """