from tkinter import*
from tkinter import ttk
import socket,pickle
import cpuinfo
import multiprocessing

import sys
sys.path.insert(0, './Benchmarks')
import chaos
import deltablue
import django_template
import floatb
import go
import hexiom
import json_dumps
import json_loads
import mdp
import meteor_contest
import nbody
import nqueens
import pidigits
import pyflate
import raytrace
import regex_dna
import richards
import scimark
import spectral_norm
import sqlite_synth

isServer=False
model=cpuinfo.get_cpu_info()['brand']
pool = multiprocessing.Pool(processes=1)
pool.terminate()
servers=["Xeon","EPYC","Opteron","Itanium","Sparc"]
for server in servers:
    if server in model:
        isServer=True

fenetre1=Tk()
fenetre1.title("CPU Benchmark Test")
frame1 = ttk.Frame(fenetre1)
frame1.grid(column=0, row=0, sticky=(N,W,E,S))
l=ttk.Label(frame1,text="Vanessa Chahwan, \n Walid Samaha, \n Tatiana Wakim").grid(column=2, row=5, rowspan=8, padx=40)
li=ttk.Label(frame1,text="Presented By: " ).grid(column=1, row=4, padx=10)

execTimeChaos=DoubleVar()
execTimeDeltaBlue=DoubleVar()
execTimeDjangoTemplate=DoubleVar()
execTimeFloat=DoubleVar()
execTimeGo=DoubleVar()
execTimeHexiom=DoubleVar()
execTimeJsonDumps=DoubleVar()
execTimeJsonLoads=DoubleVar()
execTimeMdp=DoubleVar()
execTimeMeteorContest=DoubleVar()
execTimeNbody=DoubleVar()
execTimeNqueens=DoubleVar()
execTimePidigits=DoubleVar()
execTimePyflate=DoubleVar()
execTimeRaytrace=DoubleVar()
execTimeRegexDna=DoubleVar()
execTimeRichards=DoubleVar()
execTimeScimark=DoubleVar()
execTimeSpectralNorm=DoubleVar()
execTimeSqliteSynth=DoubleVar()
rank=DoubleVar()
score=DoubleVar()

   
def benchmark():
    s = socket.socket()
    host = socket.gethostname()
    port=50000
    s.connect((host, port))
    bench=[isServer,model]

    time=chaos.time()
    execTimeChaos.set(time)
    bench.append(time)

    time=deltablue.time()
    execTimeDeltaBlue.set(time)
    bench.append(time)

    time=django_template.time()
    execTimeDjangoTemplate.set(time)
    bench.append(time)

    time=floatb.time()
    execTimeFloat.set(time)
    bench.append(time)

    time=go.time()
    execTimeGo.set(time)
    bench.append(time)

    time=hexiom.time()
    execTimeHexiom.set(time)
    bench.append(time)

    time=json_dumps.time()
    execTimeJsonDumps.set(time)
    bench.append(time)    

    time=json_loads.time()
    execTimeJsonLoads.set(time)
    bench.append(time)

    time=mdp.time()
    execTimeMdp.set(time)
    bench.append(time)

    time=meteor_contest.time()
    execTimeMeteorContest.set(time)
    bench.append(time)

    time=nbody.time()
    execTimeNbody.set(time)
    bench.append(time)

    time=nqueens.time()
    execTimeNqueens.set(time)
    bench.append(time)
    
    time=pidigits.time()
    execTimePidigits.set(time)
    bench.append(time)

    time=pyflate.time()
    execTimePyflate.set(time)
    bench.append(time)
    
    time=raytrace.time()
    execTimeRaytrace.set(time)
    bench.append(time)

    time=regex_dna.time()
    execTimeRegexDna.set(time)
    bench.append(time)
    
    time=richards.time()
    execTimeRichards.set(time)
    bench.append(time)

    time=scimark.time()
    execTimeScimark.set(time)
    bench.append(time)
    
    time=spectral_norm.time()
    execTimeSpectralNorm.set(time)
    bench.append(time)

    time=sqlite_synth.time()
    execTimeSqliteSynth.set(time)
    bench.append(time)

    data=pickle.dumps(bench)
    s.send(data)
    data=s.recv(1024)
    result=pickle.loads(data)

    rank.set(result[0])
    score.set(result[1])
    s.close()

def gui():           
    fenetre2=Toplevel(fenetre1)
    fenetre2.title("Scores and Ranking")
    frame2 = ttk.Frame(fenetre2)
    frame2.grid(column=0, row=0, sticky=(N,W,E,S))
    button1=ttk.Button(frame2, text="START", command=benchmark).grid(column=0, row=0, padx=20, pady=40)

    label1=ttk.Label(frame2,text="Chaos").grid(column=0, row=1, columnspan=2, padx=40)
    Label=ttk.Label(frame2, textvariable=execTimeChaos).grid(column=5, row=1,  padx=40)
    label2=ttk.Label(frame2,text="Delta Blue").grid(column=0, row=2, columnspan=2, padx=40)
    Label=ttk.Label(frame2, textvariable=execTimeDeltaBlue).grid(column=5, row=2,  padx=40)
    label3=ttk.Label(frame2,text="Django Template").grid(column=0, row=3, columnspan=2, padx=40)
    Label=ttk.Label(frame2, textvariable=execTimeDjangoTemplate).grid(column=5, row=3,  padx=40)
    label4=ttk.Label(frame2,text="Float").grid(column=0, row=4, columnspan=2, padx=40)
    Label=ttk.Label(frame2, textvariable=execTimeFloat).grid(column=5, row=4,  padx=40)
    label5=ttk.Label(frame2,text="Go").grid(column=0, row=5, columnspan=2, padx=40)
    Label=ttk.Label(frame2, textvariable=execTimeFloat).grid(column=5, row=5,  padx=40)
    label6=ttk.Label(frame2,text="Hexiom").grid(column=0, row=6, columnspan=2, padx=40)
    Label=ttk.Label(frame2, textvariable=execTimeHexiom).grid(column=5, row=6,  padx=40)
    label7=ttk.Label(frame2,text="Json Dumps").grid(column=0, row=7, columnspan=2, padx=40)
    Label=ttk.Label(frame2, textvariable=execTimeJsonDumps).grid(column=5, row=7,  padx=40)
    label8=ttk.Label(frame2,text="Json Loads").grid(column=0, row=8, columnspan=2, padx=40)
    Label=ttk.Label(frame2, textvariable=execTimeJsonLoads).grid(column=5, row=8,  padx=40)
    label9=ttk.Label(frame2,text="Mdp").grid(column=0, row=9, columnspan=2, padx=40)
    Label=ttk.Label(frame2, textvariable=execTimeMdp).grid(column=5, row=9,  padx=40)
    label10=ttk.Label(frame2,text="Meteor Contest").grid(column=0, row=10, columnspan=2, padx=40)
    Label=ttk.Label(frame2, textvariable=execTimeMeteorContest).grid(column=5, row=10,  padx=40)
    label11=ttk.Label(frame2,text="Nbody").grid(column=0, row=11, columnspan=2, padx=40)
    Label=ttk.Label(frame2, textvariable=execTimeNbody).grid(column=5, row=11,  padx=40)
    label12=ttk.Label(frame2,text="Nqueens").grid(column=0, row=12, columnspan=2, padx=40)
    Label=ttk.Label(frame2, textvariable=execTimeNqueens).grid(column=5, row=12,  padx=40)
    label13=ttk.Label(frame2,text="Pidigits").grid(column=0, row=13, columnspan=2, padx=40)
    Label=ttk.Label(frame2, textvariable=execTimePidigits).grid(column=5, row=13,  padx=40)
    label14=ttk.Label(frame2,text="Pyflate").grid(column=0, row=14, columnspan=2, padx=40)
    Label=ttk.Label(frame2, textvariable=execTimePyflate).grid(column=5, row=14,  padx=40)
    label15=ttk.Label(frame2,text="Raytace").grid(column=0, row=15, columnspan=2, padx=40)
    Label=ttk.Label(frame2, textvariable=execTimeRaytrace).grid(column=5, row=15,  padx=40)
    label16=ttk.Label(frame2,text="Regex DNA").grid(column=0, row=16, columnspan=2, padx=40)
    Label=ttk.Label(frame2, textvariable=execTimeRegexDna).grid(column=5, row=16, padx=40)
    label17=ttk.Label(frame2,text="Richards").grid(column=0, row=17, columnspan=2, padx=40)
    Label=ttk.Label(frame2, textvariable=execTimeRichards).grid(column=5, row=17,  padx=40)
    label18=ttk.Label(frame2,text="Scimark").grid(column=0, row=18, columnspan=2, padx=40)
    Label=ttk.Label(frame2, textvariable=execTimeScimark).grid(column=5, row=18, padx=40)
    label19=ttk.Label(frame2,text="Spectral Norm").grid(column=0, row=19, columnspan=2, padx=40)
    Label=ttk.Label(frame2, textvariable=execTimeSpectralNorm).grid(column=5, row=19,  padx=40)
    label20=ttk.Label(frame2,text="Sqlite Synth").grid(column=0, row=20, columnspan=2, padx=40)
    Label=ttk.Label(frame2, textvariable=execTimeSqliteSynth).grid(column=5, row=20,  padx=40)
    

    label21=ttk.Label(frame2,text="TOTAL SCORE").grid(column=4, row=21, pady=40)
    label22=ttk.Label(frame2,text="RANK").grid(column=4, row=22,pady=10)
    label23=ttk.Label(frame2,text="TIME").grid(column=5, row=0, pady=20, padx=40)
    Label=ttk.Label(frame2, textvariable=score).grid(column=5, row=21, pady=20)
    Label=ttk.Label(frame2, textvariable=rank).grid(column=5, row=22)


button=ttk.Button(frame1, text="CPU Benchmark", command=gui).grid(column=2, row=2, padx=50, pady=50)
fenetre1.mainloop()
