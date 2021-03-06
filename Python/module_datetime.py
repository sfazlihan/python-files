from datetime import datetime
from datetime import timedelta
#import datetime

simdi=datetime.now()
simdi=datetime.today()      # şimdiki zamanları verir.

result=datetime.now()
result=datetime.year
result=datetime.month
result=datetime.day         # şimdiki günü verir
result=datetime.hour
result=datetime.minute
result=datetime.second

result=datetime.ctime(simdi)    # bir datetime objesini ayrıntılı şekilde verir
result=datetime.strftime(simdi,"%Y")    # şimdi deki yılı gösterir    
result=datetime.strftime(simdi,"%X")    # şimdi deki saati gösterir 
result=datetime.strftime(simdi,"%d")    # şimdi deki günü gösterir 
result=datetime.strftime(simdi,"%A")    # şimdi deki günün adını gösterir 
result=datetime.strftime(simdi,"%B")    # şimdi deki ayı gösterir 
result=datetime.strftime(simdi,"%Y %A %B")   # şimdi deki Yılı,GününAdını,Ayı  gösterir 

t="15 April 2020 hour 10:20:59"
result=datetime.strptime(t,'%d %B %Y hour %H:%M:%S')    #bir stringden tarihi çıkarır.
result=result.year      #resulttaki yılı gösterir



birthday=datetime(2003,3,1)


result=datetime.timestamp(birthday)   #saniyeye çevirir
result=datetime.fromtimestamp(result)   #datetime e çevirir
result=datetime.fromtimestamp(0)    #bilgisayarların miladı olan "1970-01-01 03:00:00" tarihini verir.


result=simdi-birthday  # kaç gün yaşadığını gösterir.  => timedelta

result=result.days
# result=result.seconds
# result=result.microseconds


print(simdi)
result=simdi + timedelta(days=10)       #şimdiki zamana 10gün ekler.
result=simdi + timedelta(days=730, minutes=10)      #şimdiki zamana 2yıl, 10dakika ekler.
result=simdi - timedelta(days=10)       #şimdiki zamandan 10gün çıkarır.


print(result)