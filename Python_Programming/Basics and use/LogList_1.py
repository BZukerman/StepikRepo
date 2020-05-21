import time         # Импорт модуля для работы Loggable
class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))
#
class LoggableList(list, Loggable):     # Реализация с помощью super
    def append(self, item, Array = []): # Определение метода
        self.item = item
#        print("1. self.item:", self.item)
#        list.append(self, item)
        super(LoggableList, self).append(item)  # множ. наследование
        Array.append(item)          # Добавление сообщения из Loggable
#        print("Array:", Array)
#        return Array           # Stepik не принял этот вариант
        return self.log(item)
#
Message = "Hello!"
Result = Loggable.log(time, Message)
#
z = LoggableList()
print("2. z:", z)
z.append(1)
print("3. z:", z)
z.append('value')
print("4. z:", z)