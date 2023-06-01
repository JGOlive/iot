from simpful import *

FS_CPU = FuzzySystem()
FS_NET = FuzzySystem()

CPU_Load_01 = FuzzySet( points=[[0, 1.],  [0.40, 1.],  [0.7, 0]], term="low_load" )
CPU_Load_02 = FuzzySet( points=[[0.50, 1.],  [0.70, 1.],  [0.80, 0], [0.90, 0]], term="good_load" )
CPU_Load_03 = FuzzySet( points=[[0.8, 1.],  [0.9, 1.], [1, 1]], term="overload_load" )

FS_CPU.add_linguistic_variable("cpu_load", LinguisticVariable( [CPU_Load_01, CPU_Load_02, CPU_Load_03] ))