def isLen(num,l):
  return (len(str(num)) == l)

def no7(num):
  for i in str(num):
    if i=="7":
      return False
  return True  

def only7(num,place):
  for nu, i in enumerate(str(num)):
    if (len(str(num))-nu)==place and i!="7":
      return False
    if (len(str(num))-nu)!=place and i=="7": 
      return False
  return True 

def longdiv(div, fac, D, Q, M, R):
  #check constraints on div and fac
  dl = len(str(div))
  fl = len(str(fac))
  D.append(int(str(div)[:len(str(fac))]))
  for i in range(dl - fl + 1):
    Q.append(int(D[i]/fac))
    M.append(fac * Q[i])
    if len(M)==1:
      if not no7(M[0]) or not isLen(M[0],6):
        return  
    if len(M)==2:
      if not no7(M[1]) or not isLen(M[1],7):
        return  
    if len(M)==3:
      if not only7(M[2],5) or not isLen(M[2],6):
        return  
    if len(M)==4:
      if not only7(M[3],3) or not isLen(M[3],7):
        return  
    if len(M)==5:
      if not no7(M[4]) or not isLen(M[4],6):
        return  
    R.append(D[i] - M[i])
    if i<dl-fl:
      D.append(R[i]*10 + int(str(div)[len(str(fac)) + i])) 
    if len(D)==2:
      if not only7(D[1],2) or not isLen(D[1],7):
        return
    if len(D)==3:
      if not only7(D[2],5) or not isLen(D[2],6):
        return
    if len(D)==4:
      if not no7(D[3]) or not isLen(D[3],7):
        return
    if len(D)==5:
      if not no7(D[4]) or not isLen(D[4],6):
        return
  #check constraints
  print "SOLUTION", div, fac	

thou = 0
for fac in range(100070,999979):
  if only7(fac,2):
    if thou!=int(fac/1000):
      thou = int(fac/1000)
      print thou
    temp = 9999999999/fac
    for mul in range(10700,temp):
      if not only7(mul,3):
        continue
      div = fac * mul
      if only7(div,8):
        D,Q,M,R = ([] for i in range(4))
        longdiv(div,fac,D,Q,M,R)

