import mysql.connector
from scipy.stats.mstats import gmean

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="password",
  database="benchmark"
)

mycursor = mydb.cursor()

import socket,pickle
s=socket.socket()
host = ''
port=50000
s.bind((host, port))
s.listen(5)
while True:
  c,addr = s.accept()
  data=c.recv(8192)
  bench=pickle.loads(data)

  if(bench[0]==True):
    sqlexectime="INSERT INTO serverexectime (execTimeChaos,execTimeDeltaBlue,execTimeDjangoTemplate,execTimeFloat, \
    execTimeGo,execTimeHexiom,execTimeJsonDumps,execTimeJsonLoads,execTimeMdp,execTimeMeteorContest, \
    execTimeNbody,execTimeNqueens,execTimePidigits,execTimePyflate,execTimeRaytrace,execTimeRegexDna, \
    execTimeRichards,execTimeScimark,execTimeSpectralNorm,execTimeSqliteSynth) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    select="SELECT * FROM serverexectime WHERE idServer=1"
    sql="INSERT INTO server (idServer,model,score) VALUES (%s,%s,%s)"
    order="select idServer from server ORDER BY score DESC"
  else:
    sqlexectime="INSERT INTO pcexectime (execTimeChaos,execTimeDeltaBlue,execTimeDjangoTemplate,execTimeFloat, \
    execTimeGo,execTimeHexiom,execTimeJsonDumps,execTimeJsonLoads,execTimeMdp,execTimeMeteorContest, \
    execTimeNbody,execTimeNqueens,execTimePidigits,execTimePyflate,execTimeRaytrace,execTimeRegexDna, \
    execTimeRichards,execTimeScimark,execTimeSpectralNorm,execTimeSqliteSynth) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    select="SELECT * FROM pcexectime WHERE idPC=1"
    sql="INSERT INTO pc (idPC,model,score) VALUES (%s,%s,%s)"
    order="select idPC from pc ORDER BY score DESC"
  valexectime=tuple(bench[2:])
  mycursor.execute(sqlexectime, valexectime)
  mydb.commit()

  mycursor.execute(select)
  myresult = mycursor.fetchall()
  ref=myresult[0]
  SPEC=[1 for i in range(1,21)]
  for i in range(1,21):
      SPEC[i-1]=ref[i]/valexectime[i-1]
  score=gmean(SPEC)

  mycursor.execute("SELECT LAST_INSERT_ID()");
  myresult = mycursor.fetchall()
  id=myresult[0]
  val=(id[0],bench[1],score)
  mycursor.execute(sql, val)
  mydb.commit()

  mycursor.execute(order)
  myresult = mycursor.fetchall()

  i=0
  while(i<len(myresult)):
      if myresult[i][0]==id[0]:
          break
      i+=1

  result=[i+1,score]
  data=pickle.dumps(result)
  c.send(data)
  c.close()
  
