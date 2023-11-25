met=float(input("Digite um valor em metros: "))
print("{} metros\ncorresponde a {} Km\ncorresponde a {} Hm \ncorresponde a {} Dam" .format(met,(met/1000),(met/100),(met/10)))
print("corresponde a {} dm \ncorresponde a {} cm\ncorresponde a {} mm" .format((met*10),(met*100),(met*1000)))