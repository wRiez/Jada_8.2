def check_query(query):
    elements = query.split(', ')
    # Напишите код функции
    if elements[-1] == 'друзей?':
        return ' '.join(elements[-1])
    elif elements[-1] == 'был?':
        return ' '.join(elements[-1])
    elif elements[-1] == 'скорей!':
        return ' '.join(elements[-1])
    else:
        return ' '.join(elements[-1])


# Дальше следует код, вызывающий вашу функцию; не изменяйте его:
queries = [
    'Анфиса, сколько у меня друзей?',
    'Андрей, ну где ты был?',
    'Андрей, ну обними меня скорей!',
    'Анфиса, кто все мои друзья?'
]

for q in queries:
    result = check_query(q)
    print(q, '—', result)