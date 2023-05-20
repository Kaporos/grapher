import os
import graph
import time
import sys
import ctypes


try:
    folder = sys.argv[1]
    lgraph = graph.Graph.parse(folder)
    lgraph.plot()
except Exception as e:
    print("error: ", e)
    input("")
"""
subfolders = [ f.path for f in os.scandir("./graphs") if f.is_dir() ]

for folder in subfolders:
    lgraph = graph.Graph.parse(folder)
    lgraph.plot()
"""
print("Graphs generated !")
