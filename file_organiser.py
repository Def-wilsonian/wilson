import os
from pathlib import Path
import shutil
os.chdir(Path.home()/'wilson')
Dfolder = Path.cwd()
os.chdir(Path(Path.home()/'wilson'))
for dir in os.listdir(Path.home()):
    #print(Path(dir))
    try:
        if Path(Path.home()/dir).is_dir() and Path.home()/dir != Dfolder:
            for subdir in os.listdir(Path(Path.home()/dir)):
                if Path(subdir).suffix == '.py':
                    print(Path(subdir))
                    shutil.copy(Path(Path.home()/dir/subdir), Dfolder)
                continue
        elif Path(dir).suffix == '.py':
            print(Path(dir))
            #shutil.copy(Path(dir), Dfolder)'''
    except PermissionError:
        continue

