import os
import subprocess

directory_name = "Ultraviolet-App"

if not os.path.exists(directory_name):
    print(f"{directory_name} does not exist. Cloning and installing...")

    try:
        subprocess.run(["git", "clone", "https://github.com/titaniumnetwork-dev/Ultraviolet-App.git"], check=True)
        os.chdir(directory_name)
        subprocess.run(["npm", "install"], check=True)
        subprocess.run(["npm", "start"], check=True)

    except subprocess.CalledProcessError as e:
        print(f"Error during cloning/installation/start: {e}")
        print(f"Command output: {e.output}")

    except FileNotFoundError as e:
        print(f"Error: {e}. Make sure git and npm are installed.")

else:
    print(f"{directory_name} exists. Starting...")
    try:
        os.chdir(directory_name)
        subprocess.run(["npm", "start"], check=True)

    except subprocess.CalledProcessError as e:
        print(f"Error during start: {e}")
        print(f"Command output: {e.output}")

    except FileNotFoundError as e:
        print(f"Error: {e}. Make sure npm is installed.")
