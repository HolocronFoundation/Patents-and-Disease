"""Merges CSVs

Author: Samuel Troper
Date: 2019.05.01
Purpose: Appends datasets to prepare for usage

"""

import csv
from glob import glob


def append_csvs(input_directory, output_directory,
                input_file_type="", output_file_name="appended.csv"):
    """Appends csvs.

    Parameters
    ----------
    input_directory : string
        Location of input files.
    output_directory : string
        Location to output appended files.
    input_file_type : string
        Input file type, e.g. ".csv".
    output_file_name : string
        Name for output file.

    """
    # assumes there are headers in the files
    output = []
    files = glob(input_directory + '*' + input_file_type)
    print(input_directory)
    print(files)
    for file in files:
        with open(file) as file_to_append:
            output.extend(list(csv.DictReader(file_to_append)))
    with open(output_directory + output_file_name, 'w') as output_file:
        fields = list(output[0].keys())
        writer = csv.DictWriter(output_file, fields)
        writer.writeheader()
        writer.writerows(output)


def __main__():
    step_2_dir = "C:/Users/stroper/Desktop/WIP Projects/Patents and Disease/2. Raw Data/"
    step_3_dir = "C:/Users/stroper/Desktop/WIP Projects/Patents and Disease/3. Appended Data/"
    append_csvs(step_2_dir + "Main (All gender)/", step_3_dir + "Main (All gender)/",
                input_file_type=".csv", output_file_name="IMHE-merged-all_gender.csv")
    append_csvs(step_2_dir + "Main (Split gender)/", step_3_dir + "Main (Split gender)/",
                input_file_type=".csv", output_file_name="IMHE-merged-split_gender.csv")


if __name__ == "__main__":
    __main__()
