def dig(num, place):
  if len(str(num)) < place:
    return -1
  return(int(str(num)[len(str(num))-place]))

def longdiv(div, fac, D, Q, M, R):
  #check constraints on div and fac
  dl = len(str(div))
  fl = len(str(fac))
  D.append(int(str(div)[:len(str(fac))]))
  for i in range(dl - fl + 1):
    Q.append(int(D[i]/fac))
    M.append(fac * Q[i])
    if len(M)>2:
      if dig(M[2],5)!=7:
        return  
    if len(M)>3:
      if dig(M[3],3)!=7:
        return  
    R.append(D[i] - M[i])
    if i<dl-fl:
      D.append(R[i]*10 + int(str(div)[len(str(fac)) + i])) 
    if len(D)>1:
      if dig(D[1],2)!=7:
        return
    if len(D)>2:
      if dig(D[2],5)!=7:
        return
  #check constraints
  print "SOLUTION", div, fac	

 
thou = 0
for fac in range(100070,999979):
  if dig(fac,2)==7:
    if thou!=int(fac/1000):
      thou = int(fac/1000)
      print thou
    temp = 9999999999/fac
    for mul in range(10700,temp):
      if dig(mul,3)!=7:
        continue
      div = fac * mul
      if dig(div,8)==7:
        D,Q,M,R = ([] for i in range(4))
        longdiv(div,fac,D,Q,M,R)

