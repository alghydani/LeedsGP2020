#!/usr/bin/env python
# coding: utf-8

# In[7]:


#--------------------------------------------------------------------------
# File name : Student_python_code
# Author: Mohammed Nidaa Alharbi
# Copyright: © 2020 The University of Leeds and Mohammed Nidaa Alharbi
# Discretion: One of the requirements for the graduation project
# Submitted in accordance with the requirements for the degree
# of MSc Advanced Computer Science - 2019/2020 School of Computing
# ENGINEERING FACULTY - University of Leeds - Leeds, United Lingdom 
#--------------------------------------------------------------------------

# Import Tabula library : to install use this link : https://pypi.org/project/tabula-py/

import tabula
# Import Read_pdf which can read table of PDF. You can read tables from PDF and convert into pandas’s DataFrame., more infomration : https://tabula-py.readthedocs.io/en/latest/
from tabula import read_pdf


# Call the file from the local machine :
# [alternative way] call the file form the online github repository: (SDHH_CVD) link : https://github.com/alghydani/LeedsGP2020/raw/main/SDHH_CVD.pdf
# Then the code will real all the PDF
# then convert it using read_pdf of tabula from PDF string text to a DataFrame then a CSV file 

df = tabula.convert_into("SDHH_CVD.pdf", "JupyterSDHH_CVD.csv", output_format="csv", pages='all')
# df will hold the DataFrame so the next code is going to produce the CSV file


# In[8]:


# import padas and pd to manage the data DataFrame [df]
import pandas as pd 
# data will hold the final file [CSV] from the DataFrame (df) and save in in the local machine as upyterSDHH_CVD_online_code.csv
# output name can be change
data = pd.read_csv("JupyterSDHH_CVD_online_code.csv") 
print (data) # optional to print the output on Jupyter notebook


# In[ ]:




