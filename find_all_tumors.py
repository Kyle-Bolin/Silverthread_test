import os,glob
import find_tumor
import concurrent.futures, sqlite3, threading
lock = threading.Lock()
def find_all_tumors(in_dir,out_file):
    files = glob.glob(os.path.join(in_dir,'*.in'))
    with open(out_file,"w") as f:
        f.write('Filename,HasTumor,Rows,Columns\n')
        for file in files:
            f.write(file + ',' + str(find_tumor.find_tumor(file)))
    return 0 

def sql_to_csv(out_file, db_cursor):
    with open(out_file,'w') as f:
        f.write('Filename,HasTumor,Rows,Columns\n')
        for row in db_cursor.execute("SELECT * FROM results"):
            f.write(row[0]+','+row[1]+','+row[2]+','+row[3]+'\n')

def find_tumor_sql(in_file,db_con):
    db_cursor = db_con.cursor()
    result = find_tumor.find_tumor(in_file).split(",")
    try:
        lock.acquire(True)
        db_cursor.execute("INSERT INTO results values(?,?,?,?)",(in_file,result[0],result[1],result[2].strip()))
        db_con.commit()
    finally:
        lock.release()
    return result
    

def find_all_tumors_multithread(in_dir,out_file,threads):
    pool = []
    con = sqlite3.connect("tumor.db",check_same_thread=False)
    cur = con.cursor()
    cur.execute("Create TABLE IF NOT EXISTS results(File_name, HasTumor, Rows, Columns)")
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=threads)
    files = glob.glob(os.path.join(in_dir,'*.in'))
    for file in files:
        pool.append(executor.submit(find_tumor_sql,in_file=file,db_con=con))
    for task in concurrent.futures.as_completed(pool):
        pass
    sql_to_csv(out_file,cur)
    cur.execute("DROP TABLE results")
    con.close()