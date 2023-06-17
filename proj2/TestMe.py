# Ficheiro para experimentar coisas

import pandas as pd
from simpful import *

# Pandas File

# Project2_SampleData.csv
#df = pd.read_csv("Project2_SampleData.csv")
#print(df[["MemoryUsage","ProcessorLoad","InpNetThroughput","OutNetThroughput","OutBandwidth","Latency","CLPVariation"]])

# Lab10-Proj2_TestS.csv
df = pd.read_csv("Lab10-Proj2_TestS.csv")

# Inputs (should be extraced from the pandas dataframe)
mem_data = df["MemoryUsage"]
proc_data = df["ProcessorLoad"]
input_data = df["InpNetThroughput"]
output_data = df["OutNetThroughput"]
bandwidth_data = df["OutBandwidth"]
latency_data = df["Latency"]
clpv_data = df["CLPVariation"]

# Fuzzy Systems

CPU_LOAD = FuzzySystem()
FS_NET_US = FuzzySystem()
FS_NET_AV = FuzzySystem()
FS_CLPV = FuzzySystem()

# Fuzzyset Template

Template_FuzzySet_01 = FuzzySet( points=[[0, 0], [0, 1.],  [0.25, 1.], [0.5, 0]], term="low" )
Template_FuzzySet_02 = FuzzySet( points=[[0.2, 0.],  [0.4, 1.],  [0.6, 1], [0.8, 0]], term="medium")
Template_FuzzySet_03 = FuzzySet( points=[[0.5, 0.],  [0.75, 1.],  [1, 1.], [1, 0]], term="high" )

# Small Block output template

Template_OUT_Small_01 = FuzzySet( points=[[0, 0], [0, 1.],  [0.20, 1.], [0.5, 0]], term="low" )
Template_OUT_Small_02 = FuzzySet( points=[[0.2, 0.],  [0.4, 1.],  [0.6, 1], [0.8, 0]], term="medium")
Template_OUT_Small_03 = FuzzySet( points=[[0.5, 0.],  [0.80, 1.],  [1, 1.], [1, 0]], term="high" )
'''
CPU_LOAD_OUT_01 = Template_OUT_Small_01
CPU_LOAD_OUT_02 = Template_OUT_Small_02
CPU_LOAD_OUT_03 = Template_OUT_Small_03
'''
# 3 mbf, 5 wouldn't be so predictable to "debug"
Template_OUT_Big_01 = FuzzySet( points=[[-1, 0], [-1, 1.],  [-0.8, 1.], [-0.5, 0]], term="remote" )
#Template_OUT_Big_02 = FuzzySet( points=[, term="semi_static" )
Template_OUT_Big_03 = FuzzySet( points=[[-0.6, 0], [-0.2, 1.],  [0.2, 1.], [0.6, 0]], term="static" )
#Template_OUT_Big_02 = FuzzySet( points=[, term="semi_local" )
Template_OUT_Big_05 = FuzzySet( points=[[ 0.5, 0], [ 0.8, 1.],  [ 1, 1.], [1, 0]], term="local" )

# CPU Fuzzy System
CPU_Ut_01 = FuzzySet( points=[[0, 1.],  [0.40, 1.],  [0.65, 0]], term="low" )
CPU_Ut_02 = FuzzySet( points=[[0.45, 0.],  [0.65, 1.],  [0.75, 1], [0.85, 0]], term="medium" )
CPU_Ut_03 = FuzzySet( points=[[0.75, 0.],  [0.85, 1.], [1, 1]], term="high" )

CPU_LOAD.add_linguistic_variable("cpu_ut", LinguisticVariable( [CPU_Ut_01, CPU_Ut_02, CPU_Ut_03] ))

CPU_Mem_01 = FuzzySet( points=[[0, 1.],  [0.40, 1.],  [0.65, 0]], term="low" )
CPU_Mem_02 = FuzzySet( points=[[0.45, 0.],  [0.65, 1.],  [0.75, 1], [0.85, 0]], term="medium" )
CPU_Mem_03 = FuzzySet( points=[[0.75, 0.],  [0.85, 1.], [1, 1]], term="high" )

CPU_LOAD.add_linguistic_variable("cpu_mem", LinguisticVariable( [CPU_Mem_01, CPU_Mem_02, CPU_Mem_03] ))

CPU_LOAD_OUT_01 = Template_OUT_Small_01
CPU_LOAD_OUT_02 = Template_OUT_Small_02
CPU_LOAD_OUT_03 = Template_OUT_Small_03

CPU_LOAD.add_linguistic_variable("cpu_load", LinguisticVariable( [CPU_LOAD_OUT_01, CPU_LOAD_OUT_02, CPU_LOAD_OUT_03], universe_of_discourse=[0,1] ))

CPU_LOAD.add_rules([
	"IF ((cpu_ut IS high) OR (cpu_mem IS high)) THEN (cpu_load IS high)",
	"IF ((cpu_ut IS medium) AND (cpu_mem IS medium)) THEN (cpu_load IS medium)",
	"IF ((cpu_ut IS medium) AND (cpu_mem IS low)) THEN (cpu_load IS low)",
	"IF ((cpu_ut IS low) AND ((cpu_mem IS low) OR (cpu_mem IS medium))) THEN (cpu_load IS low)"
    ])


# Network Usage
NET_Input_01 = Template_FuzzySet_01
NET_Input_02 = Template_FuzzySet_02
NET_Input_03 = Template_FuzzySet_03

FS_NET_US.add_linguistic_variable("net_input", LinguisticVariable( [NET_Input_01, NET_Input_02, NET_Input_03] ))

NET_Output_01 = Template_FuzzySet_01
NET_Output_02 = Template_FuzzySet_02
NET_Output_03 = Template_FuzzySet_03

FS_NET_US.add_linguistic_variable("net_output", LinguisticVariable( [NET_Output_01, NET_Output_02, NET_Output_03] ))

FS_NET_US_OUT_01 = Template_OUT_Small_01
FS_NET_US_OUT_02 = Template_OUT_Small_02
FS_NET_US_OUT_03 = Template_OUT_Small_03

FS_NET_US.add_linguistic_variable("net_us_fs", LinguisticVariable( [FS_NET_US_OUT_01, FS_NET_US_OUT_02, FS_NET_US_OUT_03], universe_of_discourse=[0,1]))

FS_NET_US.add_rules([
	"IF ((net_input IS low) OR (net_output IS high)) THEN (net_us_fs IS low)",
	"IF ((net_input IS medium) AND (net_output IS medium)) THEN (net_us_fs IS low)",
	"IF ((net_input IS medium) AND (net_output IS low)) THEN (net_us_fs IS medium)",
	"IF ((net_input IS high) AND (net_output IS medium)) THEN (net_us_fs IS medium)",
	"IF ((net_input IS high) AND (net_output IS low)) THEN (net_us_fs IS high)"
	])


# Network Available
NET_Bandwidth_01 = Template_FuzzySet_01
NET_Bandwidth_02 = Template_FuzzySet_02
NET_Bandwidth_03 = Template_FuzzySet_03

FS_NET_AV.add_linguistic_variable("net_bandwidth", LinguisticVariable( [NET_Bandwidth_01, NET_Bandwidth_02, NET_Bandwidth_03] ))

NET_Latency_01 = Template_FuzzySet_01
NET_Latency_02 = Template_FuzzySet_02
NET_Latency_03 = Template_FuzzySet_03

FS_NET_AV.add_linguistic_variable("net_latency", LinguisticVariable( [NET_Latency_01, NET_Latency_02, NET_Latency_03] ))

FS_NET_AV_OUT_01 = Template_OUT_Small_01
FS_NET_AV_OUT_02 = Template_OUT_Small_02
FS_NET_AV_OUT_03 = Template_OUT_Small_03

FS_NET_AV.add_linguistic_variable("net_av_fs", LinguisticVariable( [FS_NET_AV_OUT_01, FS_NET_AV_OUT_02, FS_NET_AV_OUT_03], universe_of_discourse=[0,1] ))

FS_NET_AV.add_rules([
	"IF ((net_bandwidth IS low) OR (net_latency IS high)) THEN (net_av_fs IS low)",
	"IF (((net_latency IS medium) OR (net_latency IS low)) AND (net_bandwidth IS medium)) THEN (net_av_fs IS medium)",
	"IF (((net_latency IS medium) OR (net_latency IS low)) AND (net_bandwidth IS high)) THEN (net_av_fs IS high)"
	])


# FS_CLPV Fuzzy System
FS_CPU_01 = Template_FuzzySet_01
FS_CPU_02 = Template_FuzzySet_02
FS_CPU_03 = Template_FuzzySet_03

FS_CLPV.add_linguistic_variable("fs_cpu", LinguisticVariable( [FS_CPU_01, FS_CPU_02, FS_CPU_03] ))

FS_NET_US_01 = Template_FuzzySet_01
FS_NET_US_02 = Template_FuzzySet_02
FS_NET_US_03 = Template_FuzzySet_03

FS_CLPV.add_linguistic_variable("fs_net_us", LinguisticVariable( [FS_NET_US_01, FS_NET_US_02, FS_NET_US_03] ))

FS_NET_AV_01 = Template_FuzzySet_01
FS_NET_AV_02 = Template_FuzzySet_02
FS_NET_AV_03 = Template_FuzzySet_03

FS_CLPV.add_linguistic_variable("fs_net_av", LinguisticVariable( [FS_NET_AV_01, FS_NET_AV_02, FS_NET_AV_03] ))

CPLV_OUT_01 = Template_OUT_Big_01
CPLV_OUT_03 = Template_OUT_Big_03
CPLV_OUT_05 = Template_OUT_Big_05

FS_CLPV.add_linguistic_variable("clpv", LinguisticVariable( [CPLV_OUT_01, CPLV_OUT_03, CPLV_OUT_05], universe_of_discourse=[-1,1] ))


FS_CLPV.add_rules([
    "IF (fs_cpu IS low) THEN (clpv IS local)",
    "IF ((fs_cpu IS medium) AND ((fs_net_av IS low) AND (fs_net_us IS low) ) )      THEN (clpv IS local)",
    "IF ((fs_cpu IS medium) AND ((fs_net_av IS low) AND (fs_net_us IS medium) ) )   THEN (clpv IS local)",
    "IF ((fs_cpu IS medium) AND ((fs_net_av IS low) AND (fs_net_us IS high) ) )     THEN (clpv IS local)",
    "IF ((fs_cpu IS medium) AND ((fs_net_av IS medium) AND (fs_net_us IS low) ) )   THEN (clpv IS static)",
    "IF ((fs_cpu IS medium) AND ((fs_net_av IS medium) AND (fs_net_us IS medium) ) ) THEN (clpv IS local)",
    "IF ((fs_cpu IS medium) AND ((fs_net_av IS medium) AND (fs_net_us IS high) ) )  THEN (clpv IS local)",
    "IF ((fs_cpu IS medium) AND ((fs_net_av IS high) AND (fs_net_us IS low) ) )     THEN (clpv IS remote)",
    "IF ((fs_cpu IS medium) AND ((fs_net_av IS high) AND (fs_net_us IS medium) ) )  THEN (clpv IS static)",
    "IF ((fs_cpu IS medium) AND ((fs_net_av IS high) AND (fs_net_us IS high) ) )    THEN (clpv IS local)",
    "IF ((fs_cpu IS high) AND ((fs_net_av IS high) OR (fs_net_us IS low) ) ) THEN (clpv IS remote)",
    "IF ((fs_cpu IS high) AND ((fs_net_av IS medium) AND (fs_net_us IS medium) ) ) THEN (clpv IS remote)",
    "IF ((fs_cpu IS high) AND ((fs_net_av IS low) AND (fs_net_us IS medium) ) ) THEN (clpv IS static)",
    "IF ((fs_cpu IS high) AND ((fs_net_av IS medium) AND (fs_net_us IS high) ) ) THEN (clpv IS static)",
    "IF ((fs_cpu IS high) AND ((fs_net_av IS low) AND (fs_net_us IS high) ) ) THEN (clpv IS local)"
])


# Calculate the outputs

for i in range(len(mem_data)):

	cpu_ut = proc_data[i]
	cpu_mem = mem_data[i]
	input_throughput = input_data[i]
	output_throughput = output_data[i]
	latency = latency_data[i]
	available_bw = bandwidth_data[i]

	# CPU FS set Inputs/ get Output 
	CPU_LOAD.set_variable("cpu_ut", cpu_ut)
	CPU_LOAD.set_variable("cpu_mem", cpu_mem)

	cpu_load = CPU_LOAD.inference()
	cpu_load_output = cpu_load["cpu_load"]

	# Net Usage FS set Inputs/ get Output 
	FS_NET_US.set_variable("net_input", input_throughput)
	FS_NET_US.set_variable("net_output", output_throughput)

	fs_net_us = FS_NET_US.inference()
	fs_net_us_output = fs_net_us["net_us_fs"]

	# Net Usage FS set Inputs/ get Output 
	FS_NET_AV.set_variable("net_latency", latency)
	FS_NET_AV.set_variable("net_bandwidth", available_bw)

	fs_net_av = FS_NET_AV.inference(["net_av_fs"])
	fs_net_av_output = fs_net_av["net_av_fs"]

	# Net Usage FS set Inputs/ get Output 
	FS_CLPV.set_variable("fs_cpu", cpu_load_output)
	FS_CLPV.set_variable("fs_net_us", fs_net_us_output)
	FS_CLPV.set_variable("fs_net_av", fs_net_av_output)

	clpv = FS_CLPV.inference(["clpv"])
	clpv_ouput = clpv["clpv"]

	print( "CLPV (File):",clpv_data[i],"\t","CLPV (Predicted):",clpv_ouput)

