import time
import getUndone from algorithmEntry
import getMatrix from algorithmEntry
import GNN_prediction from GNN

UserID = "tric"#redefine
events = getUndone(UserID)

class obj:
    """unsorted list objects, obtain from back-end database"""
    def __init__(self,tID,eventID,begin,last):
        self.id = tID
        # self.event
        self.eventID = eventID
        self.begin = begin
        self.last = last

UnSortedList = []
# UnSortedList = append(obj(0,))
for i in range(1,len(events)):
    UnSortedList.append(obj(i,events[i-1].eventID,events[i-1].eventStarttime,eventPeriod))

for i in range()

class Sorting:
    """
    TimeVec: n*n vector for storing the distance from server
    TimeDiff: pre-regulated time between different actions
    sequence: the arranged time provided to the user
    UnsortedList: the waiting list to be sorted
    [
        id:
        begin:
        last:
        location:
    ]
    """
    def __init__(self,TimeVec,TimeDiff,UnSortedList,beginTime = 0,endTime = 86400):
        self.TimeVec = TimeVec #attain from database
        self.TimeDiff = TimeDiff #attain from database
        self.UnSortedList = UnSortedList
        self.sequence = []
        # self.currentTime = time.time()
        self.currentTime = 0
        self.beginTime = beginTime
        self.endTime=endTime

    def GetTravellingTime(self, begin_id,end_id):
        return TimeVec[begin_id][end_id]

    def GreedyRoute(self):
        ''' rrange the marked schedule'''
        cnt1 = 0
        for i in self.UnSortedList:
            if i.begin != -1:
                i.last += self.TimeDiff #the lasting Time has been prolonged for "Timediff" sec
                self.sequence.append(i)
                self.UnSortedList.remove(i) #remove the user-defined ones
                # print("self.sequence=",self.sequence[:])                
                cnt1+=1
        #consider the problem for "no sorted list"

        '''arrange the unmarked schedule'''
        # 1. search for min-time-range
        TimeInterval = [] #record the time intervals between two different positioned works
        # ScheduleInsertion = [] #record the inserted schedule between diff intervals
        newTime = [] #[time interval,beginid,[schedule in between],beginTime]
        newTime.append(self.sequence[0].begin-self.currentTime-self.TimeDiff)
        newTime.append(0);
        newTime.append([]); 
        newTime.append(self.sequence[0].begin)   
        TimeInterval.append(newTime)
        # ScheduleInsertion.append([])     
        # TimeInterval.append(sequence[0].begin-self.currentTime)
        for i in range(0,len(self.sequence)-1):
            print("i",i)
            # newSchedule = []
            # ScheduleInsertion.append(newSchedule)
            newTime = []
            newTime.append(self.sequence[i+1].begin-(self.sequence[i].begin+self.sequence[i].last))
            newTime.append(self.sequence[i].id)
            newTime.append([])
            newTime.append(self.sequence[i].begin)   
            TimeInterval.append(newTime)    
        TimeInterval.append([self.endTime-(self.sequence[len(self.sequence)-1].begin+self.sequence[len(self.sequence)-1].last),self.sequence[len(self.sequence)-1].id,[]])
        # newSchedule = []
        # ScheduleInsertion.append(newSchedule)
        # print("schedule insertion", ScheduleInsertion)
        TimeInterval.sort(cmp = None,key = lambda x:x[0],reverse=False)
        #2. insert objects according to a greedy schedule
        SortedSequence = self.UnSortedList
        begin_id = 0 # from current place
        for i in SortedSequence:
            i.last += self.GetTravellingTime(begin_id,i.id)
            print i.last
        SortedSequence = sorted(self.sequence,key = lambda x :x.last,reverse=False)#sorted schemes to be planned
        cnt = 0
        valid = True
        while len(SortedSequence):
            """
            for insertion into every single piece
            try
            """
            if cnt == len(TimeInterval)-1:
                if  TimeInterval[cnt][0]- cur.last < self.TimeDiff:
                    print("No appropriate solution.")
                    valid = False
                    break
                else:
                    cur.begin = self.endTime - (TimeInterval[cnt][0]-self.TimeDiff)
                    # cur.begin = self.sequence(TimeInterval[cnt][1])+TimeInterval[cnt][0]+self.TimeDiff
                    TimeInterval[cnt][2].append(cur)
                    TimeInterval[cnt][0] -= (cur.last + self.TimeDiff)
                    SortedSequence.remove(SortedSequence[0])
                    begin_id = cur.id
                    for i in SortedSequence:
                        i.last += self.GetTravellingTime(begin_id,i.id)
                    cnt = 0
                    # SortedSequence = self.UnSortedList
                    continue

            cur = SortedSequence[0]
            if TimeInterval[cnt][0] - cur.last < self.TimeDiff:
                cnt+=1
                continue
            cur.begin = TimeInterval[cnt+1][0] - (TimeInterval[cnt][0]-self.TimeDiff)
            TimeInterval[cnt][2].append(cur)
            # ScheduleInsertion[TimeInterval[cnt][1]+1].append(cur)
            TimeInterval[cnt][0] -= (cur.last + self.TimeDiff)
            """between schedule insertion, the scheule marked 0 means from current status to the 1st scheme, and so on and so on.."""
            SortedSequence.remove(SortedSequence[0])
            begin_id = cur.id
            for i in SortedSequence:
                i.last += self.GetTravellingTime(begin_id,i.id)
            cnt = 0
            # SortedSequence = self.UnSortedList
        if valid:
            TimeInterval.sort(cmp = None,key = lambda x:x[3],reverse=False)
            res=[]
            for i in TimeInterval:
                res.append([i[3],UnSortedList[i[1]].eventID])
                startTime = i[3] + Timediff
                for j in i[2]:
                    res.append([j.begin,j.eventID])
            return res


# TimeVec = [[0,3,2,6],[3,0,4,2],[2,4,0,5],[6,2,5,0]]
TimeDiff = 300
# A = obj(0,1,0.5)
# B = obj(1,-1,3)
# C = obj(2,1.5,3)
# D = obj(3,-1,2)

# UnSortedList = []
# UnSortedList.append(A)
# UnSortedList.append(B)
# UnSortedList.append(C)
# UnSortedList.append(D)

# res = Sorting(TimeVec,TimeDiff,UnSortedList)
# res.GreedyRoute()

TimeVec = getMatrix("tric","江苏省南京市新街口")
res = Sorting(TimeVec,TimeDiff,UnSortedList)
res.GreedyRoute()
        
        
            





        


            

            



        

            

            