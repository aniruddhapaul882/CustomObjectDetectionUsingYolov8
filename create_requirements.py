import subprocess

########################################################################################
# This function might not required all the time if the system failed to make the "requirements.txt" then it can be used
def make_requirements_text_file():
    try:
        complete_subprocess = subprocess.run('type nul > requirements.txt', shell=True)
        if complete_subprocess.returncode == 0:
            print('requirements file created')
            return True
        else:
            print('failed to create requirements file')
            return False

    except Exception as e:
        print("error occoured while creating requirements file as: ", e)
        return False
########################################################################################
def get_installed_packages():
    try:
        #Use subprocess to run pip list commands and capture the output into a text file
        complete_process = subprocess.run(['pip', 'list'], capture_output=True, text=True)
        if complete_process.returncode == 0:
            # split the outputs into lines and skip header
            lines = complete_process.stdout.strip().split('\n')[2:]
            #extract packages names and version
            packages = [line.split()[:2] for line in lines]
            return packages
        else:
            print("Error occurred while getting installed packages.")
            return []

    except Exception as e:
        print("Error occurred while getting installed packages", e)
        return []

def write_requirements_file(packages, filename='requirements.txt'):
    with open(filename, 'w') as file:
        for package in packages:
            file.write(f"{package[0]}=={package[1]}\n")
    print(f"successfully created {filename} with {len(packages)} packages.")


if __name__ == "__main__":
    file_creation = make_requirements_text_file() # use only if system failed to make the "requirements.txt"
    if file_creation: # use only if system failed to make the "requirements.txt" aslo correct the indentation if not using this "if loop"
        installed_packages = get_installed_packages()
        if installed_packages:
            write_requirements_file(installed_packages)
        else:
            print("No packages found. Make sure you have Python packages installed.")

    else: # use only if system failed to make the "requirements.txt"
        print("failed!") # use only if system failed to make the "requirements.txt"
