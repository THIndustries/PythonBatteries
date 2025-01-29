def coroutine():
    print('Запускаем корутину')
    msg = yield  # Остановка для приёма данных
    print(f'От источника получено: {msg}')
    yield msg.upper()  # выдаем данные из генератора
    print('Завершаем корутину')


coro = coroutine()
next(coro)
res = coro.send(input('Введи >>>'))
print(res)
next(coro)