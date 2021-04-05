#!/usr/bin/python3
#def isPrime
def isPrime(n):
    if (n<=1):
        return False
    elif (n==2):
        return True;
    else:
        for x in range(2,int(n//2)+1):
            if(n % x==0):
                return False
        return True     
#def multiples
def multiples(x,n):
  listMultiples = [x,]
  i=2
  while(listMultiples[-1]< (n-x)+1):
    listMultiples.append(x*i)
    i=i+1
  return listMultiples

def playARound(t):
  listofPrimeInt=[]
  for x in t :
    if (isPrime(x)):
      listofPrimeInt.append(x)
  i=0
  max= t[-1]
  player=0
  while(len(t)>1):
    for pick in listofPrimeInt:
      listOfMultiples=multiples(pick,max) 
      for i in t:
        if i in  listOfMultiples:
          t.remove(i)
      player=player+1
    # if 1 maria wins else Ben wins
  return player%2
def isWinner(x,nums):
  listofnums = []
  for n in nums:
    listofnums.append([i for i in range(1,n+1)])
  listofnums
  result = [playARound(t) for t in listofnums]
  if (result.count(0)==result.count(1)):
    return None
  else:
    if (sum(result)>len(result)//2):
      return "Winner: Maria"
    else:
      return "Winner: Ben"

    
