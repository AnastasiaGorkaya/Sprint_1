new_tasks = ['task_001', 'task_011', 'task_007', 'task_015', 'task_005']
completed_tasks = ['task_002', 'task_012', 'task_006']
completed_tasks.append(new_tasks.pop(new_tasks.index('task_005')))
new_tasks.remove('task_007')
new_tasks.insert(0, new_tasks.pop(-1))
print(f'У задачи {new_tasks[0]} высокий приоритет, необходимо ее взять в работу.')