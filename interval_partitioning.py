import heapq
from datetime import datetime

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0
  
    def push(self, item, priority):
        heapq.heappush(self._queue, (priority, self._index, item))
        #print(self._index, self._queue)
        self._index += 1
  
    def pop(self):
        if self._index == 0:
            return None
        return heapq.heappop(self._queue)[-1]


class Classroom:
    def __init__(self, number, finish_time):
        self.class_num = number
        self.finish_time = finish_time

    def __repr__(self):
        return f'Classroom({self.class_num})'

# Tarefas já ordenadas pelo horário de início de forma crescente
tasks = [
    (1, 930, 1100),
    (2, 930, 1300),
    (3, 930, 1100),
    (5, 1100, 1400),
    (4, 1130, 1300),
    (6, 1330, 1500),
    (7, 1330, 1500),
    (8, 1430, 1700),
    (9, 1530, 1700),
    (10, 1530, 1700)
]

nine_30 = datetime(year=2021, day=4, month=9, hour=9, minute=30)

eleven_00 = datetime(year=2021, day=4, month=9, hour=11, minute=0)
eleven_30 = datetime(year=2021, day=4, month=9, hour=11, minute=30)

thirteen_00 = datetime(year=2021, day=4, month=9, hour=13, minute=0)
thirteen_30 = datetime(year=2021, day=4, month=9, hour=13, minute=30)

fourteen_00 = datetime(year=2021, day=4, month=9, hour=14, minute=0)
fourteen_30 = datetime(year=2021, day=4, month=9, hour=14, minute=30)

fifteen_00 = datetime(year=2021, day=4, month=9, hour=15, minute=0)
fifteen_30 = datetime(year=2021, day=4, month=9, hour=15, minute=30)

seventeen_00 = datetime(year=2021, day=4, month=9, hour=17, minute=0)

tasks = [
    ('Testando string 1', nine_30, eleven_00),
    ('Testando string 2', nine_30, thirteen_00),
    ('Testando string 3', nine_30, eleven_00),
    ('Testando string 5', eleven_00, fourteen_00),
    ('Testando string 4', eleven_30, thirteen_00),
    ('Testando string 6', thirteen_30, fifteen_00),
    ('Testando string 7', thirteen_30, fifteen_00),
    ('Testando string 8', fourteen_30, seventeen_00),
    ('Testando string 9', fifteen_30, seventeen_00),
    ('Testando string 10', fifteen_30, seventeen_00)
]

def find_num_classrooms():
    num_classrooms = 0
    priority_queue = PriorityQueue()
 
    # Itera sobre todas as tarefas que serão feitas
    for task in tasks:
        task_id, start_time, finish_time = task

        # Remove a sala que termina a aula primeiro (menor finish_time)
        classroom = priority_queue.pop()

        # Se a sala não tiver nenhuma aula alocada, aloca uma nova sala
        if not classroom:
            num_classrooms+= 1
            print(f'ABRINDO SALA PRIMEIRA VEZ {num_classrooms}: {start_time} - {finish_time}')
            priority_queue.push(
                Classroom(
                    num_classrooms,
                    finish_time
                ),
                finish_time
            )
        else:
            #print('TEM AULA NA SALA')
            # Verifica se o horário do fim da aula alocada atualmente na sala
            # é menor que o horário inicial da aula que será alocada
            if classroom.finish_time  <= start_time:
                print(f'UTILIZANDO SALA JÁ EXISTENTE {classroom.class_num}: {start_time} - {finish_time}')
                classroom.finish_time = finish_time

                priority_queue.push(
                    classroom,
                    finish_time
                )
            else:
                num_classrooms += 1

                # Envia a sala já aberta para a lista de prioridade com novo finish_time 
                # para ser comparada novamente
                priority_queue.push(
                    classroom,
                    finish_time
                )

                print(f'ABRINDO NOVA SALA {num_classrooms}: {start_time} - {finish_time}')
                # Adiciona a sala que estava fechada na lista de prioridade
                priority_queue.push(
                    Classroom(num_classrooms, finish_time),
                    finish_time
                )
        print('#'*30)
    return num_classrooms
     
if __name__ == '__main__':
    classrooms = find_num_classrooms()
    print(f"Number of classrooms required: {classrooms}")