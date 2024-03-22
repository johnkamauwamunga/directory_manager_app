import os
import shutil

def distribute_files(sourcedir, targetdir):
    print("Source directory:", sourcedir)
    print("Target directories:", targetdir)
    
    for tdir in targetdir:
        os.makedirs(tdir, exist_ok=True)

    files = sorted(os.listdir(sourcedir), key=lambda x: os.path.getsize(os.path.join(sourcedir, x)))
    print("Files in source directory:", files)
    
    if len(files) == 0:
        print("No files found in the directory.")
        return
    
    #checking the siize of dirrectories,atleatsone file
    csize = max(len(files) // len(targetdir), 1)  
    cks = [files[i:i+csize] for i in range(0, len(files), csize)]
    
    for i, ck in enumerate(cks):
        for file in ck:
            sourcepath = os.path.join(sourcedir, file)
            targetpath = os.path.join(os.path.expanduser(targetdir[i]), file)
            print("Move", sourcepath, "to", targetpath)
            shutil.move(sourcepath, targetpath)
    
    
def main():
    sourcedir = os.path.expanduser("~/Music/jay")  #pick the directory to move files from
    targetdir = [f"~/dir/{i+1}" for i in range(8)]  # Creating target directories
    targetdir = [os.path.expanduser(directory) for directory in targetdir]  

    distribute_files(sourcedir, targetdir)

if __name__ == "__main__":
    main()
