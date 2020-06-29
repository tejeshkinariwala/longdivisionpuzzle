def isLen(num,l): # this functions checks if the length of the num is same as l. Returns true and false accordingly
  return (len(str(num)) == l)

def only7(num,place): # this function checks if there is 7 in the num at units place 'place'. slightly a misnomer because previously was fitting for only 7 but now it is not worrying about other places.
  for nu, i in enumerate(str(num)):
    if (len(str(num))-nu)==place and i!="7":
      return False
  return True

def longdiv(div, fac, D, Q, M, R): 
  # this function performs the long division and at each step looks of the number meets the criteria of length and 7s presence in the right place
  # needs a fac and a dividend as input
  dl = len(str(div))
  fl = len(str(fac))
  #D stores the list of dividend at each step
  #Q stores the list of quotient digits
  #M stores the factor * quotient
  #R stores remainders
  D.append(int(str(div)[:len(str(fac))]))
  if D[0]<fac:
    return
  for i in range(dl - fl + 1):
    Q.append(int(D[i]/fac))
    M.append(fac * Q[i])
    if len(M)==1:
      if not isLen(M[0],6):
        return
    if len(M)==2:
      if not isLen(M[1],7):
        return
    if len(M)==3:
      if not only7(M[2],5) or not isLen(M[2],6):
        return
    if len(M)==4:
      if not only7(M[3],3) or not isLen(M[3],7):
        return
    if len(M)==5:
      if not isLen(M[4],6):
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
      if not isLen(D[3],7):
        return
    if len(D)==5:
      if not isLen(D[4],6):
        return
  print "SOLUTION", div, fac, D,Q,M,R

#### this is like the main function where the script actually startes running.
# this is basically a loop over all possible dividends and factors which clear the basic criteria of length, 7 in the right place and that they are 0 remainder pair
# this calls the longdiv function above which checks if the given pair also clears the deeper constraints
for fac in range(100070,999979):
  if only7(fac,2):
    temp_min = 1000000000/fac
    temp_max = 9999999999/fac
    for mul in range(temp_min,temp_max):
      if not only7(mul,3):
        continue
      div = fac * mul
      if only7(div,8):
        D,Q,M,R = ([] for i in range(4))
        longdiv(div,fac,D,Q,M,R)

~                              
