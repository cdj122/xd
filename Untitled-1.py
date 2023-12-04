class mydate:
    def __init__(self,y,m,d,h,s):
        mydate.__init__(self,y,m,d,h,s)
        if h<0 or h>23:
            raise ValueError('hour must be in 0-23')
        if m<0 or m>59:
            raise ValueError('minute must be in 0-59')
        if s<0 or s>59:
            raise ValueError('second must be in 0-59')
        self.hour=h
        self.minute=m
        self.second=s
    def showdate(self):
        print(self.year,self.month,self.day,self.hour,self.minute,self.second)
t=mydate(2020,1,1,1,1)
t.showdate()