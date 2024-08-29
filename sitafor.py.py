import time

r=["🔴","🟡","🟢"]
p=["🧍","🏃"]

while True:
 q=10
 while q>=1:
  print("\r",r[0],str(q),p[1],end="")
  time.sleep(1)
  q-=1
 s=1
 while s>=1:
  print("\r",r[1],str(s),p[1],end="")
  time.sleep(1)
  s-=1
 y=10
 while y>=1:
  print("\r",r[2],str(y), p[0],end="")
  time.sleep(1)
  y-=1
