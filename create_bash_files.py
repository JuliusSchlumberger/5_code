total_size = 24751  # Adjust this to your actual list size
operations = 32

# Calculate the size of each range
range_size = total_size // operations
remainder = total_size % operations

file_names = ['03_snellius_create_objectives_for_timehorizons.py', '02_snellius_create_system_parameters.py', '11_snellius_create_timing_sets.py']

for file_name in file_names:
    # Open a file to write the shell commands
    with open(f"{file_name[:-3]}.sh", "w") as file:
        file.write("#!/bin/bash\n\n"
                   "#SBATCH -t 0-8:00:00\n"
                    "#SBATCH --nodes=1\n"
                    f"#SBATCH --ntasks={operations}\n"
                    "#SBATCH --cpus-per-task=1\n"
                    "#SBATCH --partition=genoa\n"
                    "#SBATCH --mail-type=BEGIN,END\n"
                    "#SBATCH --mail-user=j.schlumberger@vu.nl\n\n"
                    "module load 2022\n"
                    "module load Python/3.10.4-GCCcore-11.3.0\n")
        for i in range(operations):
            start_index = i * range_size + min(i, remainder)
            end_index = start_index + range_size - 1
            if i < remainder:  # Distribute the remainder among the first few operations
                end_index += 1
            # Write the command to the file
            file.write(f"python {file_name} {i+1} {start_index} {end_index} &\n")
        file.write("wait\n")  # Wait for all background processes to finish

    print(f"Shell script {file_name[:-3]}.sh has been created.")



file_names = ['04_snellius_combine_per_risk_owner_hazard.py', '12_snellius_combine_timing_sets.py', '13_snellius_create_pathway_generator_inputs.py','01_snellius_performance_benchmark.py']
operations = 1
for file_name in file_names:
    # Open a file to write the shell commands
    with open(f"{file_name[:-3]}.sh", "w") as file:
        file.write("#!/bin/bash\n\n"
                   "#SBATCH -t 0-8:00:00\n"
                    "#SBATCH --nodes=1\n"
                    f"#SBATCH --ntasks={operations}\n"
                    "#SBATCH --cpus-per-task=1\n"
                    "#SBATCH --partition=genoa\n"
                    "#SBATCH --mail-type=BEGIN,END\n"
                    "#SBATCH --mail-user=j.schlumberger@vu.nl\n\n"
                    "module load 2022\n"
                    "module load Python/3.10.4-GCCcore-11.3.0\n")
        for i in range(operations):
            start_index = i * range_size + min(i, remainder)
            end_index = start_index + range_size - 1
            if i < remainder:  # Distribute the remainder among the first few operations
                end_index += 1
            # Write the command to the file
            file.write(f"python {file_name} {i+1} {start_index} {end_index} &\n")
        file.write("wait\n")  # Wait for all background processes to finish

    print(f"Shell script {file_name[:-3]}.sh has been created.")