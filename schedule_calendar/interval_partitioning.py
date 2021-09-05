import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0
  
    def push(self, item, priority):
        heapq.heappush(self._queue, (priority, self._index, item))
        self._index += 1
  
    def pop(self):
        if self._index == 0:
            return None
        return heapq.heappop(self._queue)[-1]


class Employee:
    def __init__(self, number, finish_time):
        self.employee_num = number
        self.finish_time = finish_time

    def __repr__(self):
        return f'Employee({self.employee_num})'


def find_num_employees(tasks):
    num_employees = 0
    priority_queue = PriorityQueue()
 
    # Itera sobre todas as tarefas que serão feitas
    for task in tasks:
        task_id, start_time, finish_time = task

        # Remove o funcionário que finaliza a tarefa primeiro (menor finish_time)
        employee = priority_queue.pop()

        # Se o funcionário não tiver nenhuma tarefa alocada, aloca uma tarefa para o funcionário
        if not employee:
            num_employees+= 1
            priority_queue.push(
                Employee(
                    num_employees,
                    finish_time
                ),
                finish_time
            )
        else:
            # Verifica se o horário do fim da tarefa alocada atualmente para um funcionário
            # é menor que o horário inicial da tarefa que será alocada
            if employee.finish_time  <= start_time:
                employee.finish_time = finish_time

                priority_queue.push(
                    employee,
                    finish_time
                )
            else:
                num_employees += 1

                # Envia o funcionário já alocado para a lista de prioridade com novo finish_time 
                # para ser comparado novamente
                priority_queue.push(
                    employee,
                    finish_time
                )
                # Adiciona o funcionário que não tinha tarefa alocada para a lista de prioridade
                priority_queue.push(
                    Employee(num_employees, finish_time),
                    finish_time
                )
    return num_employees
