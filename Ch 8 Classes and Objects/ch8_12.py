# defining an interface or abssstract base class

from abc import ABCMeta, abstractmethod

class IStream(metaclass=ABCMeta):
    @abstractmethod
    def read(self, maxbytes = -1):
        pass
    @abstractmethod
    def write(self, date):
        pass

class SocketStream(IStream):
    def read(self, maxbytes =-1):
        pass
    def write(self, data):
        pass

    #skipping for now