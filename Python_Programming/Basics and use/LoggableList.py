# Реализуйте класс LoggableList, отнаследовав его от классов list и Loggable
# таким образом, чтобы при добавлении элемента в список посредством метода
# append в лог отправлялось сообщение, состоящее из только что добавленного
# элемента.
# В self находится массив для добавления элемента
#
import time
class Loggable:
    def log(self, msg):
        print("0:", str(time.ctime()) + ": " + str(msg))
#
class LoggableList(list, Loggable):
    def append(self, item):
        print("1:", self)
#        x = msg.append(self, item)
#        x = super(Loggable, self)
        super().append(item)
#        list.append(self, item)
#        super(LoggableList, self).append(item)
#        return self.log
#
Message = "Hello!"
Result = Loggable.log(time, Message)
#
z = LoggableList()
print(time.ctime())
print(type(time.ctime()))
z.append(1)
#z = LoggableList()
z.append('value')