from zipfile import ZipFile
import os

files = ["BananaPeel_Slippery.doc", "DiscoDancingUnicorn.mp3", "SneezingPanda.gif", "InvisibleCloak.exe",
         "PizzaDelivery_Drone.txt", "LaserCat_Visualization.pdf", "AlienCookbook.txt",
         "ZombieApocalypseSurvivalGuide.docx", "TalkingPotato.mp4", "DancingBroccoli.jpg"]


with ZipFile('XXX.zip', mode='a') as arch:
    for curr_file in files:
        if os.path.exists(curr_file):
            arch.write(curr_file)

