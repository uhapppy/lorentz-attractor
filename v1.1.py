from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.opengl as gl
import pyqtgraph as pg
import numpy as np
import sys
from pathlib import Path
from scipy.stats import kde




x1=[]
y1=[]
z1=[]

listepos=[]
listeview=[]


delta_time=0.005


o=10
b=8/3
p=28




def ajouterLigne(x,y,z,colors):
    x1.append([x])
    y1.append([y])
    z1.append([z])
    pos1 = (x,y,z)
    pos11= np.vstack(pos1).T
    listeview.append(gl.GLLinePlotItem(pos=pos11 , width=1,color=colors))


ajouterLigne(0.01,0.01,0.01,(0.5,0.0,0.5,1.0))
ajouterLigne(0.1,0.1,0.1,(1.0,0.0,0.0,1.0))
ajouterLigne(0.2,0.2,0.2,(0.0,1.0,0.0,1.0))
ajouterLigne(0.3,0.3,0.3,(0.0,0.0,1.0,1.0))








    






def update_lorentz(x,y,z):
    global x1,y1,z1
    for i in range(0,len(x)):


        vx=o*((y[i][len(y[i])-1])-(x[i][len(x[i])-1]))
        vy=(p*(x[i][len(x[i])-1]))-(y[i][len(y[i])-1])-((x[i][len(x[i])-1])*(z[i][len(z[i])-1]))
        vz=(-b*(z[i][len(z[i])-1]))+((x[i][len(x[i])-1])*(y[i][len(y[i])-1]))

        ax=x[i][len(x[i])-1]+(delta_time*vx)
        ay=y[i][len(y[i])-1]+(delta_time*vy)
        az=z[i][len(z[i])-1]+(delta_time*vz)

        x[i].append(ax)
        y[i].append(ay)
        z[i].append(az)
    return x,y,z



app = QtGui.QApplication([])
w = gl.GLViewWidget()
w.setGeometry(0, 110, 1920, 1080)
w.show()
x = gl.GLGridItem()
y = gl.GLGridItem()
z = gl.GLGridItem()

x.setSize(x=100,y=100,z=0)
y.setSize(x=100,y=50,z=0)
z.setSize(x=50,y=100,z=0)

x.setSpacing(x=5,y=5,z=5)
y.setSpacing(x=5,y=5,z=5)
z.setSpacing(x=5,y=5,z=5)

w.addItem(x)
w.addItem(y)
w.addItem(z)

y.rotate(90,1,0,0)
y.translate(0,50,25)

z.rotate(90,0,1,0)
z.translate(50,0,25)


for i in range(0,len(listeview)):
    w.addItem(listeview[i])




#sp1.setGLOptions('opaque')
#sp2.setGLOptions('opaque')
#sp3.setGLOptions('opaque')



def update():
    global x1,y1,z1

    update_lorentz(x1,y1,z1)


    for i in range(0,len(x1)):
        pos1 = (x1[i][0:len(x1[i])],y1[i][0:len(y1[i])],z1[i][0:len(z1[i])])
        pos11= np.vstack(pos1).T
        listeview[i].setData(pos=pos11)


    

    
t = QtCore.QTimer()
t.timeout.connect(update)
t.start(0)




## Start Qt event loop unless running in interactive mode.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()

