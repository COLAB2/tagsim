import matplotlib.pyplot as plt
import numpy as np 
import os, time



def drawFig(Xdata,Ydata,heat,fig=1,colormap='inferno',label=''):
	plt.figure(fig)
	plt.clf()
	plt.axis('scaled')
	plt.grid(True)
	plt.contourf(Xdata, Ydata, heat, 20, cmap=colormap)# cmap='coolwarm'), cmap='RdGy')
	cbar = plt.colorbar()
	cbar.set_label(label)
	plt.xlim([0, xrange])
	plt.ylim([0, xrange])
	plt.xticks(np.arange(0,xrange,xrange/20))
	plt.yticks(np.arange(0,yrange,yrange/20))
	plt.draw()
	plt.pause(0.00001)
	
	
fname="gp.csv"
#moddate=os.stat(fname)[8]
#last=moddate
i=1
xrange=1
yrange=1
while True:
	#moddate=os.stat(fname)[8]
	#print(os.path.exists(str(i)+fname),str(i)+fname)
	if os.path.exists(str(i)+fname):
	#if  moddate != last:
		print(str(i)+fname)
		time.sleep(.1)
		#last=moddate
		try:
			gpdata=np.genfromtxt(str(i)+fname, delimiter=',')
			EIDvals = gpdata[:,0]
			mean = gpdata[:,1]
			var = gpdata[:,2]
			Xdata = gpdata[:,3]
			xrange=np.max(Xdata)
			Ydata = gpdata[:,4]
			yrange=np.max(Ydata)
			spacing=int(np.sqrt(EIDvals.shape[0]))
			EIDvals.shape=(spacing,spacing)
			mean.shape=(spacing,spacing)
			var.shape=(spacing,spacing)
			Xdata.shape=(spacing,spacing)
			Ydata.shape=(spacing,spacing)
		except:
			time.sleep(.2)
			continue
		#np.savetxt(str(i)+fname,gpdata)
		drawFig(Xdata,Ydata,mean,colormap='coolwarm',label='gp mean')
		drawFig(Xdata,Ydata,var,fig=2,colormap='RdGy',label='gp variance')
		drawFig(Xdata,Ydata,EIDvals,fig=3,label='EID')
		i+=1
	time.sleep(.1)
        




gpdata=np.genfromtxt('gp.csv', delimiter=',')
np.savetxt(fname+str(i),gpdata)
EIDvals = gpdata[:,0]
mean = gpdata[:,1]
var = gpdata[:,2]
Xdata = gpdata[:,3]
Ydata = gpdata[:,4]
spacing=int(np.sqrt(EIDvals.shape[0]))
EIDvals.shape=(spacing,spacing)
mean.shape=(spacing,spacing)
var.shape=(spacing,spacing)
Xdata.shape=(spacing,spacing)
Ydata.shape=(spacing,spacing)
drawFig(Xdata,Ydata,mean,label='gp mean')
drawFig(Xdata,Ydata,var,fig=2,colormap='inferno',label='gp variance')
drawFig(Xdata,Ydata,EIDvals,fig=3,colormap='inferno',label='EID')
input()