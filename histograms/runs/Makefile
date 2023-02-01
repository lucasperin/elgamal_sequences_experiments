PY=python3
SRC_DIR=scripts
NORMAL_DIR=plots/normal
THM10_DIR=plots/thm10
V_IS_G_DIR=plots/v_is_g
RATIO_DIR=plots/ratio
ACCURACY_DIR=plots/accuracy
MAIN=main.py

all: normal thm10 v_is_g ratio accuracy

normal: clean_normal run_normal

thm10: clean_thm10 run_thm10

v_is_g: clean_v_is_g run_v_is_g

ratio: clean_ratio run_ratio

accuracy: clean_accuracy run_accuracy

run_normal:
	cd $(SRC_DIR) && $(PY) $(MAIN) normal

run_thm10:
	cd $(SRC_DIR) && $(PY) $(MAIN) thm10

run_v_is_g:
	cd $(SRC_DIR) && $(PY) $(MAIN) v_is_g

run_ratio:
	cd $(SRC_DIR) && $(PY) $(MAIN) ratio

run_accuracy:
	cd $(SRC_DIR) && $(PY) $(MAIN) accuracy

clean_normal:
	rm -f $(NORMAL_DIR)/*.png

clean_thm10:
	rm -f $(THM10_DIR)/*.png

clean_v_is_g:
	rm -f $(V_IS_G_DIR)/*.png

clean_ratio:
	rm -f $(RATIO_DIR)/*.png

clean_accuracy:
	rm -f $(ACCURACY_DIR)/*.png

clean_all: clean_normal clean_thm10 clean_v_is_g clean_ratio clean_accuracy
