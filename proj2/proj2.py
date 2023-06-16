import pandas as pd
from simpful import *

# Pandas File
df = pd.read_csv("Project2_SampleData.csv")
print(df[["MemoryUsage","ProcessorLoad","InpNetThroughput","OutNetThroughput","OutBandwidth","Latency","CLPVariation"]])

# Inputs (should be extraced from the pandas dataframe)

cpu_load = 0.5
cpu_mem = 0.5
input_throughput = 0.5
output_throughput = 0.5
latency = 0.5
available_bw = 0.5

# Fuzzy Systems

FS_CPU = FuzzySystem()
FS_NET_US = FuzzySystem()
FS_NET_AV = FuzzySystem()
FS_NET = FuzzySystem()
FIS = FuzzySystem()

# CPU Fuzzy System
CPU_Load_01 = FuzzySet( points=[[0, 1.],  [0.40, 1.],  [0.7, 0]], term="low_load" )
CPU_Load_02 = FuzzySet( points=[[0.50, 0.],  [0.70, 1.],  [0.80, 1], [0.90, 0]], term="good_load" )
CPU_Load_03 = FuzzySet( points=[[0.8, 0.],  [0.9, 1.], [1, 1]], term="overload_load" )

FS_CPU.add_linguistic_variable("cpu_load", LinguisticVariable( [CPU_Load_01, CPU_Load_02, CPU_Load_03] ))

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


# Network Usage
NET_Input_01 = FuzzySet( points=[[0, 1.],  [0.25, 1.], [0.35, 0]], term="low" )
NET_Input_02 = FuzzySet( points=[[0.25, 0.],  [0.35, 1.],  [0.65, 1], [0.75, 0]], term="medium" )
NET_Input_03 = FuzzySet( points=[[0.65, 0.],  [0.75, 1.], [1, 1]], term="high" )

FS_NET_US.add_linguistic_variable("net_input", LinguisticVariable( [NET_Input_01, NET_Input_02, NET_Input_03] ))

NET_Output_01 = FuzzySet( points=[[0, 1.],  [0.25, 1.], [0.35, 0]], term="low" )
NET_Output_02 = FuzzySet( points=[[0.25, 0.],  [0.35, 1.],  [0.65, 1], [0.75, 0]], term="medium" )
NET_Output_03 = FuzzySet( points=[[0.65, 0.],  [0.75, 1.], [1, 1]], term="high" )

FS_NET_US.add_linguistic_variable("net_output", LinguisticVariable( [NET_Output_01, NET_Output_02, NET_Output_03] ))

FS_NET_US.set_crisp_output_value("low", 0)
FS_NET_US.set_crisp_output_value("medium", 0.5)
FS_NET_US.set_crisp_output_value("high", 1)

FS_NET_US.add_rules([
	
	])


# Network Available
NET_Bandwidth_01 = FuzzySet( points=[[0, 1.],  [0.25, 1.], [0.35, 0]], term="low" )
NET_Bandwidth_02 = FuzzySet( points=[[0.25, 0.],  [0.35, 1.],  [0.65, 1], [0.75, 0]], term="medium" )
NET_Bandwidth_03 = FuzzySet( points=[[0.65, 0.],  [0.75, 1.], [1, 1]], term="high" )

FS_NET_AV.add_linguistic_variable("net_bandwidth", LinguisticVariable( [NET_Bandwidth_01, NET_Bandwidth_02, NET_Bandwidth_03] ))

NET_Latency_01 = FuzzySet( points=[[0, 1.],  [0.25, 1.], [0.35, 0]], term="low" )
NET_Latency_02 = FuzzySet( points=[[0.25, 0.],  [0.35, 1.],  [0.65, 1], [0.75, 0]], term="medium" )
NET_Latency_03 = FuzzySet( points=[[0.65, 0.],  [0.75, 1.], [1, 1]], term="high" )

FS_NET_AV.add_linguistic_variable("net_latency", LinguisticVariable( [NET_Latency_01, NET_Latency_02, NET_Latency_03] ))

FS_NET_AV.set_crisp_output_value("low", 0)
FS_NET_AV.set_crisp_output_value("medium", 0.5)
FS_NET_AV.set_crisp_output_value("high", 1)

FS_NET_AV.add_rules([
	
	])


# FIS Fuzzy System
FS_CPU_01 = FuzzySet( points=[[0, 1.],  [0.25, 1.], [0.35, 0]], term="low" )
FS_CPU_02 = FuzzySet( points=[[0.25, 0.],  [0.35, 1.],  [0.65, 1], [0.75, 0]], term="medium" )
FS_CPU_03 = FuzzySet( points=[[0.65, 0.],  [0.75, 1.], [1, 1]], term="high" )

FIS.add_linguistic_variable("fs_cpu", LinguisticVariable( [FS_CPU_01, FS_CPU_02, FS_CPU_03] ))

FS_NET_US_01 = FuzzySet( points=[[0, 1.],  [0.25, 1.], [0.35, 0]], term="low" )
FS_NET_US_02 = FuzzySet( points=[[0.25, 0.],  [0.35, 1.],  [0.65, 1], [0.75, 0]], term="medium" )
FS_NET_US_03 = FuzzySet( points=[[0.65, 0.],  [0.75, 1.], [1, 1]], term="high" )

FIS.add_linguistic_variable("fs_net_us", LinguisticVariable( [FS_NET_US_01, FS_NET_US_02, FS_NET_US_03] ))

FS_NET_AV_01 = FuzzySet( points=[[0, 1.],  [0.25, 1.], [0.35, 0]], term="low" )
FS_NET_AV_02 = FuzzySet( points=[[0.25, 0.],  [0.35, 1.],  [0.65, 1], [0.75, 0]], term="medium" )
FS_NET_AV_03 = FuzzySet( points=[[0.65, 0.],  [0.75, 1.], [1, 1]], term="high" )

FIS.add_linguistic_variable("fs_net_av", LinguisticVariable( [FS_NET_AV_01, FS_NET_AV_02, FS_NET_AV_03] ))

FIS.set_crisp_output_value("low", 0)
FIS.set_crisp_output_value("medium", 0.5)
FIS.set_crisp_output_value("high", 1)

FIS.add_rules([
	
	])

# Calculate the outputs


# Net Usage FS set Inputs/ get Output 
for i in range(4):
	# CPU FS set Inputs/ get Output 
	FS_CPU.set_variable("cpu_load", cpu_load)
	FS_CPU.set_variable("cpu_mem", cpu_mem)

	fs_cpu = FS_CPU.Sugeno_inference("cpu_fs")

	# Net Usage FS set Inputs/ get Output 
	FS_NET_US.set_variable("net_input", input_throughput)
	FS_NET_US.set_variable("net_output", output_throughput)

	fs_net_us = FS_NET_US.Sugeno_inference("net_us_fs")

	# Net Usage FS set Inputs/ get Output 
	FS_NET_AV.set_variable("net_latency", latency)
	FS_NET_AV.set_variable("net_bandwidth", available_bw)

	fs_net_av = FS_NET_AV.Sugeno_inference("net_av_fs")

	# Net Usage FS set Inputs/ get Output 
	FS_NET_AV.set_variable("net_latency", latency)
	FS_NET_AV.set_variable("net_bandwidth", available_bw)

	fis = FS_NET_AV.Sugeno_inference("fis")

