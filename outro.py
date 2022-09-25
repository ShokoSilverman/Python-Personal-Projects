import os
import time
import winsound

winsound.PlaySound('Python\Python Files\outro.wav', winsound.SND_ASYNC | winsound.SND_ALIAS)
print('Initiating shutdown sequence.')
for num in reversed(range(1,11)):
    print('Shutting down in', num)
    time.sleep(0.9)
os.system('shutdown /s /t 1')