import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0
  
    def push(self, item, priority):
        heapq.heappush(self._queue, (priority, self._index, item))
        self._index += 1
  
    def pop(self):
        if(self._index == 0):
                return None
        return heapq.heappop(self._queue)[-1]


class Classroom:
    def __init__(self, number, finish_time):
        self.class_num = number
        self.finish_time = finish_time


jobs = [
    (1, 930, 1100),
    (2, 930, 1300),
    (3, 930, 1100),
    (5, 1100, 1400),
    (4, 1130, 1300),
    (6, 1330, 1500),
    (7, 1330, 1500),
    (8,1430,1700),
    (9, 1530, 1700),
    (10, 1530, 1700)
]
 
def find_num_classrooms():
    num_classrooms = 0
    priority_queue = PriorityQueue()
 
    for job in jobs:
        # we have job here, now pop the classroom with least finishing time
        classroom = priority_queue.pop()
        if(classroom == None) :
            #allocate a new class
            num_classrooms+= 1
            priority_queue.push(Classroom(num_classrooms,job[2]),job[2])
        else:
            #check if finish time of current classroom is
            #less than start time of this lecture
            if(classroom.finish_time  <= job[1]):
                classroom.finish_time = job[2]
                priority_queue.push(classroom,job[2])
            else:
                num_classrooms+= 1
                #Since last classroom needs to be compared again, push it back
                priority_queue.push(classroom,job[2])
                #Push the new classroom in list
                priority_queue.push(Classroom(num_classrooms,job[2]),job[2])
 
    return  num_classrooms
     
if __name__ == '__main__':
    classrooms = find_num_classrooms()
    print(f"Number of classrooms required: {classrooms}")