import csv
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import numpy as np
import re
from math import ceil, floor, gcd

FILE_NAME="../data.csv"
SAVE_PATH="../plots/"
CSV_DELIMITER='\t'
T_MIN=1
T_MAX=7
T_NUM=(T_MAX-T_MIN)+1
LB_DELTA_START=3
UB_DELTA_START=4
SUM_DELTA_START=5
SHIFT=3
NUM_BINS=30
P = 0
V = 1
G = 2

def condition_all(row):
    return True

def condition_g_equals_v(row):
    return int(row[V]) == int(row[G])


def condition_binary(row):
    return int(row[V]) == 2

"""
PLOT HELPER FUNCTIONS
"""
def create_plot(title, condition=None):
    if not callable(condition):
        return
    data_x = []
    data_y = []
    with open(FILE_NAME, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=CSV_DELIMITER)
        for row in reader:
            if condition(row):
                for t in range(T_MIN, T_MAX):
                    current_t = SUM_DELTA_START + (t-1)*SHIFT
                    next_t    = SUM_DELTA_START + (t)*SHIFT
                    if len(row) > next_t: #sometimes this is required since the sequence might not have all run lengths.
                        current_count = int(row[current_t])
                        next_count = int(row[next_t])
                        if (current_count > 0) and (current_count > next_count):
                            data_x.append(t)
                            data_y.append(next_count/current_count)

        title = "Run ratio with actual count ({})".format(title)
        plt.title(title)
        #plt.scatter(data_x, data_y)
        plt.hist2d(data_x, data_y, bins=50, cmap=plt.cm.jet, cmin=1)
        save_name = SAVE_PATH + re.sub('[^A-Za-z0-9]+', '', title)
        plt.savefig(save_name, bbox_inches='tight')
        plt.savefig(save_name, bbox_inches='tight', transparent=True)
        plt.clf()


def create_all():
    create_plot("all", condition_all)
    create_plot("g = v", condition_g_equals_v)
    create_plot("binary", condition_binary)


if __name__ == "__main__":
    create_all()
