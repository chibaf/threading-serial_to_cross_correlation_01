import threading
import queue,time
import serial,sys
import cross_corr_via_serial_sub

i=1;k=1
q =queue.Queue()  # queue which stores a result of a thread
th = threading.Thread(target=cross_corr_via_serial_sub.serial_cross_corr, args=(sys.argv[1],sys.argv[2],q),daemon=True)
th.start()
print("start thread: "+str(i))
#th.join()
while True:
  if threading.active_count()==1:
    ix = q.get()
    print(ix)
    i=i+1
    if i>5:
      print("k="+str(k))
      break;
    th = threading.Thread(target=cross_corr_via_serial_sub.serial_cross_corr, args=(sys.argv[1],sys.argv[2],q),daemon=True)
    th.start()
    print("start thread: "+str(i))
  k=k+1
exit()
