from simpful import *

FS1 = FuzzySystem()

TLV1 = AutoTriangle(3, terms=["Cold", "Warm", "Hot"], universe_of_discourse=[0,100])
TLV2 = AutoTriangle(3, terms=["Slow", "Normal", "Turbo"], universe_of_discourse=[0,5])

FS1.add_linguistic_variable("CPU_Temp", TLV1)
FS1.add_linguistic_variable("CPU_Speed", TLV2)

O1 = TriangleFuzzySet(0,0,50,   term="Slow")
O2 = TriangleFuzzySet(0,50,100,  term="Medium")
O3 = TriangleFuzzySet(50,100,100, term="Fast")
FS1.add_linguistic_variable("Fan_Speed_%", LinguisticVariable([O1, O2, O3], universe_of_discourse=[0,100]))

FS1.add_rules([
    "IF (CPU_Speed IS Turbo) THEN (Fan_Speed_% IS Fast)"
    "IF (CPU_Temp IS Hot) THEN (Fan_Speed_% IS Fast)"
     
    ])