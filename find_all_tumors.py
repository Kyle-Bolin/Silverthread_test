import os,glob
import find_tumor
import concurrent.futures
dirpath = './Slice_inputs'
outputfile = "out.csv"
def find_all_tumors(in_dir,out_file):
    files = glob.glob(os.path.join(in_dir,'*.in'))
    with open(out_file,"w") as f:
        f.write('Filename,HasTumor,Rows,Columns\n')
        for file in files:
            f.write(file + ',' + str(find_tumor.find_tumor(file)))
    return 0 

def find_all_tumors_multithread(in_dir,out_file,cores):
    pass
