url = "https://docs.google.com/forms/d/e/1FAIpQLSc2L11swRRs95mcOqF3yHoanqNOnAsucEnv3nP43941czfKHg/formResponse"

print("Hallo, gerne nehme ich heute deine Bestellung fuer Flo's Fett Restaurant auf, hierführ benötige ich ein paar Infos von dir. Auf welchem Namen soll ich bestellen: ")
name = input("Name: ")
time = input("Super " + name + " für welche Uhrzeit soll ich bestellen? ")
order = input("Ok, was soll ich dir für " + time + " bestellen? ")

value_name = name
value_time = time
value_order = order

submission = {"entry.536960079": value_name,"entry.659618339": value_time,"entry.1665018644": value_order}

import requests
requests.post(url, submission)
