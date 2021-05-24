# For creating the 'virtualenv' for the project, use the following command :


conda create - n vbo_env

"""
    vbo_env : name of the new virtual environment to be created
"""


# For creating the 'virtualenv' with spesific version of python, use the following command :

conda create - n vbo_env python = 3

# You can use the following command to activate the current environment:

conda activate vbo_env

# Listing all of the installed packages inside the current environment:

conda list

# Install package with spesific version or last version:
# - If the version is specified, the package is installed with the relevant version,
# - if not, the installation is performed with the latest version.

conda install numpy pandas = 1.2.1

"""
    the latest version of numpy & 1.2.1 version of the pandas are installed
"""

# Checking the version of the specific package in current environment (etc:numpy?):

python - c "import numpy; print(numpy.__version__)"

# Checking the list or version of the packages:

conda list

# For the uninstallation of the package, use the following command (for instance, numpy):

conda remove numpy

# For performing updates, use the following command: for instance, pandas)

conda update pandas

# Saving the packages to a YAML file:

conda env export > vbo_env_packages.yaml

# The following command removes the 'vbo_env' Virtual Environment with all its packages at the same time.

# - Firstly, deactive the current environment.

conda deactivate

# - Secondly, remove the 'vbo_env' Virtual Environment

conda env remove - n vbo_env
