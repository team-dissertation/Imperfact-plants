'''def rotX(self, angle):
    if 'turtle' in Conf.DEBUG:
        print
        "Called: rotX(", angle, ");"
    angle = self.randomize(angle)
    self.heading.set((
        self.heading.x,
        self.heading.y * math.cos(angle) - self.heading.z * math.sin(angle),
        self.heading.y * math.sin(angle) + self.heading.z * math.cos(angle)))
    print
    self.heading.toString()

def rot_x()


def irotX(self, angle):
    if 'turtle' in Conf.DEBUG:
        print
        "Called: rotX(", angle, ");"
    angle = self.randomize(angle)
    angle = -angle
    self.heading.set((
        self.heading.x,
        self.heading.y * math.cos(angle) - self.heading.z * math.sin(angle),
        self.heading.y * math.sin(angle) + self.heading.z * math.cos(angle)))
    print
    self.heading.toString()


""" Rotation around the y direction """


def rotY(self, angle):
    if 'turtle' in Conf.DEBUG:
        print
        "Called: rotY(", angle, ");"
    angle = self.randomize(angle)
    self.heading.set((
        self.heading.x * math.cos(angle) + self.heading.z * math.sin(angle),
        self.heading.y,
        - self.heading.x * math.sin(angle) + self.heading.z * math.cos(angle)))
    print
    self.heading.toString()


""" Reverse rotation around the y direction"""


def irotY(self, angle):
    if 'turtle' in Conf.DEBUG:
        print
        "Called: rotY(", angle, ");"
    angle = self.randomize(angle)
    angle = -angle
    self.heading.set((
        self.heading.x * math.cos(angle) + self.heading.z * math.sin(angle),
        self.heading.y,
        - self.heading.x * math.sin(angle) + self.heading.z * math.cos(angle)))
    print
    self.heading.toString()


""" Rotation around the z direction """


def rotZ(self, angle):
    if 'turtle' in Conf.DEBUG:
        print
        "Called: rotZ(", angle, ");"
    angle = self.randomize(angle)
    self.heading.set((
        self.heading.x * math.cos(angle) - self.heading.y * math.sin(angle),
        self.heading.x * math.sin(angle) + self.heading.y * math.cos(angle),
        self.heading.z))
    print
    self.heading.toString()


""" Reverse rotation around the z direction"""


def irotZ(self, angle):
    if 'turtle' in Conf.DEBUG:
        print
        "Called: rotZ(", angle, ");"
    angle = self.randomize(angle)
    angle = -angle
    self.heading.set((
        self.heading.x * math.cos(angle) - self.heading.y * math.sin(angle),
        self.heading.x * math.sin(angle) + self.heading.y * math.cos(angle),
        self.heading.z))
    print
    self.heading.toString()
'''