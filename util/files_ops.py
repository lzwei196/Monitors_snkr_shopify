import glob, os, sys
import datetime as dt

def remove_old_files(folder, day):
    '''remove files older than
       'day' days from folder
    '''
    for file in glob.glob(folder):
        last_changed = os.path.getmtime(file)
        last_changed = dt.datetime.fromtimestamp(last_changed)
        days_diff = (dt.datetime.now() -  last_changed).days
        if days_diff > day:
            print(f'removing {file}')
            os.remove(file)

if __name__ == '__main__':
    folder = sys.argv[1]
    day = int(sys.argv[2])
    remove_old_files(folder, day)