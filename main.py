import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy import stats


def normal_distribution():
    mean = [-1, -1]
    cov = [[1, 0.5], [0.5, 2]]
    x, y = np.random.multivariate_normal(mean, cov, 100).T
    calculate_and_print_correlation(x, y)
    plot_data(x, y, ['x', 'y'])


def test_data():
    protein, oil = read_data_from_file()
    calculate_and_print_correlation(protein, oil)
    plot_data(protein, oil, ['protein', 'oil'])


def calculate_and_print_correlation(x, y):
    pearsonr = sp.stats.pearsonr(x, y)
    print('r: ', pearsonr[0])
    print('p-value: ', pearsonr[1])


def plot_data(x, y, labels):
    plt.plot(x, y, 'x')
    plt.xlabel(labels[0])
    plt.ylabel(labels[1])
    plt.axis('equal')
    plt.show()


def read_data_from_file():
    file = open("01-soybean-data.txt")
    protein = []
    oil = []
    for line in file:
        splitted_line = line.split()
        protein.append(float(splitted_line[9]))
        oil.append(float(splitted_line[10]))
    file.close()
    return np.array(protein), np.array(oil)


if __name__ == '__main__':
    normal_distribution()
    test_data()
