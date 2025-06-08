import random
import os
import subprocess
global version
version="1.0"
path = subprocess.check_output('echo %USERPROFILE%', shell=True).decode().strip()
global langs
os.system('cd %Userprofile%\\Voc1.0')
langs=os.listdir(path+f"\\Voc{version}\\Sprachen")

def vokcheck(clang):
    with open(path+"\\Voc1.0\\Sprachen\\"+clang,"r") as voks:
        rawlines=set(voks.readlines())
        voks.close()
    os.system('cls')
    insg=len(rawlines)
    cp=len(rawlines)
    blist=[1,2]
    for _ in range(insg):
        
        test=len(rawlines)
        if test==0:
            break
        rb=random.choice(list(blist))
        if rb==2:
            cvok=random.choice(list(rawlines))
            rawlines.remove(cvok)
            cvoka=(cvok.split('|'))[1]
            cvokuh=(cvok.split('|'))[0]
        else:
            cvok=random.choice(list(rawlines))
            rawlines.remove(cvok)
            cvoka=(cvok.split('|'))[0]
            cvokuh=(cvok.split('|'))[1]
        io=cvoka
        print("Übersetze das:"+cvokuh)
        io=input("Antwort:")
        if "\n" in cvoka:
            cvoka=cvoka.removesuffix('\n')
        os.system('cls')
        if io==cvoka:
            print("Richtig!")
        else:
            print("Falsch! Die richtige Antwort wäre "+cvoka+" gewesen!")
            cp=cp-1
    print("Du hast "+str(cp)+"/"+str(insg)+" Punkte ereicht!")
    os.system('pause')
    langsel(clang)
def langsel(inlang):
    inlang=str(inlang)
    with open(path+f"\\Voc1.0\\Sprachen\\{inlang}", 'r') as infile:
        zeilen=infile.readlines()
        for zeile in zeilen:
            if zeile=='\n':  # Überprüfen, ob die Zeile nicht leer ist
                zeilen.remove(zeile)
                break 
            nz="\n"
            oldzeile=zeile
            while "\n" in zeile and "\n" in nz:
                nz=zeile.removesuffix('\n')
                nz=nz.removeprefix('\n')
            if "\n" in oldzeile:
                zeilen.remove(zeile)
                zeilen.append(nz)

    with open(path+f"\\Voc1.0\\Sprachen\\{inlang}", 'w') as clearfile:
        clearfile.write("")
    with open(path+f"\\Voc1.0\\Sprachen\\{inlang}", 'a') as outfile:
         for zeile in zeilen:
            if not (zeile=="\n" or "\n" in zeile):
                outfile.write(zeile+"\n")
            else:
                if "\n" in zeile and zeile!="\n":
                    nzeile=zeile.strip("\n")
                    outfile.write(nzeile+"\n")
                

    
        
    print("Hier ist die Sprachenoptionen:\n1 - Vokabel hinzufügen\n2 - Sprache löschen\n3 - Vokabel(-n) löschen\n4 - Sprache umbenennen\n5 - Vokabeln abprüfen\n6 - Vokabeln auflisten\n7 - Zurück zum Menü")
    io=input("Ihre Option:")
    if io=="1":
        io=input("Vokabel auf Deutsch:")
        gervok=io
        langwof=inlang.removesuffix('.txt')
        io=input(f"Vokabel auf {langwof}:")
        ovok=io
        with open(path+"\\Voc1.0\\Sprachen\\"+inlang,"a") as langfile:
            langfile.write(f"\n{gervok}|{ovok}")
            langfile.close()
        os.system('cls')
        langsel(inlang=inlang)
    if io=="2":
        io=input("Sicher?(j/n) ")
        if io=="j":
            os.remove(path+f"\\Voc{version}\\Sprachen\\{inlang}")
            langsel(inlang)
    if io=="3":
        io=input("Vokabel: ")
        with open(path+f"\\Voc{version}\\Sprachen\\{inlang}","r") as cdatei:
            zeils=cdatei.readlines()
            for ZNr,zeile in enumerate(zeils):
                if io in zeile:
                    nr=ZNr
                    print(str(nr))
                    break
            print(str(ZNr))
            cdatei.close() 
        with open(path+f"\\Voc{version}\\Sprachen\\{inlang}","r") as cdateit:
            alllines=cdateit.readlines()
            rline=alllines[nr]
            alllines.remove(rline)
            cdateit.close()
        with open(path+f"\\Voc{version}\\Sprachen\\{inlang}","w") as cdateif:
            cdateif.write("")
        with open(path+f"\\Voc{version}\\Sprachen\\{inlang}","a") as cdateid:
            for allline in alllines:
                cdateid.write(+allline)
        langsel(inlang)
    if io=="4":
        io=input("Neuer Name: ")
        io=io+".txt"
        os.system(f'ren %Userprofile%\\Voc{version}\\Sprachen\\{inlang} {io}')
        print(f"{inlang} wurde zu {io} umbenannt!")
        langsel(io)
    if io=="5":
        vokcheck(inlang)
    if io=="6":
        os.system('cls')
        print("Das sind die Vokabeln:")
        with open(path+f"\\Voc{version}\\Sprachen\\"+inlang,"r") as file:
            lines=file.readlines()
            for line in lines:
                tvoks=line.split('|')
                print(tvoks[0]+" - "+tvoks[1])
    if io=="7":
        os.system('cls')
        menu()
def menu():
    print("Hier sind die Optionen:\n1 - Sprache auswählen\n2 - Sprache hinzufügen\n3 - Sprachen auflisten\n4 - Beenden")
    io=input("Ihre Option:")
    if io=="1":
        io=input("Name:")
        pathlf=io+".txt"
        if os.path.exists(path+f"\\Voc{version}\\Sprachen\\{pathlf}"):
            os.system('cls')
            langsel((io+".txt"))
        else:
            print("Datei existiert nicht!")
            print()
            menu()
    if io=="2":
        os.system('cls')
        io=input("Name:")
        with open("Sprachen\\"+io+".txt","w") as ndatei:
            ndatei.close()
        menu()
    if io=="3":
        os.system('cls')
        print(f"Diese Sprachen wurden bereits hinzugefügt:")
        for lang in langs:
            print(lang.removesuffix('.txt'))
        print("\n")      
        menu()
    if io=="4":
        os.system('cls')
        exit()
    if not io=="1" or io=="2" or io=="3" or io=="4":
        print("Diese Option existiert nicht!")
        menu()
os.system('cls')
print("Willkommen im selbsteinrichtbaren Vokabeltrainer Voc1.0!")
menu()