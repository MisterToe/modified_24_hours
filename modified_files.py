import os.path, time
import datetime as dt
import shutil


for root,dirs,files in os.walk('C:\Users\student\Desktop\A'):  
    for file_name in files:
        now = dt.datetime.now()
        before = now - dt.timedelta(hours = 24)
        path = os.path.join(root,file_name)
        st = os.stat(path)    
        mod_time = dt.datetime.fromtimestamp(st.st_mtime)
        if mod_time > before:
            print('%s modified %s'%(path, mod_time))
            shutil.move(os.path.join(root, file_name), 'C:\Users\student\Desktop\B')
