class CountString:

    def update(self, subject):

        print('CountString: Subject {} has {} words'.format(subject.name, len(subject.data.split())))


class CountEvenWords:

    def update(self, subject):

        count = 0
        for word in subject.data.split():
            if len(word) % 2 == 0:
                count += 1
        print('CountEvenWords: Subject {} has {} even words'.format(subject.name, count))


class CountUpperWords:

    def update(self, subject):
        count = 0
        for word in subject.data.split():
            if word[0].isupper():
                count += 1
        print('CountUpperWords: Subject {} has {} upper words'.format(subject.name, count))


class Subject:

    def __init__(self):

        self._observers = []

    def notify(self, modifier=None):

        for observer in self._observers:
            if modifier != observer:
                observer.update(self)

    def attach(self, observer):

        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):

        try:
            self._observers.remove(observer)
        except ValueError:
            pass


class Data(Subject):
   
    def __init__(self, name=''):
        Subject.__init__(self)
        self.name = name
        self._data = 0

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
        self.notify()


if __name__ == "__main__":
    obj1 = Data('Data 1')
    obj2 = Data('Data 2')
    obj1.attach(CountString())
    obj1.attach(CountEvenWords())
    obj1.attach(CountUpperWords())
    obj2.attach(CountString())
    obj2.attach(CountEvenWords())
    obj2.attach(CountUpperWords())
    obj1.data = 'Uma letra maiúscula'
    obj2.data = 'Duas Maiúsculas'
    print(obj1.data)
    print(obj2.data)
