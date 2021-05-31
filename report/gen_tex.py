import os

OUTPUT_FILENAME = '/tmp/figures.tex'

HEADER = """ \\documentclass{article}
\\usepackage[utf8]{inputenc}
\\usepackage{geometry,graphicx}
 \\geometry{
 a4paper,
 total={170mm,257mm},
 left=20mm,
 top=20mm,
 }

\\title{ElGamal Experiments Report}
\\author{Lucas Perin}
\\date{May 2020}

\\begin{document}

\\maketitle 
"""

END = "\\end{document}"

ONE_FIGS = """
\\begin{figure}[!htb]
\\centering
\\centering
\\includegraphics[width=.5\\linewidth]{image1}
\\end{figure}
"""
TWO_FIGS = """
\\begin{figure}[!htb]
\\centering
\\begin{minipage}{.5\\textwidth}
  \\centering
  \\includegraphics[width=.9\\linewidth]{image1}
\\end{minipage}%
\\begin{minipage}{.5\\textwidth}
  \\centering
  \\includegraphics[width=.9\\linewidth]{image2}
\\end{minipage}
\\end{figure}
"""


NORMAL_TUPLES = "/home/lucasperin/workspace/elgamal_sequences_experiments/histograms/tuples/plots/normal"
V_IS_G_TUPLES = '/home/lucasperin/workspace/elgamal_sequences_experiments/histograms/tuples/plots/v_is_g/'
ACCURACY_TUPLES = '/home/lucasperin/workspace/elgamal_sequences_experiments/histograms/tuples/plots/accuracy/'
NORMAL_DIST_TUPLES = '/home/lucasperin/workspace/elgamal_sequences_experiments/histograms/tuples/plots/norm_dist/'

NORMAL_RUNS = "/home/lucasperin/workspace/elgamal_sequences_experiments/histograms/runs/plots/normal"
THM10_RUNS = '/home/lucasperin/workspace/elgamal_sequences_experiments/histograms/runs/plots/thm10'
V_IS_G_RUNS = '/home/lucasperin/workspace/elgamal_sequences_experiments/histograms/runs/plots/v_is_g/'
RATIO_RUNS = '/home/lucasperin/workspace/elgamal_sequences_experiments/histograms/runs/plots/ratio'

def clear_page(file):
    file.write("\n\\clearpage\n")

def write_figures(dir, header, file):
    f.write("\n\\subsection{{{}}}\n".format(header))
    FIGS = os.listdir(dir)
    FIGS.remove(".gitkeep")
    for i in range(0, len(FIGS) - 1, 2):
        temp = TWO_FIGS.replace('image1', dir + '/' + FIGS[i])
        temp = temp.replace('image2', dir + '/' + FIGS[i + 1])
        file.write(temp)

    if len(FIGS)%2 != 0:
        temp = ONE_FIGS.replace('image1', dir + '/' + FIGS[len(FIGS) - 1])
        file.write(temp)



if __name__ == "__main__":
    with open(OUTPUT_FILENAME, 'w') as f:
        f.write(HEADER)
        f.write("\n\\section{TUPLES}\n")
        write_figures(NORMAL_TUPLES, "Tuples bounds (normal experiment)", f)
        clear_page(f)
        write_figures(V_IS_G_TUPLES, "Tuple bounds (v is Generator experiment)", f)
        clear_page(f)
        write_figures(ACCURACY_TUPLES, "Tuple bounds (accuracy experiment)", f)
        clear_page(f)
        write_figures(NORMAL_DIST_TUPLES, "Tuple bounds (normalized distribution experiment)", f)
        clear_page(f)
        f.write("\n\\section{RUNS}\n")
        write_figures(NORMAL_RUNS, "Run bounds (normal experiment)", f)
        clear_page(f)
        write_figures(THM10_RUNS, "Run bounds (Theorem 10 experiment)", f)
        clear_page(f)
        write_figures(V_IS_G_RUNS, "Run bounds (V is Generator experiment)", f)
        clear_page(f)
        write_figures(RATIO_RUNS, "Run bounds (Ratio experiment)", f)
        f.write(END)
