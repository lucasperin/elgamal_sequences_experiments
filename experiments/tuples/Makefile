PY=python3
SRC_DIR=scripts
OUT_DIR=output
MAIN=main.py

all: normal v_is_g normal_all v_is_g_all

normal: clean run_normal normal_tuple_data.csv

v_is_g: clean run_v_is_g v_is_g_tuple_data.csv

normal_all: clean run_normal_all normal_tuple_data_all.csv

v_is_g_all: clean run_v_is_g_all v_is_g_tuple_data_all.csv

run_normal:
	cd $(SRC_DIR) && $(PY) $(MAIN) normal

run_v_is_g:
	cd $(SRC_DIR) && $(PY) $(MAIN) v_is_g

run_normal_all:
	cd $(SRC_DIR) && $(PY) $(MAIN) normal_all

run_v_is_g_all:
	cd $(SRC_DIR) && $(PY) $(MAIN) v_is_g_all

%.csv:
	cat $(OUT_DIR)/*.csv > $@

clean:
	rm -f $(OUT_DIR)/*.csv

clean_all: clean
	rm -f *.csv