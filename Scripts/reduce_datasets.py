"""Drops data

Author: Samuel Troper
Date: 2019.05.01
Purpose: Drops data which will not be used

"""

import csv
from glob import glob

def drop_data():


def __main__():
    step_3_dir = "C:/Users/stroper/Desktop/WIP Projects/Patents and Disease/3. Appended Data/"
    step_4_dir = "C:/Users/stroper/Desktop/WIP Projects/Patents and Disease/2. Reduced Data/"
    drop_data(step_3_dir + "Main (All gender)/", step_4_dir + "Main (All gender)/",
                input_file_type=".csv", output_file_name="IMHE-merged-all_gender.csv")
    drop_data(step_3_dir + "Main (Split gender)/", step_4_dir + "Main (Split gender)/",
                input_file_type=".csv", output_file_name="IMHE-merged-split_gender.csv")


if __name__ == "__main__":
    __main__()
