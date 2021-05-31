import sys
sys.path.append("../../../")

import csv
import matplotlib.pyplot as plt
import re
from math import ceil, floor
from array import array

CSV_DELIMITER='\t'
T_MIN=2
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
    return max((p/v) * ((g-v)/(g*v))**(t-1), tuple_lb(row, t))


def tuple_eub(row, t):
    g, p, v = int(row[G]), int(row[P]), int(row[V])
    return min((p/v) * ((g+v)/(g*v))**(t-1), tuple_ub(row, t))


"""
CONDITION HELPER FUNCTIONS
"""


def condition_all_lb(data, row, pos, t):
    d = int(row[pos])
    data.append(d - tuple_lb(row, t))


def condition_all_elb(data, row, pos, t):
    d = int(row[pos])
    data.append(d - tuple_elb(row, t))


def condition_all_ub(data, row, pos, t):
    d = int(row[pos])
    data.append(tuple_ub(row, t) - d)


def condition_all_eub(data, row, pos, t):
    d = int(row[pos])
    data.append(tuple_eub(row, t) - d)


def condition_greater_than_zero(data, row, pos, t):
    d = int(row[pos])
    lb = tuple_lb(row, t)
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
        data.append(tuple_eub(row, t) - int(row[pos]))
    else:
        print("ERROR!!")


"""
PLOT HELPER FUNCTIONS
"""


def create_histogram(t, bound_start, title, file_name, save_path, condition=None):
    if not callable(condition):
        return
    data = []
    with open(file_name, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=CSV_DELIMITER)
        pos = (t-T_MIN)*SHIFT + bound_start
        print(pos)
        for row in reader:
            if len(row) > pos: #sometimes this is required since the sequence might not have all tuple lengths.
                condition(data, row, pos, t)

    if len(data) > 0:
        bins = list(range(NUM_BINS))
        h_data = [ data.count(i) for i in bins ]
        title += " t = {} with {:.2f}% outliers".format(t, (100 - sum(h_data)/len(data)*100))
        plt.bar(bins, h_data)
        plt.title(title)
        save_name = save_path + re.sub('[^A-Za-z0-9]+', '', title)
        plt.savefig(save_name, bbox_inches='tight')
        #plt.savefig(save_name, bbox_inches='tight', transparent=True)
        plt.clf()
    else:
        print("No bounds for t = {} and {}".format(t, title))

def add_labels(fig, ax):
    for bar in fig:
        height = bar.get_height()
        ax.annotate("{:.1f}%".format(height),
                    xy=(bar.get_x() + bar.get_width() / 2, height/2),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', rotation=90)


def create_accuracy(bound_start, file_name, save_path, title, label1, label2, condition1=None, condition2=None):
    if not callable(condition1):
        return
    if not callable(condition2):
        return

    acc1 = [0]*T_NUM
    acc2 = [0]*T_NUM
    with open(file_name, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=CSV_DELIMITER)
        bins = list(range(T_MIN, T_MAX+1))
        for t in bins:
            data1 = []
            data2 = []
            pos = (t - T_MIN) * SHIFT + bound_start
            csvfile.seek(0)
            for row in reader:
                if len(row) > pos:  # sometimes this is required since the sequence might not have all tuple lengths.
                    condition1(data1, row, pos, t)
                    condition2(data2, row, pos, t)
            acc1[t-T_MIN] = data1.count(0)/len(data1)*100
            acc2[t-T_MIN] = data2.count(0)/len(data2)*100
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
    save_name = save_path + re.sub('[^A-Za-z0-9]+', '', title)
    #plt.savefig(save_name, bbox_inches='tight', transparent=True)
    plt.savefig(save_name, bbox_inches='tight')
    plt.clf()
    plt.close(fig)


def normalize_delta(p, v, t, delta):
    return pow(v, t) * (delta / (p - 1))

def create_normalized_distribution(title, file_name, save_path):
    _d_start = 4
    _shift = 1
    with open(file_name, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=CSV_DELIMITER)
        data = [0]*201
        outliers = 0
        for row in reader:
            delta_pos = _d_start
            p = int(row[0])
            v = int(row[1])
            t = int(row[3])
            while len(row) > delta_pos:
                norm = normalize_delta(p, v, t, int(row[delta_pos]))
                norm_pos = int(norm*100)
                if norm_pos > 200 or norm_pos < 0:
                    outliers +=1
                else:
                    data[norm_pos] += 1
                delta_pos += _shift
    print("Finished reading data")
    fig = plt.figure()
    ax = fig.add_subplot(111)
    width = 0.20
    toatal = outliers + sum(data)
    f1 = ax.bar([b*0.01 for b in range(201)], [b/total for b in data], width*2)
    ax.set_ylabel("Distribution")
    ax.set_xlabel("Normalized delta")
    ax.set_title(title)
    ax.legend()
    # add_labels(f1, ax)
    save_name = save_path + re.sub('[^A-Za-z0-9]+', '', title)
    plt.savefig(save_name, bbox_inches='tight')
    plt.clf()
    print("Outliers = {}({})".format(outliers, outliers/total*100))


def create_all():
    for t in range(T_MIN, T_MAX+1):
        create_histogram(t, LB_DELTA_START, "LB, ", condition_all_lb)
        create_histogram(t, LB_DELTA_START, "LB (> 0), ", condition_greater_than_zero)
        create_histogram(t, UB_DELTA_START, "UB, ", condition_all_ub)
        create_histogram(t, UB_DELTA_START, "UB (g=v), ", condition_g_equals_v)



if __name__ == "__main__":
    create_all()
    # create_accuracy(LB_DELTA_START, "Lower Bound Accuracy", "Including zero", "nonzero", condition_all_lb, condition_greater_than_zero)
    # create_accuracy(UB_DELTA_START, "Upper Bound Accuracy", "all(?)", "g = v", condition_all_ub, condition_g_equals_v)
    #
    # create_accuracy(LB_DELTA_START, "Envelope Lower Bound Accuracy", "Including zero", "Enveloped", condition_all_lb, condition_all_elb)
    # create_accuracy(UB_DELTA_START, "Enveloped Upper Bound Accuracy", "all(?)", "Enveloped", condition_all_ub, condition_all_eub)
    #
    # create_accuracy(LB_DELTA_START, "Envelope Lower Bound Accuracy Nonzero", "Nonzero", "Nonzero Enveloped", condition_greater_than_zero, condition_greater_than_zero_env)
    # create_accuracy(UB_DELTA_START, "Enveloped Upper Bound Accuracy g = v", "g = v", "g = v Enveloped", condition_g_equals_v, condition_g_equals_v_env)
