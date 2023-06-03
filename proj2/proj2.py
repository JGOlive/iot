from simpful import *

FS_CPU = FuzzySystem()
FS_NET = FuzzySystem()

# Fuzzy system responsible for checking if CPU is able to process data

CPU_Load_01 = FuzzySet( points=[[0, 1.],  [0.40, 1.],  [0.7, 0]], term="low_load" )
CPU_Load_02 = FuzzySet( points=[[0.50, 1.],  [0.70, 1.],  [0.80, 0], [0.90, 0]], term="good_load" )
CPU_Load_03 = FuzzySet( points=[[0.8, 1.],  [0.9, 1.], [1, 1]], term="overload_load" )

FS_CPU.add_linguistic_variable("cpu_load", LinguisticVariable( [CPU_Load_01, CPU_Load_02, CPU_Load_03] ))

CPU_Mem_01 = FuzzySet( points=[[0, 1.],  [0.40, 1.],  [0.65, 0]], term="high_memory" )
CPU_Mem_02 = FuzzySet( points=[[0.45, 1.],  [0.65, 1.],  [0.75, 0], [0.85, 0]], term="medium_memory" )
CPU_Mem_03 = FuzzySet( points=[[0.75, 1.],  [0.85, 1.], [1, 1]], term="low_memory" )

FS_CPU.add_linguistic_variable("cpu_mem", LinguisticVariable( [CPU_Mem_01, CPU_Mem_02, CPU_Mem_03] ))

