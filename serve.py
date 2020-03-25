#!/usr/bin/python

print "Content-type: text/html"
print

# Pane see programm kataloogi /home/kasutajanimi/public_html/cgi-bin
# ja ytle samas kasurealt
# chmod a+rx serve.py

# See programm laheb kaima, kui avad urli
# http://dijkstra.cs.ttu.ee/~kasutajanimi/cgi-bin/serve.py

# kasutame neid pythonisse sisse ehitatud standardteeke

import sqlite3
import json 
import cgi
import cgitb

# see annab debugimiseks arusaadavaid veateateid brauserile
cgitb.enable()

# sinu programm, mis pannakse paringu peale kaima

def getdata():
   	
  args = cgi.FieldStorage()
  # vaata, kas urlil anti key, op ja val parameetrid
  key=args.getvalue("key",'')
  op=args.getvalue("op",'')
  val=args.getvalue("val",'') 
  
  # vota baasiga yhendust, valmista ette paring
  conn = sqlite3.connect('data.db')
  cur = conn.cursor()
  
  # hakka kokku panema paringu-sqli, alustades standardosast
  sql="""select id,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10 from maintable """
  
  # kui olid olemas key, op ja val, siis ehita where tingimus
  if key and val:
    if not op: # vaikimisi olgu op =
      op = "="
    # kontrollime, kas parameetrid ok  
    if (not (key in ["id","c1","c2","c3","c4","c5","c6","c7","c8","c9","c10"]) 
        or
        not (op in ["=","<",">","!="])):
      # valed parameetrid, sulge yhendus
      cur.close()
      conn.close()
      # anna veateade ja lopeta
      return('"error"')
    # siin koik ok
    op="like"
    where = " where " + key + op + "?"
    # where c1 like '%sein%';
    #val="%"+val+"%"
    args = [val]
  else:
    where=""
    args=None
    
  # liida where tingimus sql standardosale
  where = " where c1 like '%"+ val +"%'"
  args=None
  sql = sql + where
  
  # liida sql lausele sorteering
  sql = sql + " order by id asc"
  
  # tryki debugimiseks sql lause ja args valja
  # print(sql,args)
  
  # tee paring baasi
  if args:
    cur.execute(sql,args)
  else:
    cur.execute(sql)
    
  # loe koik read sisse, mis paringuga klapivad
  res=cur.fetchall()
  # sulge yhendus
  cur.close()
  conn.close()
  
  # teisenda saadud tulemus json formaati ja anna vastuseks
  print(json.dumps(res))

# see paneb tegelikult programmi algul kaima:

getdata()
