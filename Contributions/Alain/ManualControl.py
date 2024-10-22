import keyboard
import time
from DataStructModule import DataStruct
from PlotStructModule import PlotStruct

model = DataStruct(10)
plot = PlotStruct(model)
stepsize = 50

while True:
    
    if keyboard.is_pressed('esc'):
        break

    i = 0
    while i < stepsize:
        i += 1
        model.update()
        continue


    
    time.sleep(1)
    print("1")
    continue


plot = PlotStruct(model)
plot.createPlotRandTraject(2)


