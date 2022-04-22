import numpy as np
import random
from .german_credit_data import german_credit_data
from .preprocessing_data import rescaledDataframe

def genearate_noisy_data(inputMatrix, inputVector, noise_dim, dim):
    noise = inputMatrix 
    noisy_vector = inputVector
    rows, columns = inputMatrix.shape
    new_array = np.zeros(dim)
    for i in range(noise_dim):
        for j in range(dim):
            random_index = random.randint(0, rows-1)
            random_binary = random.randint(0, 1)
            new_array[j] = inputMatrix[random_index][j]
        noise = np.vstack([noise, new_array])
        noisy_vector = np.append(noisy_vector, random_binary)
    print(noisy_vector)
    return noise, noisy_vector

'''data = german_credit_data()
matrix = rescaledDataframe(data)
genearate_noisy_data(matrix, 5, 48)'''