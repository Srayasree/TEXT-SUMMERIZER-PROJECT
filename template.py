import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')
project_name = "TextSummrizer"#project name

#Defines a list of all the files and folders to be created. 
# It uses f-strings to dynamically create paths within the src directory based on the project_name.
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/conponents/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/utils/configuration.py", 
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml", # Corrected to params.yaml 
    "main.py",
    "Dockerfile", # Corrected to Dockerfile
    "requirements.txt",
    "setup.py",
    "test.py",
    "research/trials.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath)  #iteraate throgh the list of files and 
    #create string path for each file or directory.

    filedir, filename = os.path.split(filepath) 
    
    if filedir:  # Check if filedir is not empty
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir} for the file: {filename}")

    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        with open(filepath, 'w') as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} is already exists")

#Defines a list of files and folders for a project.
#Iterates through this list.
#Creates any necessary directories.
#Creates empty files if they don't exist or are empty.
#Logs information about the process.