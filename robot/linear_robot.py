from gripper.gripper import Gripper
from robot.base_robot import BaseRobot
from utils.utils import current_state

class LinearRobot(BaseRobot):
    def __init__(self):
        super().__init__(name="UR10", payload=10,
                         weight=200, bins=['bin1', 'bin2'])
        self._linear_rail_length = 10

    # Getter Methods

    @property
    def get_linear_rail_length(self):
        return self._linear_rail_length

    # Methods for linear_robot class

    def __str__(self):
        return {'Name': self._name, 'Gripper': Gripper.__str__}

    def plan(self):
        self._find_part()
