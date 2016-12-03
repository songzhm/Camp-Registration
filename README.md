# Camp-Registration

Build Status: 

[![Build Status](https://travis-ci.com/songzhm/Camp-Registration.svg?token=eZqkyDBTstz7c4k1na4p&branch=master)](https://travis-ci.com/songzhm/Camp-Registration)

Code Coverage Status:

[![codecov](https://codecov.io/gh/songzhm/Camp-Registration/branch/master/graph/badge.svg?token=rm8ZPBOsT9)](https://codecov.io/gh/songzhm/Camp-Registration)

class project
develop env python 3 + sqlite 3

* presentation link:

    https://docs.google.com/presentation/d/1L_-4Jkg8OemI2luZm-QX5eM7_qbGQ4OcVQhDDl0vVZU/edit?usp=sharing

* In ordert to look at our SCRUM Big Board, please add ZenHub plugin to Github:

    https://www.zenhub.com/

* Build exe file (replace "C:\Users\Ming\AppData\..." with your local PyQt4 path)
    `PyInstaller -y -F --distpath="." -p "C:\Users\Ming\AppData\Local\Programs\Python\Python35\Lib\site-packages\PyQt4" --windowed main.py`

Linux Configure Process:

* Download miniconda: http://conda.pydata.org/miniconda.html
* Install: `bash MIniconda3-latest-Linux-x86_64.sh`
* Create py35 env: `conda create -n camp python=3.5.1`
* Activate py351 env: `source activate camp`
* Install pyqt4 via conda: `conda install -c anaconda pyqt=4.11.4`
