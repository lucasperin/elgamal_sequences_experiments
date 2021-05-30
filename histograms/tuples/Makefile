PY=python3
SRC_DIR=scripts
NORMAL_DIR=plots/normal
V_IS_G_DIR=plots/v_is_g
ACC_DIR=plots/accuracy
NORM_DIST_DIR=plots/norm_dist

MAIN=main.py

all: normal v_is_g accuracy

normal: clean_normal run_normal

v_is_g: clean_v_is_g run_v_is_g

accuracy: clean_accuracy run_accuracy

norm_dist: clean_norm_dist run_norm_dist

run_normal:
	cd $(SRC_DIR) && $(PY) $(MAIN) normal

run_v_is_g:
	cd $(SRC_DIR) && $(PY) $(MAIN) v_is_g

run_accuracy:
	cd $(SRC_DIR) && $(PY) $(MAIN) accuracy

run_norm_dist:
	cd $(SRC_DIR) && $(PY) $(MAIN) norm_dist

clean_normal:
	rm -f $(NORMAL_DIR)/*.png

clean_v_is_g:
	rm -f $(V_IS_G_DIR)/*.png

clean_accuracy:
	rm -f $(ACC_DIR)/*.png

clean_norm_dist:
	rm -f $(NORM_DIST_DIR)/*.png

clean_all: clean_normal clean_v_is_g clean_accuracy clean_norm_dist
