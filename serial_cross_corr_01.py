import threading
import queue,time
import numpy as np
import serial, sys
#import matplotlib.pyplot as plt

def find_index(c):  # find index of maximum value
  mc=np.amax(c)
  for i in range(len(c)):
    if c[i]==mc:
      im=i
      break
  return im

def serial_cross_corr(port,speed,q):
  ser=serial.Serial(port,speed)  #open serial port
  time.sleep(2)
  i=0
  d1=np.empty(0)
  d2=np.empty(0)
  while True:
    line = ser.readline()
    line2=line.strip().decode('utf-8',errors='replace')
    data = [str(val) for val in line2.split(",")]
#    print(line2)
    if i<100 and len(data)==11:
      d1=np.append(d1,np.float(data[1]))
      d2=np.append(d2,np.float(data[2]))
      i=i+1
    else:
      if len(d1)!=0:
        c=1.0/(np.linalg.norm(d1)*np.linalg.norm(d2)) 
#        print(len(d1))
        f1=np.fft.fft(d1)
        f2=np.conjugate(np.fft.fft(d2))
        ff=f1*f2
        corrf=np.real(np.fft.ifft(ff))*c
        ix=find_index(corrf)
        break
  ser.close()
  q.put(ix)

i=1
q =queue.Queue()  # queue which stores a result of a thread
th = threading.Thread(target=serial_cross_corr, args=(sys.argv[1],sys.argv[2],q),daemon=True)
th.start()
#th.join()
while True:
  if threading.active_count()==1:
    ix = q.get()
    print(ix)
#    print(str(i)+': thread ended')
    i=i+1
    if i>5:
      break;
    th = threading.Thread(target=serial_cross_corr, args=(sys.argv[1],sys.argv[2],q),daemon=True)
    th.start()
#  print(str(i)+' dose not end')
#  time.sleep(2)  #do other tasks

exit()
