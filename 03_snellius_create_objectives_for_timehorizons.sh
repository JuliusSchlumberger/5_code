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
python 03_snellius_create_objectives_for_timehorizons.py 1 0 774 &
python 03_snellius_create_objectives_for_timehorizons.py 2 774 1548 &
python 03_snellius_create_objectives_for_timehorizons.py 3 1548 2322 &
python 03_snellius_create_objectives_for_timehorizons.py 4 2322 3096 &
python 03_snellius_create_objectives_for_timehorizons.py 5 3096 3870 &
python 03_snellius_create_objectives_for_timehorizons.py 6 3870 4644 &
python 03_snellius_create_objectives_for_timehorizons.py 7 4644 5418 &
python 03_snellius_create_objectives_for_timehorizons.py 8 5418 6192 &
python 03_snellius_create_objectives_for_timehorizons.py 9 6192 6966 &
python 03_snellius_create_objectives_for_timehorizons.py 10 6966 7740 &
python 03_snellius_create_objectives_for_timehorizons.py 11 7740 8514 &
python 03_snellius_create_objectives_for_timehorizons.py 12 8514 9288 &
python 03_snellius_create_objectives_for_timehorizons.py 13 9288 10062 &
python 03_snellius_create_objectives_for_timehorizons.py 14 10062 10836 &
python 03_snellius_create_objectives_for_timehorizons.py 15 10836 11610 &
python 03_snellius_create_objectives_for_timehorizons.py 16 11610 12383 &
python 03_snellius_create_objectives_for_timehorizons.py 17 12383 13156 &
python 03_snellius_create_objectives_for_timehorizons.py 18 13156 13929 &
python 03_snellius_create_objectives_for_timehorizons.py 19 13929 14702 &
python 03_snellius_create_objectives_for_timehorizons.py 20 14702 15475 &
python 03_snellius_create_objectives_for_timehorizons.py 21 15475 16248 &
python 03_snellius_create_objectives_for_timehorizons.py 22 16248 17021 &
python 03_snellius_create_objectives_for_timehorizons.py 23 17021 17794 &
python 03_snellius_create_objectives_for_timehorizons.py 24 17794 18567 &
python 03_snellius_create_objectives_for_timehorizons.py 25 18567 19340 &
python 03_snellius_create_objectives_for_timehorizons.py 26 19340 20113 &
python 03_snellius_create_objectives_for_timehorizons.py 27 20113 20886 &
python 03_snellius_create_objectives_for_timehorizons.py 28 20886 21659 &
python 03_snellius_create_objectives_for_timehorizons.py 29 21659 22432 &
python 03_snellius_create_objectives_for_timehorizons.py 30 22432 23205 &
python 03_snellius_create_objectives_for_timehorizons.py 31 23205 23978 &
python 03_snellius_create_objectives_for_timehorizons.py 32 23978 24750 &
wait
