
import time_call_one
import time




@time_call_one.stat_called_time
def foo():
 print("I'm foo")

if __name__=='__main__':
 for i in range(10):
  time.sleep(2)
  foo()
