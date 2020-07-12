
import time

def stat_called_time(func):
 cache={}
 limit_times=[1]

 def _called_time(*args,**kwargs):
  key=func.__name__
  if key in cache.keys():
   [call_times,updatetime]=cache[key]
   sy_time=time.time()-updatetime
   if time.time()-updatetime <5: # 20秒之内
    cache[key][0]+=1
   else:
    cache[key]=[1,time.time()]
  else:
   call_times=1
   cache[key]=[call_times,time.time()]
  print('调用次数: %s' % cache[key][0])
  print('限制次数: %s' % limit_times[0])
  if cache[key][0] <= limit_times[0]:
   res=func(*args,**kwargs)
   cache[key][1] = time.time()
   return res
  else:
   print("超过调用次数了")
   return "不要频繁操作 %d秒后可以操作"%(5-int(sy_time))+"<ul><li><a href='/index'>返回</a></li></ul>"



 return _called_time




'''
@stat_called_time
def foo():
 print("I'm foo")
 
if __name__=='__main__':
 for i in range(10):
  time.sleep(2)
  foo()
'''

