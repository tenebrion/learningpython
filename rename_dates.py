#! python3
"""
rename_dates.py - Renames file names with American MM-DD-YYYY date format to European
DD-MM-YYYY
"""
import shutil
import os
import re

# Create a regex that matches files with the American date format
date_pattern = re.compile(r"""^(.*?)      # all text before the date
                          ([01]?\d)-     # one or two digits before the date
                          ([0123]?\d)- # one or two digits for the day
                          ((19|20)\d\d)   # four digits for the year
                          (.*?)$          # all text after the date
                          """, re.VERBOSE)

# loop over the files in the working directory
for american_filename in os.listdir("."):
    mo = date_pattern.search(american_filename)

    # skip files without a date
    if mo is None:
        continue

    # get the different parts of the filename
    before_part = mo.group(1)
    month_part = mo.group(2)
    day_part = mo.group(3)
    year_part = mo.group(4)
    after_part = mo.group(6)

    # form the European-style filename
    european_filename = "{}{}-{}-{}{}".format(before_part, day_part, month_part, year_part, after_part)

    # get full, absolute file paths
    absolute_working_directory = os.path.abspath(".")
    american_filename = os.path.join(absolute_working_directory, american_filename)
    european_filename = os.path.join(absolute_working_directory, european_filename)

    # rename the files
    print("Renaming {} to {}...".format(american_filename, european_filename))
    # shutil.move(american_filename, european_filename) # uncomment after testing
