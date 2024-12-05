import random

## GENERATE DATASETS FOR EXPERIMENT ### 


def generate_small_random_datasets(num_datasets=50, num_elements=10):
    """
    Generate datasets with specified number of datasets and elements in each.
    
    Args:
    - num_datasets (int): Number of datasets to generate.
    - num_elements (int): Maximum number of elements in each dataset.
    
    Returns:
    - list of lists: Each inner list is a dataset.
    """
    datasets = []
    for _ in range(num_datasets):
        #number_of_elemenets = random.randint(1, num_elements)
        dataset = [random.randint(1, 1000000) for _ in range(num_elements)]
        random.shuffle(dataset)  # Shuffle the dataset
        datasets.append(dataset)
    return datasets

# Example usage
# n = 10  # Change this to the desired number of elements per dataset
# random_small_datasets = generate_small_random_datasets(num_datasets=50, num_elements=n)


def generate_partialy_sorted_small_datasets(num_datasets=50, num_elements=300):
    """
    Generate datasets with specified number of datasets and elements in each.
    
    Args:
    - num_datasets (int): Number of datasets to generate.
    - num_elements (int): Maximum number of elements in each dataset.
    
    Returns:
    - list of lists: Each inner list is a dataset.
    """
    datasets = []
    for _ in range(num_datasets):
        #number_of_elements = random.randint(1, num_elements)
        start_number = random.randint(1, 1000000)
        dataset = [start_number + i for i in range(10)]
        #dataset = list(range(1, main_number + 1))
        ratio_to_swap = random.randint(0, 20)
        n = int(len(dataset) * (ratio_to_swap / 100))
        indices = list(range(len(dataset))) 
        for _ in range(n):
            # Randomly choose two indices to swap
            i, j = random.sample(indices, 2)
            dataset[i], dataset[j] = dataset[j], dataset[i] 
        datasets.append(dataset)
    return datasets

# Example usage
# n = 10  # Change this to the desired number of elements per dataset
# partialy_sorted_small_datasets = generate_partialy_sorted_small_datasets(num_datasets=50, num_elements=n)


def generate_random_large_datasets(num_datasets=50, num_elements=300):
    """
    Generate datasets with specified number of datasets and elements in each.
    
    Args:
    - num_datasets (int): Number of datasets to generate.
    - num_elements (int): Maximum number of elements in each dataset.
    
    Returns:
    - list of lists: Each inner list is a dataset.
    """
    datasets = []
    for _ in range(num_datasets):
        #number_of_elemenets = random.randint(1, num_elements)
        dataset = [random.randint(1, 1000000) for _ in range(num_elements)]
        random.shuffle(dataset)  # Shuffle the dataset
        datasets.append(dataset)
    return datasets

# Example usage
# n = 10000  # Change this to the desired number of elements per dataset
# large_random_datasets = generate_random_large_datasets(num_datasets=50, num_elements=n)

# with open("large_random_datasets.py", "w") as file:
#     file.write(f"large_random_datasets = {large_random_datasets}")


def generate_partialy_sorted_large_datasets(num_datasets=50, num_elements=300):
    """
    Generate datasets with specified number of datasets and elements in each.
    
    Args:
    - num_datasets (int): Number of datasets to generate.
    - num_elements (int): Maximum number of elements in each dataset.
    
    Returns:
    - list of lists: Each inner list is a dataset.
    """
    datasets = []
    for _ in range(num_datasets):
        #number_of_elements = random.randint(1, num_elements)
        start_number = random.randint(1, 1000000)
        dataset = [start_number + i for i in range(10000)]
        #dataset = list(range(1, main_number + 1))
        ratio_to_swap = random.randint(0, 20)
        n = int(len(dataset) * (ratio_to_swap / 100))
        indices = list(range(len(dataset))) 
        for _ in range(n):
            # Randomly choose two indices to swap
            i, j = random.sample(indices, 2)
            dataset[i], dataset[j] = dataset[j], dataset[i] 
        datasets.append(dataset)
    return datasets

# Example usage
# n = 10000  
# partialy_sorted_datasets_large = generate_partialy_sorted_large_datasets(num_datasets=50, num_elements=n)

# with open("partialy_sorted_datasets_large.py", "w") as file:
#     file.write(f"partialy_sorted_datasets = {partialy_sorted_datasets_large}")

# print("Datasets saved to 'partialy_sorted_large_datasets.py'")