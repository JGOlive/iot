import pandas as pd
from simpful import *

# Pandas File

df = pd.read_csv("Project2_SampleData.csv")
print(df[["MemoryUsage","ProcessorLoad","InpNetThroughput","OutNetThroughput","OutBandwidth","Latency","CLPVariation"]])
# Fuzzy Systems

FS_CPU = FuzzySystem()
FS_FLOW = FuzzySystem()
FS_NET = FuzzySystem()

# CPU Fuzzy System

CPU_Load_01 = FuzzySet( points=[[0, 1.],  [0.40, 1.],  [0.7, 0]], term="low_load" )
CPU_Load_02 = FuzzySet( points=[[0.50, 0.],  [0.70, 1.],  [0.80, 1], [0.90, 0]], term="good_load" )
CPU_Load_03 = FuzzySet( points=[[0.8, 0.],  [0.9, 1.], [1, 1]], term="overload_load" )

FS_CPU.add_linguistic_variable("cpu_load", LinguisticVariable( [CPU_Load_01, CPU_Load_02, CPU_Load_03] ))
# CPU_Mem_01 = CPU_Load_01, CPU_Mem_02 = CPU_Load_02, CPU_Mem_03 = CPU_Load_03

CPU_Mem_01 = FuzzySet( points=[[0, 1.],  [0.40, 1.],  [0.65, 0]], term="high_memory" )
CPU_Mem_02 = FuzzySet( points=[[0.45, 0.],  [0.65, 1.],  [0.75, 1], [0.85, 0]], term="medium_memory" )
CPU_Mem_03 = FuzzySet( points=[[0.75, 0.],  [0.85, 1.], [1, 1]], term="low_memory" )

FS_CPU.add_linguistic_variable("cpu_mem", LinguisticVariable( [CPU_Mem_01, CPU_Mem_02, CPU_Mem_03] ))

FS_CPU.set_crisp_output_value("low_cpu_fs", 0)
FS_CPU.set_crisp_output_value("medium_cpu_fs", 0.5)
FS_CPU.set_crisp_output_value("high_cpu_fs", 1)

FS_CPU.add_rules([
	"IF (cpu_mem IS low_memory) THEN (cpu_fs IS low_cpu_fs)",
	"IF (cpu_mem IS medium_memory) THEN (cpu_fs IS medium_cpu_fs)",
    "IF ((cpu_mem IS high_memory) OR (cpu_load IS overload_load)) THEN (cpu_fs IS medium_cpu_fs)",
	"IF ((cpu_mem IS high_memory) OR (NOT(cpu_load IS overload_load))) THEN (cpu_fs IS high_cpu_fs)"
    ])

'''
FS_CPU.set_variable("cpu_load", 0.6)
FS_CPU.set_variable("cpu_mem", 0.8)

print(FS_CPU.inference())
'''

# Network Fuzzy System

NET_Input_01 = FuzzySet( points=[[0, 1.],  [0.25, 1.], [0.35, 0]], term="low" )
NET_Input_02 = FuzzySet( points=[[0.25, 0.],  [0.35, 1.],  [0.65, 1], [0.75, 0]], term="medium" )
NET_Input_03 = FuzzySet( points=[[0.65, 0.],  [0.75, 1.], [1, 1]], term="high" )

FS_FLOW.add_linguistic_variable("net_input", LinguisticVariable( [NET_Input_01, NET_Input_02, NET_Input_03] ))

NET_Output_01 = FuzzySet( points=[[0, 1.],  [0.25, 1.], [0.35, 0]], term="low" )
NET_Output_02 = FuzzySet( points=[[0.25, 0.],  [0.35, 1.],  [0.65, 1], [0.75, 0]], term="medium" )
NET_Output_03 = FuzzySet( points=[[0.65, 0.],  [0.75, 1.], [1, 1]], term="high" )

FS_FLOW.add_linguistic_variable("net_output", LinguisticVariable( [NET_Output_01, NET_Output_02, NET_Output_03] ))

NET_Bandwidth_01 = FuzzySet( points=[[0, 1.],  [0.25, 1.], [0.35, 0]], term="low" )
NET_Bandwidth_02 = FuzzySet( points=[[0.25, 0.],  [0.35, 1.],  [0.65, 1], [0.75, 0]], term="medium" )
NET_Bandwidth_03 = FuzzySet( points=[[0.65, 0.],  [0.75, 1.], [1, 1]], term="high" )

FS_FLOW.add_linguistic_variable("net_bandwidth", LinguisticVariable( [NET_Bandwidth_01, NET_Bandwidth_02, NET_Bandwidth_03] ))

FS_CPU.set_crisp_output_value("low_flow_fs", 0)
FS_CPU.set_crisp_output_value("medium_flow_fs", 0.5)
FS_CPU.set_output_function("high_flow_fs", 1)


FS_FLOW.add_rules([
	
	])