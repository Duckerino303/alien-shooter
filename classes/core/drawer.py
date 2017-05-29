import threading
import classes.core.settings as settings
import random
import time

def explosion(x,y):
    threading.Thread(target=draw_explosion,args=(x,y)).start()

def draw_explosion(x,y):
    for i in range(settings.EXPLOSION_TIME * 100):
        settings.WINDOW.blit(settings.EXPLOSION_IMG,(x,y))
