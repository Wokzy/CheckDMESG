import os, shutil, glob

def copy_dmesg():
	os.chdir('/var/crash')
	dir_lst = glob.glob('*/dmesg.*')

	for file in dir_lst:
		shutil.copyfile(file, f"/opt/var/log/crash-log/{file.split('/')[-1]}")

def clean_crashlog():
	os.chdir('/opt/var/log/crash-log')

	not_in_top_10 = sorted(glob.iglob('*'), key=os.path.getctime, reverse=True)[10::]

	for file in not_in_top_10:
		os.system(f'rm -rf {file}')

def clean_crash():
	os.chdir('/var/crash')

	list_without_first_3 = sorted(glob.iglob('*/'), key=os.path.getctime, reverse=True)[3::]

	for directory in list_without_first_3:
		if "." not in directory:
			os.system(f"rm -rf {directory}")

copy_dmesg()
clean_crash()
clean_crashlog()
