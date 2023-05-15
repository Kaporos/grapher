import os
import graph
import time
import sys
import ctypes


try:
    result = ctypes.windll.user32.MessageBoxW(None, "Show graph (YES) or generate png (NO)", "Question", 4)
    folder = sys.argv[1]
    lgraph = graph.Graph.parse(folder)
    lgraph.plot(show=(result==6))
except Exception as e:
    print("error: ", e)
"""
subfolders = [ f.path for f in os.scandir("./graphs") if f.is_dir() ]

for folder in subfolders:
    lgraph = graph.Graph.parse(folder)
    lgraph.plot()
"""
print("Graphs generated !")
input("Waiting for you to press enter..")