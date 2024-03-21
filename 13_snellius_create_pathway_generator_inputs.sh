#!/bin/bash

#SBATCH -t 0-8:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --partition=genoa
#SBATCH --mail-type=BEGIN,END
#SBATCH --mail-user=j.schlumberger@vu.nl

module load 2022
module load Python/3.10.4-GCCcore-11.3.0
python 13_snellius_create_pathway_generator_inputs.py 1 0 773 &
wait
