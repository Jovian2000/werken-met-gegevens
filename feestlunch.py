AantalCroissant = 17
AantalStokbrood = 2
AantalKortingsbon = 3
PrijsCroissant = 0.39
PrijsStokbrood = 2.78
PrijsKortingsbon = 0.50
prijs = (AantalCroissant*PrijsCroissant)+(AantalStokbrood*PrijsStokbrood)-(AantalKortingsbon*PrijsKortingsbon)
print (prijs)
tekst='De feestlunch kost je bij de bakker '+str(prijs)+' euro voor de '+str(AantalCroissant)+" croissantjes en de "+str(AantalStokbrood)+' stokbroden als de '+str(AantalKortingsbon)+' kortingsbonnen nog geldig zijn!'
print (tekst)