from tuple_plot import *


normal_tuple_data = "../../../experiments/tuples/normal_tuple_data.csv"
normal_plot_path = "../plots/normal/"

v_is_g_tuple_data = "../../../experiments/tuples/v_is_g_tuple_data.csv"
v_is_g_plot_path = "../plots/v_is_g/"

accuracy_plot_path = "../plots/accuracy/"

normal_tuple_data_all = "../../../experiments/tuples/normal_tuple_data_all.csv"
v_is_g_tuple_data_all = "../../../experiments/tuples/v_is_g_tuple_data_all.csv"
norm_dist_path = "../plots/norm_dist/"

def tuple_normal():
    print("Run Normal")
    for t in range(T_MIN, T_MAX+1):
        create_histogram(t, LB_DELTA_START, "LB, ", normal_tuple_data, condition_all_lb)
        create_histogram(t, LB_DELTA_START, "LB (> 0), ", normal_tuple_data, normal_plot_path, condition_greater_than_zero)
        create_histogram(t, UB_DELTA_START, "UB, ", normal_tuple_data, normal_plot_path, condition_all_ub)
        create_histogram(t, UB_DELTA_START, "UB (g=v), ", normal_tuple_data, normal_plot_path, condition_g_equals_v)



def tuple_v_is_g():
    print("Run v is g")
    for t in range(T_MIN, T_MAX+1):
        create_histogram(t, LB_DELTA_START, "LB, ", v_is_g_tuple_data, v_is_g_plot_path, condition_all_lb)
        create_histogram(t, LB_DELTA_START, "LB (> 0), ", v_is_g_tuple_data, v_is_g_plot_path, condition_greater_than_zero)
        create_histogram(t, UB_DELTA_START, "UB, ", v_is_g_tuple_data, v_is_g_plot_path, condition_all_ub)
        create_histogram(t, UB_DELTA_START, "UB (g=v), ", v_is_g_tuple_data, v_is_g_plot_path, condition_g_equals_v)


def tuple_accuracy():
    print("Run Accuracy")
    create_accuracy2(LB_DELTA_START, normal_tuple_data, normal_tuple_data, accuracy_plot_path,
                    "Tuples Lower Bound Accuracy", "All trials", r'$\lambda(z) > 0$', condition_all_lb, condition_greater_than_zero)
    create_accuracy2(LB_DELTA_START, normal_tuple_data, normal_tuple_data, accuracy_plot_path,
                     "Tuples Envelope Lower Bound Accuracy", "All trials", "Enveloped", condition_all_lb, condition_all_elb)
    create_accuracy2(LB_DELTA_START, normal_tuple_data, normal_tuple_data, accuracy_plot_path,
                     "Tuples Envelope Lower Bound Accuracy Nonzero", r'$\lambda(z) > 0$', "Nonzero Enveloped",
                     condition_greater_than_zero, condition_greater_than_zero_env)
    create_accuracy2(LB_DELTA_START, normal_tuple_data, normal_tuple_data, accuracy_plot_path,
                     "Tuples Lower Bound Accuracy all vs binary", "All trials", "Binary", condition_all_lb, condition_binary_lb)
    create_accuracy2(LB_DELTA_START, v_is_g_tuple_data, v_is_g_tuple_data, accuracy_plot_path,
                     "Tuples Lower Bound Accuracy all (g is v) vs binary (g is v)", r"All ($g = v$)", r"Binary ($g = v$)", condition_all_lb, condition_binary_lb)
    create_accuracy2(LB_DELTA_START, normal_tuple_data, v_is_g_tuple_data, accuracy_plot_path,
                     "Tuples Lower Bound Accuracy binary vs binary where v is g", "Binary", r"Binary ($v = g$)", condition_binary_lb, condition_binary_lb, "green")


    create_accuracy2(UB_DELTA_START, normal_tuple_data, v_is_g_tuple_data, accuracy_plot_path,
                    "Tuples Upper Bound Accuracy", "All trials", r"$g = v$", condition_all_ub, condition_g_equals_v, 'green')
    create_accuracy2(UB_DELTA_START, normal_tuple_data, normal_tuple_data, accuracy_plot_path,
                    "Tuples Enveloped Upper Bound Accuracy", "All trials", "Enveloped", condition_all_ub, condition_all_eub)
    create_accuracy2(UB_DELTA_START, v_is_g_tuple_data, v_is_g_tuple_data, accuracy_plot_path,
                    "Tuples Enveloped Upper Bound Accuracy g = v", r"$g = v$", r"$g = v$ Enveloped",
                     condition_g_equals_v, condition_g_equals_v_env, 'green')
    create_accuracy2(UB_DELTA_START, normal_tuple_data, normal_tuple_data, accuracy_plot_path,
                     "Tuples Upper Bound Accuracy all s binary", "All trials", "Binary", condition_all_ub, condition_binary_ub)
    create_accuracy2(UB_DELTA_START, v_is_g_tuple_data, v_is_g_tuple_data, accuracy_plot_path,
                     "Tuples Upper Bound Accuracy all (g is v) s binary (g is v)", r"All ($g = v$)", r"Binary ($g = v$)", condition_all_ub, condition_binary_ub)
    create_accuracy2(UB_DELTA_START, normal_tuple_data, v_is_g_tuple_data, accuracy_plot_path,
                     "Tuples Upper Bound Accuracy binary vs binary where v is g", "Binary", r"Binary ($v = g$)", condition_binary_ub, condition_binary_ub, "green")

def tuple_norm_dist():
    print("Run Normalized Distribution")
    create_normalized_distribution("Normalized Distribution", normal_tuple_data_all, norm_dist_path)
    create_normalized_distribution("Normalized Distribution where v is g", v_is_g_tuple_data_all, norm_dist_path)

functions = {
    'normal': tuple_normal,
    'v_is_g': tuple_v_is_g,
    'accuracy': tuple_accuracy,
    'norm_dist': tuple_norm_dist,
}

if __name__ == '__main__':
    func = functions[sys.argv[1]]
    func()
    sys.exit(0)
