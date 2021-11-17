ticket = 7.45
# in euro
persoon = 4
# er zijn 4 personen
GameseatPrijs = 0.37/5 
# Gameseat prijs is 37 cent per 5 minuten
GameseatTijd = 45 
# in minuten
prijs = (ticket*persoon)+(GameseatPrijs*GameseatTijd*persoon)
print(prijs)
tekst ='Dit geweldige dagje-uit met '+ str(persoon)+' mensen in de Speelhal met '+str(GameseatTijd)+' minuten VR kost je maar '+ str(prijs)+' euro.'
print(tekst)