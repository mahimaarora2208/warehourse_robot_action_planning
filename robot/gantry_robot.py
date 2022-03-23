from gripper.gripper import Gripper
from robot.base_robot import BaseRobot
from utils.utils import current_state


class GantryRobot(BaseRobot):
    def __init__(self):
        super().__init__(name="Gantry", payload=15,
                         weight=500, bins=['bin3', 'bin4'])
        self._small_rail_length = 12
        self._long_rail_length = 20
        self._small_rail_height = 5
        self._long_rail_height = 4.75

    # Getter Methods
    @property
    def get_small_rail_length(self):
        return self._small_rail_length

    @property
    def get_long_rail_length(self):
        return self._long_rail_length

    @property
    def get_small_rail_height(self):
        return self._small_rail_height

    @property
    def get_long_rail_height(self):
        return self._long_rail_height

    # Methods for gantry_robot class

    def _pickup_tray(self, tray, table):
        tray_location = current_state['trays'][tray]['location']
        if tray_location == 'table':
            Gripper.activate_gripper()
            Gripper.set_object_held('tray')
            print(f"pickup_tray({ self._name} , { tray} , { table} )")
            tray_location = 'gripper'
            agv = 'agv3'
            ######## AGV used in scenario(user input) ######
            self._place_tray(tray, agv)
        else:
            return

    def _place_tray(self, tray, agv):
        gripper_holding = Gripper.get_object_held()
        if gripper_holding == 'tray':
            Gripper.deactivate_gripper()
            current_state['trays'][tray]['location'] = agv
            self._find_part()
        else:
            return

    def __str__(self):
        return {'Name': self._name, 'Gripper': Gripper.__str__}

    '''
    Executes _pickup_tray() if required tray is found
    '''

    def plan(self):
        tray = 'yellow_tray'  ############ get from dictionary

        if tray is not None:
            if tray == 'yellow_tray':
                tray_on_table = 'yellow_tray_table' ###########  re-check
            else:
                tray_on_table = 'gray_tray_table'
        self._pickup_tray(tray, tray_on_table)
