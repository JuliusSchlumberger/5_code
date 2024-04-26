#!/bin/bash

#SBATCH -t 0-8:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=4
#SBATCH --cpus-per-task=1
#SBATCH --partition=genoa
#SBATCH --mail-type=BEGIN,END
#SBATCH --mail-user=j.schlumberger@vu.nl

module load 2022
module load Python/3.10.4-GCCcore-11.3.0
python 05a_snellius_filter_pathways.py drought_agr &
python 05a_snellius_filter_pathways.py drought_shp &
python 05a_snellius_filter_pathways.py flood_agr &
python 05a_snellius_filter_pathways.py flood_urb &
wait
