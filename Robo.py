import datetime

cunostinte_animale = {
    "URS": "Ursul hibenreaza iarna",
    "DELFIN": "Delfinii comunica intre ei prin sunete",
    "PINGUIN": "Pinguinii nu pot zbura",
    "FURNICA": "Furnicile pot ridica greutati mari"
}

def afiseaza_ora():
    """Afiseaza ora curenta a sistemului"""
    acum = datetime.datetime.now()
    ora_formatata = acum.strftime("%H:%M:%S")
    print(f"\n Ora exacta este: {ora_formatata}.")
    
def afiseaza_data():
    """Afiseaza data curenta a sistemului."""
    acum = datetime.datetime.now()
    data_formatata = acum.strftime("%d %B %Y")
    print(f"\n Astazi este: {data_formatata}.")

def invata_animale(nume_utilizator):
    """Permite utilizatorului sa invete despre animale."""
    print("\n--- Sectiunea Curiozitati despre animale ---")
    
    print("Alege din aceste animale: URS, DELFIN, PINGUIN, FURNICA.")
    cuvant_cheie = input(f"Despre ce animal ai vrea sa inveti, {nume_utilizator}?").strip().upper()
    
    if cuvant_cheie in cunostinte_animale:
        informatie = cunostinte_animale[cuvant_cheie]
        print(f"\n---Descopera!---")
        print(f"Stiai ca? {informatie}")
        print(f"Sper ca ai invatat ceva nou, {nume_utilizator}!")
    else:
        print(f"\n Imi pare rau. Nu am informatii despre '{cuvant_cheie}'. Incearca URS, DELFIN, PINGUIN sau FURNICA.")
        
def cuvinte_amestecate():
    """Contine logica jocului de ghicit 3 cuvinte amestecate, cu mesaj adaptat scorului."""
    
    cuvinte_corecte = ["COD", "PYTHON", "CALCULATOR"]
    cuvinte_amestecate = ["ODC", "THNOYP", "LATORCALCU"]
    
    scor = 0
    numar_cuvinte = len(cuvinte_corecte)
    
    print("\n ---Sectiune Joc (Litere Amestecate)---")
    
    for i in range(numar_cuvinte):
        print(f"\n{i+1}. Ghiceste cuvantul amestecat: {cuvinte_amestecate[i]}")
        
        raspuns = input("Raspunsul tau: ").strip().upper()
        
        if raspuns == cuvinte_corecte[i]:
            print(f"Corect! Bravo! Cuvantul era: {cuvinte_corecte[i]}")
            scor +=1
        else:
            print(f"Gresit! Cuvantul corect era: {cuvinte_corecte[i]}")
    
   
    
    
    if scor ==numar_cuvinte:
        print("Felicitari! Ai ghicit toate cuvintele.")
    elif scor >0:
        print("Bravo! Ai reusit sa ghicesti cateva cuvinte!")
    else:
        print("Nu ai ghicit niciun cuvant. Mai incearca! Sigur vei reusi data viitoare!")
        
    print(f" Ai ghicit {scor} din {numar_cuvinte} cuvinte")
    
        
print("Buna! Sunt Asistentul tau virtual, Robo!")
nume_utilizator = input("Pentru a incepe, te rog sa-mi spui cum te numesti: ").capitalize()
print(f"Bine ai venit, {nume_utilizator}! Ma bucur sa te ajut. Ce optiune ti-a starnit curiozitatea?")


while True:
    print("\n --------")
    print("Alege o optiune:")
    print("Scrie 'ORA' pentru a afla cat este ceasul.")
    print("Scrie 'DATA' pentru a afla data de azi.")
    print("Scrie 'JOC' pentru a te juca jocul litere amestecate.")
    print("Scrie 'INVATA' pentru a invata despre animale.")
    print("Scrie 'IESIRE' pentru a incheia conversatia cu Robo.")
    print("\n --------")
    
    alegere = input("Alegerea ta: ").strip().upper()
    
    if alegere == "ORA":
        afiseaza_ora()
        
    elif alegere == "DATA":
        afiseaza_data()
        
    elif alegere == "INVATA":
        invata_animale(nume_utilizator)
        
    elif alegere == "JOC":
        cuvinte_amestecate()
        
    elif alegere == "IESIRE":
        break
        
    else:
        print(f"\n Nu am inteles comanda '{alegere}'. Incearca din nou din lista de optiuni.")
        
print(f"\n Iti multumesc pentru ca ai petrecut timp cu mine, {nume_utilizator}! La revedere!")

        
        