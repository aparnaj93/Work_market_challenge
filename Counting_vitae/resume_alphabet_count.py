import re
from collections import Counter
import string
import matplotlib.pyplot as plt;

plt.rcdefaults()


def read_file(file_path):
    file_descripter = open(file_path, 'r')
    data = file_descripter.read()

    return data


def analyse_data(data):
    value_lower = []
    value_upper = []
    data = re.sub(r'[\W\s\d]', "", data)
    frequency = Counter(data)
    lower = list(string.ascii_lowercase)
    upper = list(string.ascii_uppercase)
    for c in lower:
        value_lower.append(frequency[c])
    for c in upper:
        value_upper.append(frequency[c])
    plot_stackedbar(value_lower, value_upper, lower)
    plot_parallelbar(value_lower, value_upper, lower, upper)


def plot_stackedbar(value_lower, value_upper, lower):
    f1 = plt.figure(1)
    x_pos = range(len(lower))
    p1 = plt.bar(x_pos, value_lower, color="blue")
    p2 = plt.bar(x_pos, value_upper, color="pink", bottom=value_lower)

    plt.xticks(range(len(lower)), lower)
    plt.legend((p1[0], p2[0]), ('LowerCase', 'UpperCase'))
    plt.savefig("stacked_bar.png")


def plot_parallelbar(value_lower, value_upper, lower, upper):
    f2 = plt.figure(2)
    x_pos1 = range(0, 3 * len(lower), 3)
    x_pos2 = range(1, 3 * len(upper) + 1, 3)
    p1 = plt.bar(x_pos1, value_lower, color="blue")
    p2 = plt.bar(x_pos2, value_upper, color="pink")

    plt.xticks([x + 0.5 for x in x_pos1], lower)
    plt.legend((p1[0], p2[0]), ('LowerCase', 'UpperCase'))
    plt.savefig("parallel_bar.png")


data = read_file("Aparna_Resume_SE.txt")
analyse_data(data)
