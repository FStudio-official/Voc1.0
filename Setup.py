import os
import time
io=input("Bitte geben Sie den Pfad des Ordners an, indem diese Datei sich befindet:")
print(io)
os.system('cls')
io=io.split('\\')
pathnow=str()
for i in io:
    pathnow=pathnow+i+"\\"
pathnow=pathnow.removesuffix("\\")
print("Bitte haben Sie einen Moment Geduld...")
os.system('cd %USERPROFILE%')
if not os.path.exists("%Userprofile%\\Voc1.0") and not os.path.exists("%Userprofile%\\Voc1.0\\Sprachen"):
    os.system('cd %USerprofile%')
    os.system("mkdir %Userprofile%\\Voc1.0")
    os.system('cd %Userprofile%\\Voc1.0')
    os.system('mkdir %Userprofile%\\Voc1.0\\Sprachen')
    os.system('cd %Userprofile%\\Voc1.0\\Sprachen')
    langs=os.listdir(pathnow+"\\sSprachen")
    os.system('@cd '+pathnow+"\\sSprachen")
    if len(langs)!=0:
        for lang in langs:
            os.system(f'@copy sSprachen\\{lang} %Userprofile%\\Voc1.0\\Sprachen')

if not os.path.exists('%USerprofile%\\Voc1.0'):
    os.system('cd '+pathnow)
    os.system('@copy svoc1.0.py %Userprofile%\\Voc1.0')
    with open("Voc1.0.py","w") as file:
        file.write("import os\nos.system('cd %Userprofile%\\Voc1.0')\nos.system('python svoc1.0.py')")
    os.system('cls')
    print("Bitte warten...")
    time.sleep(6)
print("Das Setup wurde erfolgreich durchgeführt! Sie können in dem Ordner jetzt auf die Datei 'Voc1.0' klicken und der Vocabeltrainer wird starten!")
print("Drücken Sie eine beliebige Taste um das Setup zu schließen...")
os.system('@echo off')
os.system('@pause')