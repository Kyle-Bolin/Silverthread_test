Silverthread Coding Test
Written By: Kyle Bolin
Date: 9/7/2023

Problems Completed: 1,2,3

How to Install:

    install python3 if not already installed
    clone this repo
    copy find_all_tumors,find_all_tumors.py,find_tumor, and find_tumor.py to a location on your $PATH (ex:~/usr/local/bin)

Ussage:

    find_tumor:
        takes a .in file, filters the data to only letters, checks to see if the data forms a square matrix, then outputs true/false if a tumor is suspected, number of rows, number of columns to stdout. will take anyfile for the input but will fail anyfile with data not in a square matrix after it is filtered and will output error results to stdout.
            Arguments:
            --inputfile "yourinfile.in"  *required*
    EX: >>>find_tumor --inputfile tumor.in
            True,4,4
    
    find_all_tumors:
        Scans a inputed directory for .in files and then runs find_tumor from find_tumor.py on each one. The result is then placed in a csv file for all results.
        This program has two modes, a single and multithreaded mode.
        The singlethreaded mode is meant for small directories and has no redundancy.
        The multithreaded mode is meant for large directories and has database recovery if the process is interupted. 
        If the processes completes sucessfully then the database is cleared and a csv is outputed instead.

        Arguments: 
        --inputdir "yourdirectory" *required*
        --outputfile "results.csv" *required*
        --parallel "Number of threads wanted"

    EX: find_all_tumors -inputdir ./Slice_inputs --outputfile results.csv --parallel 5

Pytest:

        test_tumor.py is the test script 
        Slice_inputs has everything to test if anychanges are made
        It is recomended that Pytest is ran in a virtual environment 
        to do this run the following in the cloned directory
            python3 -m venv venv 
            source venv/bin/activate
        then install pytest
            pip install pytest
        then to run pytest
            pytest
        then to get out of the virtual envrionment
            deactivate
        

