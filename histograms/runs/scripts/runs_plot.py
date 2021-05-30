import sys
sys.path.append("../../../")

import csv
import matplotlib.pyplot as plt
import re
from math import ceil, floor, gcd

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

CONDITION=None
LB_FUNC=None
UB_FUNC=None
THM=None

"""
BOUND COMPUTATIONS
"""
def lb_thm10(row, t):
    g, p, v = int(row[G]), int(row[P]), int(row[V])
    q = floor(p / (pow(g, t +1)))
    return int(pow(floor(g/v), t-1) * pow(floor((v-1) * g / v), 2) * floor(q/v))

def ub_thm10(row, t):
    g, p, v = int(row[G]), int(row[P]), int(row[V])
    q = floor(p / (pow(g, t +1)))
    return int(pow(ceil(g/v), t-1) * pow(ceil((v-1) * g / v), 2) * ceil((q+1)/v))

def thm10_condition(row, t):
    """
    Check if g is invertible mod v
    """
    return gcd(int(row[G]), int(row[V])) == 1

def init_theorem10():
    print("Initializing THM10")
    global CONDITION, LB_FUNC, UB_FUNC, THM
    CONDITION=thm10_condition
    LB_FUNC=lb_thm10
    UB_FUNC=ub_thm10
    THM=10

def lb_clr9(row, t):
    g, p, v = int(row[G]), int(row[P]), int(row[V])
    q = floor(p / (pow(g, t +1)))
    return int((v-1)*pow(floor(g/v), t) * floor(((v-1)*g)/v) * floor(q/v))

def ub_clr9(row, t):
    g, p, v = int(row[G]), int(row[P]), int(row[V])
    q = floor(p / (pow(g, t +1)))
    return int((v-1)*pow(ceil(g/v), t) * ceil(((v-1)*g)/v) * ceil((q+1)/v))

def clr9_condition(row, t):
    return True

def init_clr9():
    print("Initializing THM9")
    global CONDITION, LB_FUNC, UB_FUNC, THM
    CONDITION=clr9_condition
    LB_FUNC=lb_clr9
    UB_FUNC=ub_clr9
    THM=9

"""
CONDITION HELPER FUNCTIONS
"""
def condition_all_lb(data, row, pos, t):
    if CONDITION(row,t):
        d = int(row[pos])
        data.append(d - LB_FUNC(row,t))

def condition_all_ub(data, row, pos, t):
    if CONDITION(row,t):
        d = int(row[pos])
        data.append(UB_FUNC(row,t) - d)

def condition_greater_than_zero(data, row, pos, t):
    if CONDITION(row,t):
        d = int(row[pos])
        lb = LB_FUNC(row,t)
        if d > 0:
            data.append(d - lb)

def condition_g_equals_v(data, row, pos, t):
    if CONDITION(row,t):
        if int(row[V]) == int(row[G]):
            data.append(UB_FUNC(row,t) - int(row[pos]))



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
        for row in reader:
            if len(row) > pos: #sometimes this is required since the sequence might not have all run lengths.
                condition(data, row, pos, t)

    if len(data) > 0:
        bins = list(range(NUM_BINS))
        h_data = [ data.count(i) for i in bins ]
        title += "t = {} with {:.2f}% outliers (Theorem {})".format(t, (100 - sum(h_data)/len(data)*100), THM)
        plt.bar(bins, h_data)
        plt.title(title)
        save_name = save_path + re.sub('[^A-Za-z0-9]+', '', title)
        plt.savefig(save_name, bbox_inches='tight')
        #plt.savefig(save_name, bbox_inches='tight', transparent=True)
        plt.clf()
    else:
        print("No bounds for t = {} and {}".format(t, title))


"""
RATIO PLOT
"""


def ratio_condition_all(row, v):
    return True


def ratio_condition_v_equals_g_all(row, v):
    return int(row[V]) == int(row[G])


def ratio_condition_v_equals_g_one_v(row, v):
    return (int(row[V]) == int(row[G])) and (int(row[V]) == v)


def ratio_condition_one_v(row, v):
    return int(row[V]) == v


def ratio(title, file_name, save_path, v, normalized, condition=None):
    """
    PLOT HELPER FUNCTIONS
    """
    if not callable(condition):
        return
    data_x = []
    data_y = []
    with open(file_name, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=CSV_DELIMITER)
        for row in reader:
            if condition(row, v):
                for t in range(T_MIN, T_MAX):
                    current_t = SUM_DELTA_START + (t-1)*SHIFT
                    next_t    = SUM_DELTA_START + (t)*SHIFT
                    if len(row) > next_t: #sometimes this is required since the sequence might not have all run lengths.
                        current_count = int(row[current_t])
                        next_count = int(row[next_t])
                        if (current_count > 0) and (current_count > next_count):
                            data_x.append(t)
                            if normalized:
                                data_y.append( (next_count/current_count) * int(row[V]))
                            else:
                                data_y.append( (next_count/current_count))

        if len(data_y) > 0:
            title = "{} - run ratio".format(title)
            plt.title(title)
            #plt.scatter(data_x, data_y)
            plt.hist2d(data_x, data_y, bins=50, cmap=plt.cm.jet, cmin=1)
            save_name = save_path + re.sub('[^A-Za-z0-9]+', '', title)
            plt.savefig(save_name, bbox_inches='tight')
            plt.savefig(save_name, bbox_inches='tight', transparent=True)
            plt.clf()


# def add_labels(fig, ax):
#     for bar in fig:
#         height = bar.get_height()
#         ax.annotate("{:.1f}%".format(height),
#                     xy=(bar.get_x() + bar.get_width() / 2, height/2),
#                     xytext=(0, 3),  # 3 points vertical offset
#                     textcoords="offset points",
#                     ha='center', va='bottom', rotation=90)
#
# def create_accuracy(bound_start, title, label1, label2, condition1=None, condition2=None):
#     if not callable(condition1):
#         return
#     if not callable(condition2):
#         return
#
#     acc1 = [None]*T_NUM
#     acc2 = [None]*T_NUM
#     with open(FILE_NAME, 'r') as csvfile:
#         reader = csv.reader(csvfile, delimiter=CSV_DELIMITER)
#         bins = list(range(T_MIN, T_MAX+1))
#         for t in bins:
#             data1 = []
#             data2 = []
#             i = t-T_MIN
#             pos = i*SHIFT + bound_start
#             csvfile.seek(0)
#             for row in reader:
#                 condition1(data1, row, pos, t)
#                 condition2(data2, row, pos, t)
#             acc1[i] = data1.count(0)/len(data1)*100
#             acc2[i] = data2.count(0)/len(data2)*100
#     fig = plt.figure()
#     ax = fig.add_subplot(111)
#     width = 0.20
#     f1 = ax.bar([b-width for b in bins], acc1, width*2, label=label1)
#     f2 = ax.bar([b+width for b in bins], acc2, width*2, label=label2)
#     ax.set_ylabel("Bound Accuraty (%)")
#     ax.set_xlabel("t")
#     ax.set_title(title)
#     ax.legend()
#     add_labels(f1, ax)
#     add_labels(f2, ax)
#     save_name = re.sub('[^A-Za-z0-9]+', '', title)
#     #plt.savefig(save_name, bbox_inches='tight', transparent=True)
#     plt.savefig(save_name, bbox_inches='tight')
#     plt.clf()


