from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.opengl as gl
import pyqtgraph as pg
import numpy as np
import sys
from pathlib import Path
from scipy.stats import kde




x1=[0.1]
y1=[0.1]
z1=[0.1]

x2=[0.2]
y2=[0.2]
z2=[0.2]


x3=[0.3]
y3=[0.3]
z3=[0.3]

delta_time=0.005

sin=0
cos=0
o=10
b=8/3
p=28

def update_lorentz(x,y,z):




    vx=o*((y[len(y)-1])-(x[len(x)-1]))
    vy=(p*(x[len(x)-1]))-(y[len(y)-1])-((x[len(x)-1])*(z[len(z)-1]))
    vz=(-b*(z[len(z)-1]))+((x[len(x)-1])*(y[len(y)-1]))

    ax=x[len(x)-1]+(delta_time*vx)
    ay=y[len(y)-1]+(delta_time*vy)
    az=z[len(z)-1]+(delta_time*vz)

    x.append(ax)
    y.append(ay)
    z.append(az)
    return x,y,z



app = QtGui.QApplication([])
w = gl.GLViewWidget()
w.setGeometry(0, 0, 1920, 1400)

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

#w.addItem(x)
#w.addItem(y)
#w.addItem(z)

y.rotate(90,1,0,0)
y.translate(0,50,25)

z.rotate(90,0,1,0)
z.translate(50,0,25)


pos1 = (x1[0:len(x1)],y1[0:len(y1)],z1[0:len(z1)])
pos11= np.vstack(pos1).T
sp1=gl.GLLinePlotItem(pos=pos11 , width=1,color=(1.0, 0.0, 0.0, 1.0))

pos2 = (x2[0:len(x2)],y2[0:len(y2)],z2[0:len(z2)])
pos12= np.vstack(pos2).T
sp2=gl.GLLinePlotItem(pos=pos12 , width=1,color=(0.0, 1.0, 0.0, 1.0))


pos3 = (x3[0:len(x3)],y3[0:len(y3)],z3[0:len(z3)])
pos13= np.vstack(pos3).T
sp3=gl.GLLinePlotItem(pos=pos13 , width=1,color=(0.0, 0.0, 1.0, 1.0))


#sp1.setGLOptions('opaque')
#sp2.setGLOptions('opaque')
#sp3.setGLOptions('opaque')
w.addItem(sp1)
w.addItem(sp2)
w.addItem(sp3)


def update():
    global x1,x2,x3,y1,y2,y3,z1,z2,z3,sin,cos
    sin=0.05
    cos=0
    update_lorentz(x1,y1,z1)
    update_lorentz(x2,y2,z2)
    update_lorentz(x3,y3,z3)


    pos1 = (x1[0:len(x1)],y1[0:len(y1)],z1[0:len(z1)])
    pos11= np.vstack(pos1).T
    sp1.setData(pos=pos11)

    pos2 = (x2[0:len(x2)],y2[0:len(y2)],z2[0:len(z2)])
    pos12= np.vstack(pos2).T
    sp2.setData(pos=pos12)

    pos3 = (x3[0:len(x3)],y3[0:len(y3)],z3[0:len(z3)])
    pos13= np.vstack(pos3).T
    sp3.setData(pos=pos13)
    w.orbit(sin,cos)
    

    
t = QtCore.QTimer()
t.timeout.connect(update)
t.start(0)




## Start Qt event loop unless running in interactive mode.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()

