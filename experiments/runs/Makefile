PY=python3
SRC_DIR=scripts
OUT_DIR=output
MAIN=main.py

all: normal thm10 v_is_g

normal: clean run_normal normal_run_data.csv

thm10: clean run_thm10 thm10_run_data.csv

v_is_g: clean run_v_is_g v_is_g_run_data.csv

run_normal:
	cd $(SRC_DIR) && $(PY) $(MAIN) normal

run_thm10:
	cd $(SRC_DIR) && $(PY) $(MAIN) thm10

run_v_is_g:
	cd $(SRC_DIR) && $(PY) $(MAIN) v_is_g

%.csv:
	cat $(OUT_DIR)/*.csv > $@

clean:
	rm -f $(OUT_DIR)/*.csv

clean_all: clean
	rm -f *.csv
