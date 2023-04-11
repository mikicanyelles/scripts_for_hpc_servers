#!/bin/bash

# USAGE: configure.sh CHEMSHELL_DIR [PYTHON_ROUTE]
#   if no route is specified for Python, conda env will be created and required 
#   packages will be installed will be installed.

sed -i "s/{{chemshell_dir}}/$1/g" *.chemsh

if [ -z "$2" ]; 
    then
        conda create -n scripts_for_hpc_servers
        conda activate scripts_for_hpc_servers
        conda config --add channels conda-forge
        conda install mdanalysis plotext matplotlib tabulate

        PYTHON_ROUTE=/home/$USER/miniconda3/envs/scripts_for_hpc_servers/bin/python
        sed -i "s/{{python_route}}/$PYTHON_ROUTE/g" *.py

    else
        pip3 install mdanalysis plotext matplotlib tabulate

        sed -i "s/{{python_route}}/$2/g" *.py

    fi

CURRENT_PATH="$(dirname -- "${BASH_SOURCE[0]}")"

echo "PATH=\$PATH:$CURRENT_PATH" >> ~/.bashrc


