import os, sys, pathlib
import pypdf
from typing import *
from types import *

def append_files(*files: str, new_name: str):
    new_file = pypdf.PdfWriter(incremental=True)
    for file in files:
        new_file.append(file)
    new_file.write("f{new_name}.pdf")

def remove_pages(pgs: List, file: str, new_name: str):
    f = pypdf.PdfWriter(incremental=True)
    j = 1
    for i in pypdf.PdfReader(file).pages:
        if j not in pgs:
            f.append(i)
    f.write("f{new_name}.pdf")




