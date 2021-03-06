import numpy as np
import random
from .utils import print_step

def generate_noisy_data(inputMatrix, inputVector, noise_dim_percent, dim, input_data_name):
    #inputMatrix = matrix from rescaledDataframe()
    #inputVector = vector from vector_V()
    #noise_dim_percent = percent of sample to make as noise
    #dim = dimension of the problem aka number of feature in the preprocessing matrix
    #input_data_name = name of dataset
    data_name = "Noisy Data from " + input_data_name
    buffer = str(noise_dim_percent*100)
    print_step("Generating "+data_name+" with "+buffer+"%% of noise")
    noise = inputMatrix 
    noisy_vector = inputVector
    noise_dim = int(len(noisy_vector)*noise_dim_percent)
    rows, columns = inputMatrix.shape
    new_array = np.zeros(dim)
    for i in range(noise_dim):
        for j in range(dim):
            random_index = random.randint(0, rows-1)
            random_binary = random.randint(0, 1)
            new_array[j] = inputMatrix[random_index][j]
        noise = np.vstack([noise, new_array])
        noisy_vector = np.append(noisy_vector, random_binary)
    
    return noise, noisy_vector, data_name

def generate_noisy_feature(inputMatrix, inputVector, noise_feature_number, dim, input_data_name):
    #inputMatrix = matrix from rescaledDataframe()
    #inputVector = vector from vector_V()
    #noise_feature_number = number of noisy feature
    #dim = dimension of the problem aka number of feature in the preprocessing matrix
    #input_data_name = name of dataset
    data_name = "Noisy Feature from " + input_data_name
    buffer = str(noise_feature_number)
    print_step("Generating "+data_name+" with "+buffer+" feature of noise")
    noise = inputMatrix 
    rows, columns = inputMatrix.shape
    
    noisy_vector = inputVector
    for i in range(noise_feature_number):
        new_column = np.zeros(rows)
        for j in range(rows):
            #new_column[j] = random.randint(0, 1)
            new_column[j] = random.random()
        noise = np.insert(noise, -1, new_column, axis=1)
        
    
    return noise, noisy_vector, data_name
    
def noisy_feature_detector(array, dim):
    alert = False
    if(np.any(array>(dim-1))):
        alert = True
    return alert   

def generate_random_data(dim, input_data_name):
    #inputMatrix = matrix from rescaledDataframe()
    #inputVector = vector from vector_V()
    #noise_feature_number = number of noisy feature
    #dim = dimension of the problem aka number of feature in the preprocessing matrix
    #input_data_name = name of dataset
    data_name = "Random data of dim " + str(dim)
    print_step("Generating "+data_name)
    rows = 1000
    random_matrix = np.zeros((rows, dim))
    for i in range(dim):
        new_column = np.ones((rows,1))
        v_vector = np.zeros((rows,1))
        for j in range(rows):
            new_column[j] = random.randint(0, 1)
            if(i == 0):
                v_vector[j] = random.randint(0, 1)
                
        random_matrix = np.insert(random_matrix, -1, new_column, axis=1)
        
    
    return random_matrix, v_vector, data_name