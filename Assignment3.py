import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

def generate_random_numbers():
    np.random.seed(25)
    num_numbers = 100
    random_numbers = np.random.normal(0, 1, num_numbers)
    for _ in tqdm(range(num_numbers), desc="Generating data", unit="number"):
        np.random.normal()

    return random_numbers

def plot_data(random_numbers):
    plt.plot(random_numbers, linestyle='-', color='b', label='Random Numbers')
    plt.show()


def main():
    random_numbers = generate_random_numbers()
    print("Generated data:")
    input("Press Enter to proceed.")
    graf = plot_data(random_numbers)

main()
