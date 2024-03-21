#!/bin/bash

#SBATCH -t 0-8:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=32
#SBATCH --cpus-per-task=1
#SBATCH --partition=genoa
#SBATCH --mail-type=BEGIN,END
#SBATCH --mail-user=j.schlumberger@vu.nl

module load 2022
module load Python/3.10.4-GCCcore-11.3.0
python 11_snellius_create_timing_sets.py 1 0 774 &
python 11_snellius_create_timing_sets.py 2 774 1548 &
python 11_snellius_create_timing_sets.py 3 1548 2322 &
python 11_snellius_create_timing_sets.py 4 2322 3096 &
python 11_snellius_create_timing_sets.py 5 3096 3870 &
python 11_snellius_create_timing_sets.py 6 3870 4644 &
python 11_snellius_create_timing_sets.py 7 4644 5418 &
python 11_snellius_create_timing_sets.py 8 5418 6192 &
python 11_snellius_create_timing_sets.py 9 6192 6966 &
python 11_snellius_create_timing_sets.py 10 6966 7740 &
python 11_snellius_create_timing_sets.py 11 7740 8514 &
python 11_snellius_create_timing_sets.py 12 8514 9288 &
python 11_snellius_create_timing_sets.py 13 9288 10062 &
python 11_snellius_create_timing_sets.py 14 10062 10836 &
python 11_snellius_create_timing_sets.py 15 10836 11610 &
python 11_snellius_create_timing_sets.py 16 11610 12383 &
python 11_snellius_create_timing_sets.py 17 12383 13156 &
python 11_snellius_create_timing_sets.py 18 13156 13929 &
python 11_snellius_create_timing_sets.py 19 13929 14702 &
python 11_snellius_create_timing_sets.py 20 14702 15475 &
python 11_snellius_create_timing_sets.py 21 15475 16248 &
python 11_snellius_create_timing_sets.py 22 16248 17021 &
python 11_snellius_create_timing_sets.py 23 17021 17794 &
python 11_snellius_create_timing_sets.py 24 17794 18567 &
python 11_snellius_create_timing_sets.py 25 18567 19340 &
python 11_snellius_create_timing_sets.py 26 19340 20113 &
python 11_snellius_create_timing_sets.py 27 20113 20886 &
python 11_snellius_create_timing_sets.py 28 20886 21659 &
python 11_snellius_create_timing_sets.py 29 21659 22432 &
python 11_snellius_create_timing_sets.py 30 22432 23205 &
python 11_snellius_create_timing_sets.py 31 23205 23978 &
python 11_snellius_create_timing_sets.py 32 23978 24750 &
wait
