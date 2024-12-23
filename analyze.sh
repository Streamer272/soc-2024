#!/usr/bin/bash

./venv/bin/python3 distribution.py --graph --save
./venv/bin/python3 analyze_sex.py --graph --save "Figure_13.png"
./venv/bin/python3 analyze_ses.py --graph --save "Figure_14.png"
./venv/bin/python3 analyze_occupation.py --graph --save "Figure_15.png"
./venv/bin/python3 analyze_living.py --graph --save "Figure_16.png"
./venv/bin/python3 analyze_commute.py --graph --save "Figure_17.png"
./venv/bin/python3 analyze_sleep.py --graph --save "Figure_18.png"
./venv/bin/python3 analyze_absence.py --graph --save "Figure_19.png"
