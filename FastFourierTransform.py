import numpy as np
from scipy.linalg import eig, solve
from scipy.fft import fft, ifft

# Eigenvalues and Eigenvectors
matrix = np.array([[4, 2], [3, 1]])
b = np.array([10,8])
eigenvalues, eigenvectors = eig(matrix)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)
answer = solve(matrix, b)
print("linear eq sol", answer)
# FFT and IFFT
data = np.array([1, 2, 3, 4])
fft_result = fft(data)
ifft_result = ifft(fft_result)
print("FFT Result:", fft_result)
print("IFFT Result:", ifft_result)

# Simple verification
print("Original Data:", data)
print("Recovered Data:", ifft_result.real)
