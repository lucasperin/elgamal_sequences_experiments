from tuple_plot import *


normal_run_data = "../../../experiments/tuples/normal_tuple_data.csv"
normal_plot_path = "../plots/normal/"

v_is_g_run_data = "../../../experiments/tuples/v_is_g_tuple_data.csv"
v_is_g_plot_path = "../plots/v_is_g/"

accuracy_path = "../plots/accuracy/"

normal_run_data_all = "../../../experiments/tuples/normal_tuple_data_all.csv"
v_is_g_run_data_all = "../../../experiments/tuples/v_is_g_tuple_data_all.csv"
norm_dist_path = "../plots/norm_dist/"

def run_normal():
    print("Run Normal")
    for t in range(T_MIN, T_MAX+1):
        create_histogram(t, LB_DELTA_START, "LB, ", normal_run_data, condition_all_lb)
        create_histogram(t, LB_DELTA_START, "LB (> 0), ", normal_run_data, normal_plot_path, condition_greater_than_zero)
        create_histogram(t, UB_DELTA_START, "UB, ", normal_run_data, normal_plot_path, condition_all_ub)
        create_histogram(t, UB_DELTA_START, "UB (g=v), ", normal_run_data, normal_plot_path, condition_g_equals_v)



def run_v_is_g():
    print("Run v is g")
    for t in range(T_MIN, T_MAX+1):
        create_histogram(t, LB_DELTA_START, "LB, ", v_is_g_run_data, v_is_g_plot_path, condition_all_lb)
        create_histogram(t, LB_DELTA_START, "LB (> 0), ", v_is_g_run_data, v_is_g_plot_path, condition_greater_than_zero)
        create_histogram(t, UB_DELTA_START, "UB, ", v_is_g_run_data, v_is_g_plot_path, condition_all_ub)
        create_histogram(t, UB_DELTA_START, "UB (g=v), ", v_is_g_run_data, v_is_g_plot_path, condition_g_equals_v)


def run_accuracy():
    print("Run Accuracy")
    for t in range(T_MIN, T_MAX+1):
        create_accuracy(LB_DELTA_START, normal_run_data, accuracy_path,
                        "Lower Bound Accuracy", "Including zero", "nonzero", condition_all_lb, condition_greater_than_zero)
        create_accuracy(UB_DELTA_START, v_is_g_run_data, accuracy_path,
                        "Upper Bound Accuracy", "all(?)", "g = v", condition_all_ub, condition_g_equals_v)

        create_accuracy(LB_DELTA_START, normal_run_data, accuracy_path,
                        "Envelope Lower Bound Accuracy", "Including zero", "Enveloped", condition_all_lb, condition_all_elb)
        create_accuracy(UB_DELTA_START, normal_run_data, accuracy_path,
                        "Enveloped Upper Bound Accuracy", "all(?)", "Enveloped", condition_all_ub, condition_all_eub)

        create_accuracy(LB_DELTA_START, normal_run_data, accuracy_path,
                        "Envelope Lower Bound Accuracy Nonzero", "Nonzero", "Nonzero Enveloped",
                        condition_greater_than_zero, condition_greater_than_zero_env)
        create_accuracy(UB_DELTA_START, v_is_g_run_data, accuracy_path,
                        "Enveloped Upper Bound Accuracy g = v", "g = v", "g = v Enveloped",
                        condition_g_equals_v, condition_g_equals_v_env)

def run_norm_dist():
    print("Run Normalized Distribution")
    create_normalized_distribution("Normalized Distribution", normal_run_data_all, norm_dist_path)
    create_normalized_distribution("Normalized Distribution where v is g", v_is_g_run_data_all, norm_dist_path)

functions = {
    'normal': run_normal,
    'v_is_g': run_v_is_g,
    'accuracy': run_accuracy,
    'norm_dist': run_norm_dist,
}

if __name__ == '__main__':
    func = functions[sys.argv[1]]
    func()
    sys.exit(0)
