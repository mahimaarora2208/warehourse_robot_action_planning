from abc import ABC

from sympy import rem
from gripper.gripper import Gripper
from utils import current_state


class BaseRobot(ABC):
    def __init__(self, name, payload, weight, bins=[], category="industrial"):
        self._name = name
        self._category = category
        self._payload = payload
        self._weight = weight
        self._gripper: Gripper = None
        self._accessible_bins = bins

    # Getter Methods
    @property
    def get_name(self):
        return self._name

    @property
    def get_category(self):
        return self._category

    @property
    def get_payload(self):
        return self._payload

    @property
    def get_weight(self):
        return self._weight

    @property
    def get_bins(self):
        return self._accessible_bins

    @property
    def get_gripper(self):
        return self._gripper

    # Setter Methods
    @get_gripper.setter
    def set_gripper(self, x):
        self._gripper = x

    # Methods for base_robot class
    def _remove_part_from_bin(self, bin):
        current_quantity = current_state['bins'][bin]['part_quantity']
        if current_quantity > 0:
            current_quantity -= 1

    def _find_part(self): #### Needs time
        found_part = None
        found_bin = None
        tray = None ########current tray to be used
        expected_parts = current_state['trays'][tray]['expected_parts']
        current_parts = current_state['trays'][tray]['current_parts']
        remaining_parts = expected_parts
        remaining_parts.remove(current_parts) ############ remove current parts from remaining parts
        for part in remaining_parts:
            if found_part == None:
                bin_for_part = part
                self._pickup_part(bin, part)


    def _pickup_part(self, bin, part):
        pass
    
    def _place_part(self, tray, part, agv):
        pass
