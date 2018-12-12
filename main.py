import os
import subprocess
from paint_datas.digits_recognition import module2 as dr

def main():
    #os.system("/paint_datas/application.windows64/paint_datas.exe")
    dr.main()

    #subprocess.call('python paint_datas/digits_recognition/module2.py', shell=True)


if __name__ == "__main__":
    main()