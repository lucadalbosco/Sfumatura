import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import time


rivestimento_lung = 100
sfumatura_lung = 30
angolo = 60
margine_lung = 100
risoluzione = 0.5 #mm per dato
lineare = False

tetta = 15

sig = tetta/risoluzione
x = np.linspace(-3*sig, 3*sig, 6*sig)
plasma_std = mlab.normpdf(x, 0, sig)



margine = margine_lung / risoluzione
rivestimento = rivestimento_lung / risoluzione
sfumatura = sfumatura_lung / risoluzione

lung_pezzo = int(margine + rivestimento + margine)

pezzo = np.zeros(lung_pezzo)

limite_sfumatura = margine + rivestimento - sfumatura
a=0
for i in range(0,len(pezzo)):
    
    if i < limite_sfumatura:
        #print 'Fuori'
        plasma = plasma_std
        
        
    if i >= limite_sfumatura:
        #print 'Dentro'
        if lineare==False or i >= limite_sfumatura+sfumatura:
            
            sig_est = sig / np.cos(angolo * np.pi / 180)
            
            x_dopo = np.linspace(-3*sig, 3*sig, 6*sig_est)
            
            plasma = mlab.normpdf(x, 0, sig_est)
        if lineare and i < limite_sfumatura+sfumatura:
            
            angolo_temp = np.linspace(1,angolo,sfumatura)
            
            sig_est = sig / np.cos(angolo_temp[a] * np.pi / 180)
            
            x_dopo = np.linspace(-3*sig, 3*sig, 6*sig_est)
            
            plasma = mlab.normpdf(x_dopo, 0, sig_est)
            
            #plt.plot(plasma) 
            a=a+1
        
    for p in range(0,len(plasma)):
        
        if i+p > margine-100 and i+p < len(pezzo):
 #       if i+p < len(pezzo):
            pezzo[i+p] =  pezzo[i+p] + plasma[p]
    #if i % 25 == 0:        
    
    
    
plt.plot(pezzo)    
plt.show()        
        

            
    