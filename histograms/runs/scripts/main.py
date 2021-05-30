from runs_plot import *


normal_run_data = "../../../experiments/runs/normal_run_data.csv"
normal_plot_path = "../plots/normal/"

thm10_run_data = "../../../experiments/runs/thm10_run_data.csv"
thm10_plot_path = "../plots/thm10/"

v_is_g_run_data = "../../../experiments/runs/v_is_g_run_data.csv"
v_is_g_plot_path = "../plots/v_is_g/"

ratio_plot_path = "../plots/ratio/"

def run_normal():
    print("Run Normal")
    init_clr9()
    for t in range(T_MIN, T_MAX+1):
        create_histogram(t, LB_DELTA_START, "LB, ", normal_run_data, normal_plot_path, condition_all_lb)
        create_histogram(t, LB_DELTA_START, "LB (> 0), ", normal_run_data, normal_plot_path, condition_greater_than_zero)
        create_histogram(t, UB_DELTA_START, "UB, ", normal_run_data, normal_plot_path, condition_all_ub)
        create_histogram(t, UB_DELTA_START, "UB (g=v), ", normal_run_data, normal_plot_path, condition_g_equals_v)


def run_thm_10():
    print("Run THM10")
    init_theorem10()
    for t in range(T_MIN, T_MAX+1):
        create_histogram(t, LB_DELTA_START, "LB, ", thm10_run_data, thm10_plot_path, condition_all_lb)
        create_histogram(t, LB_DELTA_START, "LB (> 0), ", thm10_run_data, thm10_plot_path, condition_greater_than_zero)
        create_histogram(t, UB_DELTA_START, "UB, ", thm10_run_data, thm10_plot_path, condition_all_ub)
        create_histogram(t, UB_DELTA_START, "UB (g=v), ", thm10_run_data, thm10_plot_path, condition_g_equals_v)


def run_v_is_g():
    print("Run v is g")
    init_clr9()
    for t in range(T_MIN, T_MAX+1):
        create_histogram(t, LB_DELTA_START, "LB, ", v_is_g_run_data, v_is_g_plot_path, condition_all_lb)
        create_histogram(t, LB_DELTA_START, "LB (> 0), ", v_is_g_run_data, v_is_g_plot_path, condition_greater_than_zero)
        create_histogram(t, UB_DELTA_START, "UB, ", v_is_g_run_data, v_is_g_plot_path, condition_all_ub)
        create_histogram(t, UB_DELTA_START, "UB (g=v), ", v_is_g_run_data, v_is_g_plot_path, condition_g_equals_v)

def ratio_all():
    ratio("All Data (Normalized)", normal_run_data, ratio_plot_path, 0, True, ratio_condition_all)
    ratio("All Data And v is Gen (Normalized)", v_is_g_run_data, ratio_plot_path, 0, True, ratio_condition_v_equals_g_all)
    for v in range(2, 10):
        ratio("v = {} (Normalized)".format(v), normal_run_data, ratio_plot_path, v, True, ratio_condition_one_v)
        ratio("v = {} And v is Gen(Normalized)".format(v), v_is_g_run_data, ratio_plot_path, v, True, ratio_condition_v_equals_g_one_v)


functions = {
    'normal': run_normal,
    'thm10': run_thm_10,
    'v_is_g': run_v_is_g,
    'ratio': ratio_all,
}

if __name__ == '__main__':
    func = functions[sys.argv[1]]
    func()
    sys.exit(0)
