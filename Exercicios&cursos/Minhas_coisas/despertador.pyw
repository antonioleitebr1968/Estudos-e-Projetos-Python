from datetime import datetime
import os
while True:
    a = datetime.now()
    if a.hour == 16:
         #os.popen2('/usr/bin/totem --play /usr/share/sounds/ubuntu/stereo/*')
         os.startfile('C:\\Users\\Public\\Videos\\Sample Videos\\Dino_Dancarino.mp4')
         print(f'Ta na horaaaaaaaaaaaa {a.hour}:{a.minute}hrs')
         break # importante para nao abrir varias instancias do totem
