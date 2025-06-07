import os, stat
import shutil


target_repo_local_path = "target_repo_source2"


def remove_local_directory_fn(target_repo_local_path):
    #delete the local copy of the target repo
    os.chdir("/")
    
    def remove_readonly(func, path, excinfo):
        os.chmod(path, stat.S_IWRITE)
        func(path)

    shutil.rmtree(target_repo_local_path, onexc=remove_readonly)
    print(target_repo_local_path + " deleted successfully")
    return