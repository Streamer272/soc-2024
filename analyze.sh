#!/usr/bin/bash

find results ! -name 'train.txt' -type f -exec rm -f {} +

./venv/bin/python3 distribution.py --graph --save | tee results/distribution.txt
echo -e "\n\n\n\n"
./venv/bin/python3 analyze_sex.py --graph --save "results/Figure_13.png" | tee results/sex.txt
echo -e "\n\n\n\n"
./venv/bin/python3 analyze_ses.py --graph --save "results/Figure_14.png" | tee results/ses.txt
echo -e "\n\n\n\n"
./venv/bin/python3 analyze_occupation.py --graph --save "results/Figure_15.png" | tee results/occupation.txt
echo -e "\n\n\n\n"
./venv/bin/python3 analyze_living.py --graph --save "results/Figure_16.png" | tee results/living.txt
echo -e "\n\n\n\n"
./venv/bin/python3 analyze_commute.py --graph --save "results/Figure_17.png" | tee results/commute.txt
echo -e "\n\n\n\n"
./venv/bin/python3 analyze_sleep.py --graph --save "results/Figure_18.png" | tee results/sleep.txt
echo -e "\n\n\n\n"
./venv/bin/python3 analyze_absence.py --graph --save "results/Figure_19.png" | tee results/absence.txt
