import csv
import matplotlib.pyplot as plt
import numpy as np
import re
from math import ceil, floor

FILE_NAME="../../experiments/tuples/tuples.csv"
CSV_DELIMITER='\t'
T_MIN=2
T_MAX=7
T_NUM=(T_MAX-T_MIN)+1
LB_DELTA_START=3
UB_DELTA_START=5
SHIFT=4
NUM_BINS=30
P = 0
V = 1
G = 2


"""
BOUND COMPUTATIONS
"""
def tuple_lb(row, t):
    g, p, v = int(row[G]), int(row[P]), int(row[V])
    q = floor(p / (pow(g, t - 1)))
    return  pow(floor(g / v), t - 1) * floor(q / v)

def tuple_ub(row, t):
    g, p, v = int(row[G]), int(row[P]), int(row[V])
    q = floor(p / (pow(g, t - 1)))
    return pow(ceil(g / v), t - 1) * (floor(q / v) + 1)

def tuple_elb(row, t):
    g, p, v = int(row[G]), int(row[P]), int(row[V])
    q = floor(p / (pow(g, t - 1)))
    return max((p/v) * ((g-v)/(g*v))**(t-1), tuple_lb(row,t))

def tuple_eub(row, t):
    g, p, v = int(row[G]), int(row[P]), int(row[V])
    q = floor(p / (pow(g, t - 1)))
    return min((p/v) * ((g+v)/(g*v))**(t-1), tuple_ub(row,t))

"""
CONDITION HELPER FUNCTIONS
"""
def condition_all_lb(data, row, pos, t):
    d = int(row[pos])
    data.append(d - tuple_lb(row,t))

def condition_all_elb(data, row, pos, t):
    d = int(row[pos])
    data.append(d - tuple_elb(row,t))

def condition_all_ub(data, row, pos, t):
    d = int(row[pos])
    data.append(tuple_ub(row,t) - d)

def condition_all_eub(data, row, pos, t):
    d = int(row[pos])
    data.append(tuple_eub(row,t) - d)

def condition_greater_than_zero(data, row, pos, t):
    d = int(row[pos])
    lb = tuple_lb(row,t)
    if d > 0:
        data.append(d - lb)

def condition_greater_than_zero_env(data, row, pos, t):
    d = int(row[pos])
    if d > 0:
        data.append(d - tuple_elb(row,t))

def condition_g_equals_v(data, row, pos, t):
    if int(row[V]) == int(row[G]):
        data.append(tuple_ub(row,t) - int(row[pos]))

def condition_g_equals_v_env(data, row, pos, t):
    if int(row[V]) == int(row[G]):
        data.append(tuple_eub(row,t) - int(row[pos]))

"""
PLOT HELPER FUNCTIONS
"""
def create_histogram(t, bound_start, title, condition=None):
    if not callable(condition):
        return
    data = []
    with open(FILE_NAME, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=CSV_DELIMITER)
        pos = (t-T_MIN)*SHIFT + bound_start
        for row in reader:
            condition(data, row, pos, t)

    bins = list(range(NUM_BINS))
    h_data = [ data.count(i) for i in bins ]
    title += " t = {} with {:.2f}% outliers".format(t, (100 - sum(h_data)/len(data)*100))
    plt.bar(bins, h_data)
    plt.title(title)
    save_name = re.sub('[^A-Za-z0-9]+', '', title)
    plt.savefig(save_name, bbox_inches='tight')
    #plt.savefig(save_name, bbox_inches='tight', transparent=True)
    plt.clf()

def add_labels(fig, ax):
    for bar in fig:
        height = bar.get_height()
        ax.annotate("{:.1f}%".format(height),
                    xy=(bar.get_x() + bar.get_width() / 2, height/2),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', rotation=90)

def create_accuracy(bound_start, title, label1, label2, condition1=None, condition2=None):
    if not callable(condition1):
        return
    if not callable(condition2):
        return

    acc1 = [None]*T_NUM
    acc2 = [None]*T_NUM
    with open(FILE_NAME, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=CSV_DELIMITER)
        bins = list(range(T_MIN, T_MAX+1))
        for t in bins:
            data1 = []
            data2 = []
            i = t-T_MIN
            pos = i*SHIFT + bound_start
            csvfile.seek(0)
            for row in reader:
                condition1(data1, row, pos, t)
                condition2(data2, row, pos, t)
            acc1[i] = data1.count(0)/len(data1)*100
            acc2[i] = data2.count(0)/len(data2)*100
    fig = plt.figure()
    ax = fig.add_subplot(111)
    width = 0.20
    f1 = ax.bar([b-width for b in bins], acc1, width*2, label=label1)
    f2 = ax.bar([b+width for b in bins], acc2, width*2, label=label2)
    ax.set_ylabel("Bound Accuraty (%)")
    ax.set_xlabel("t")
    ax.set_title(title)
    ax.legend()
    add_labels(f1, ax)
    add_labels(f2, ax)
    save_name = re.sub('[^A-Za-z0-9]+', '', title)
    #plt.savefig(save_name, bbox_inches='tight', transparent=True)
    plt.savefig(save_name, bbox_inches='tight')
    plt.clf()


def create_all():
    for t in range(T_MIN, T_MAX+1):
        create_histogram(t, LB_DELTA_START, "LB, ", condition_all_lb)
        create_histogram(t, LB_DELTA_START, "LB (> 0), ", condition_greater_than_zero)
        create_histogram(t, UB_DELTA_START, "UB, ", condition_all_ub)
        create_histogram(t, UB_DELTA_START, "UB (g=v), ", condition_g_equals_v)



if __name__ == "__main__":
    create_all()
    create_accuracy(LB_DELTA_START, "Lower Bound Accuracy", "Including zero", "nonzero", condition_all_lb, condition_greater_than_zero)
    create_accuracy(UB_DELTA_START, "Upper Bound Accuracy", "all(?)", "g = v", condition_all_ub, condition_g_equals_v)

    create_accuracy(LB_DELTA_START, "Envelope Lower Bound Accuracy", "Including zero", "Enveloped", condition_all_lb, condition_all_elb)
    create_accuracy(UB_DELTA_START, "Enveloped Upper Bound Accuracy", "all(?)", "Enveloped", condition_all_ub, condition_all_eub)

    create_accuracy(LB_DELTA_START, "Envelope Lower Bound Accuracy Nonzero", "Nonzero", "Nonzero Enveloped", condition_greater_than_zero, condition_greater_than_zero_env)
    create_accuracy(UB_DELTA_START, "Enveloped Upper Bound Accuracy g = v", "g = v", "g = v Enveloped", condition_g_equals_v, condition_g_equals_v_env)
