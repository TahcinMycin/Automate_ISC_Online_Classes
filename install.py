import os

# Creating a Auto package installer

def install(package):
    command = "pip install " + package
    os.system(command)
    return
  
# Main code starts from here:

if __name__ == "__main__":
    install("pyautogui")
    install("keyboard")
    install("requests")
