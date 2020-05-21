# Реализуйте класс LoggableList, отнаследовав его от классов list и Loggable
# таким образом, чтобы при добавлении элемента в список посредством метода
# append в лог отправлялось сообщение, состоящее из только что добавленного
# элемента.
# В self находится массив для добавления элемента
#
import time         # Импорт модуля для работы Loggable
class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))
#
class LoggableList(list, Loggable):     # Реализация через list.append
    def append(self, item, Array = []): # Определение метода
        self.item = item
#        print("1. self.item:", self.item)
        list.append(self, item)     # Модификация метода list
        Array.append(item)      # Добавление сообщения из Loggable
#        print("Array:", Array)
#        return Array        # Stepik не принял этот вариант
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