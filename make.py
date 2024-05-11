import graphlib
from random import randint
from typing import IO
from cyaron import * # ����CYaRon�Ŀ�
for i in range(1, 101) :
    test_data = IO(file_prefix="./data/input", data_id = i, disable_output=True) # ����
    n = randint(4, 20) # ���һ���ڵ����
    m = randint(n, n*(n-1)) # ���һ���ߵ�����
    c = randint(5, 100) # ����Ȩ
    test_data.input_writeln(n, m, c) # д�뵽�����ļ���Զ��Կո�ָ����
    graph = graphlib.DAG(n, m, weight_limit=c) # ����һ��n�㣬m�ߵ����ͼ����Ȩ����Ϊ5
    test_data.input_writeln(graph) # �Զ�д�뵽�����ļ����һ��һ��u v w����ʽ���