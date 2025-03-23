#!/usr/bin/bash

rm results/*

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
echo -e "\n\n\n\n"
./venv/bin/python3 train_nn.py --graph --save "results/Figure_20.png" | tee results/train.txt
echo -e "\n\n\n\n"

tar cvzf results.tar.gz results/
zip results.zip results/*
