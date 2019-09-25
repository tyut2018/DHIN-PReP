import sys
from os import path
import datetime
import numpy as np
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from src.DHIN_PReP import PReP
from src.load import load_matrix, load_pair2node


matrix_file = 'E:/hujialun/dhin-prep/dhin-prep/data1/matrix.txt'
pair2node_file = 'E:/hujialun/dhin-prep/dhin-prep/data1/pair2node.txt'
model_file = 'E:/hujialun/dhin-prep/dhin-prep/data1/exam1.model'
num_clus = 15
beta = 1.e-4


t_load_start = datetime.datetime.now()
w = load_matrix(matrix_file)
pair2node = load_pair2node(pair2node_file)
assert w.shape[0] == len(pair2node)
t_load_end = datetime.datetime.now()
print ("Finish loading using", t_load_end - t_load_start)

prep = PReP(w, pair2node, model_file, num_clus=num_clus, beta=beta)
prep.fit(50)