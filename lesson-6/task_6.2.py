class Road:
    _length = None
    _width = None

    def m_asf(self, mas, deep):
        m = self._length * self._width * mas * deep
        print("Масса асфальта", m/1000, "т")


r = Road()
r._length = 20
r._width = 5000
r.m_asf(25, 5)
