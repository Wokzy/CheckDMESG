import os, shutil, glob


DMESG_SOURCE = '/var/crash'
DMESG_DESTINATION = '/opt/var/crash-log'
DMESG_FILES_LIMIT = 10
DMESG_SOURCE_DIRECTORY_LIMIT = 3


def check_existence(directories):
	for directory in directories:
		folders = glob.glob("*/")
		if f"{directory}/" not in folders:
			os.system(f'mkdir {directory}')
		os.chdir(directory)

def copy_dmesg():
	os.chdir(DMESG_SOURCE)
	
	dir_lst = glob.glob('*/dmesg.*')

	for file in dir_lst:
		shutil.copyfile(file, f"{DMESG_DESTINATION}{file.split('/')[-1]}")

def clean_crashlog():
	os.chdir(DMESG_DESTINATION)

	not_in_top_10 = sorted(glob.iglob('*'), key=os.path.getctime, reverse=True)[DMESG_FILES_LIMIT::]

	for file in not_in_top_10:
		os.system(f'rm -rf {file}')

def clean_crash():
	os.chdir('/var/crash')

	list_without_first_3 = sorted(glob.iglob('*/'), key=os.path.getctime, reverse=True)[DMESG_SOURCE_DIRECTORY_LIMIT::]

	for directory in list_without_first_3:
		if "." not in directory:
			os.system(f"rm -rf {directory}")


os.chdir(f"/{DMESG_SOURCE.split('/')[1]}")
check_existence(DMESG_SOURCE.split('/')[2::])

os.chdir(f"/{DMESG_DESTINATION.split('/')[1]}")
check_existence(DMESG_DESTINATION.split('/')[2::])

copy_dmesg()
clean_crash()
clean_crashlog()
