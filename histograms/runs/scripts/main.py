from plot import *


normal_run_data = "../../../experiments/runs/normal_run_data.csv"
normal_plot_path = "../plots/normal/"

thm10_run_data = "../../../experiments/runs/thm10_run_data.csv"
thm10_plot_path = "../plots/thm10/"

v_is_g_run_data = "../../../experiments/runs/v_is_g_run_data.csv"
v_is_g_plot_path = "../plots/v_is_g/"


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


functions = {
    'normal': run_normal,
    'thm10': run_thm_10,
    'v_is_g': run_v_is_g,
}

if __name__ == '__main__':
    func = functions[sys.argv[1]]
    func()
    sys.exit(0)
