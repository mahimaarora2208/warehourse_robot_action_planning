class Gripper:
    def __init__(self, name, weight=2, closing_speed=150):
        self._name = name
        self._weight = weight
        self._closing_speed = closing_speed
        self._enable = False
        self._object_held = None

    # Getter Methods
    @property
    def get_name(self):
        return self._name

    @property
    def get_weight(self):
        return self._weight

    @property
    def get_closing_speed(self):
        return self._closing_speed

    @property
    def get_object_held(self):
        return self._object_held

    # Setter Method
    @get_object_held.setter
    def set_object_held(self, x):
        self._object_held = x

    # Methods for gripper class # Should it return anything??
    def __str__(self):
        if self._enable == True:
            status = 'enabled'
        else:
            status = 'disabled'
        return {'Name': self._name, 'Enabled':  self._enable}

    def activate_gripper(self):
        self._enable = True
        print('activate gripper')

    def deactivate_gripper(self):
        self._enable = False
        print('deactivate gripper')
