import subprocess
import pandas as pd
import openpyxl
import os
BaseFolder = input('複数のエクセルファイルが入っているフォルダを入力　>> ')
if(BaseFolder[-1:]!="\\"):
    BaseFolder=BaseFolder + '\\'
Files=os.listdir(BaseFolder)
ExlFiles=[f for f in Files if f.endswith(".xlsx") or f.endswith(".xls")]
for FileName in os.listdir(BaseFolder):
    if FileName.endswith(".xlsx"):
        ExlFiles.append(FileName)
for File in ExlFiles:
    df=pd.read_excel(os.path.join(BaseFolder, File))
    df.to_csv(os.path.join(BaseFolder, File.replace(".xlsx", ".csv").replace(".xls", ".csv")), index=False, encoding='utf-8-sig')