import math

def Moyenne(liste):
  moyenne = sum(liste) / len(liste)
  return moyenne

def variance(liste):
  moyenne = Moyenne(liste)
  Variance = sum((x-moyenne)**2 for x in liste) / len(liste)
  return Variance
  
def ecart_type(liste):
  ecart_type = math.sqrt(variance(liste))
  return ecart_type

def custum_total(liste):
  total = 0
  for i in liste:
    total += i
  return total







variance([1,2,3])
    
