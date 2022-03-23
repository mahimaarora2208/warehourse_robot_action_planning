'''
Contains program implementation to prompt user for kitting information.

'''

from robot.gantry_robot import GantryRobot
from robot.linear_robot import LinearRobot
from gripper.gripper import Gripper
from utils.utils import current_state
import sys
sys.path.insert(1, 'D:\projects\ENPM809E\rwa2_arora_mahima')


def main():
    ##################### User Interface to Input kitting information #####################

    num = 100  # number to format display
    bin_list = [1, 2, 3, 4]
    agv_list = [1, 2, 3, 4]
    parts_in_bin_list = [0, 4, 9]
    num_red_parts = ''
    num_blue_parts = ''
    num_green_parts = ''
    red_bin = 0  # initalise the bin0 if no parts in bin
    green_bin = 0  # initalise the bin0 if no parts in bin
    blue_bin = 0  # initalise the bin0 if no parts in bin
    blue_inTray = ''
    red_inTray = ''
    green_inTray = ''
    tray_color = ''
    agv = ''
    red_bin = ''
    green_bin = ''
    blue_bin = ''
    assm = ''

    print('=' * num)  # Formatting the output display
    while num_red_parts not in parts_in_bin_list:
        num_red_parts = int(
            input('How many red_parts in the workcell [0, 4, 9]?'))
    if num_red_parts > 0:  # It will ask about the location ONLY if the parts are not 0
        while red_bin not in bin_list:
            red_bin = int(
                input('In which bin are red_parts located {}?'.format(bin_list)))
        if red_bin in bin_list:
            bin_list.remove(red_bin)  # to remove bins already in use

    while num_green_parts not in parts_in_bin_list:
        num_green_parts = int(
            input('How many green_parts in the workcell [0, 4, 9]?'))
    if num_green_parts > 0:  # It will ask about the location ONLY if the parts are not 0
        while green_bin not in bin_list:
            green_bin = int(
                input('In which bin are green_parts located {}?'.format(bin_list)))
        if green_bin in bin_list:
            bin_list.remove(green_bin)

    while num_blue_parts not in parts_in_bin_list:
        num_blue_parts = int(
            input('How many blue_parts in the workcell [0, 4, 9]?'))
    if num_blue_parts > 0:  # It will ask about the location ONLY if the parts are not 0
        while blue_bin not in bin_list:
            blue_bin = int(
                input('In which bin are blue_parts located {}?'.format(bin_list)))
        if blue_bin in bin_list:
            bin_list.remove(blue_bin)  # to remove bins already in use
        # else:
        #     print('ERROR: Bin already used for red_parts or green_parts!')

    print('=' * num)  # Formatting the output display
    while tray_color != 'y' and tray_color != 'g':
        tray_color = input('Which tray to use [(y)ellow, (g)ray]?')

    if tray_color == 'y':
        tray_type = 'yellow_tray'
        tray_location = 'yellow_tray_table'
    elif tray_color == 'g':
        tray_type = 'gray_tray'
        tray_location = 'gray_tray_table'
    else:
        print('ERROR: Enter a valid choice!')

    print('=' * num)  # Formatting the output display

    while agv not in agv_list:
        agv = int(input('Which AGV to use [1, 2, 3, 4]?'))

    if agv == 1 or agv == 2:
        while assm != 1 and assm != 2:
            assm = int(
                input('Which assembly station to ship agv{} [1, 2]?'.format(agv)))
    else:
        while assm != 3 and assm != 4:
            assm = int(
                input('Which assembly station to ship agv{} [3, 4]?'.format(agv)))

    print('=' * num)  # Formatting the output display

    if num_blue_parts >= 0:
        while blue_inTray != 0 and blue_inTray != 1 and blue_inTray != 2:
            blue_inTray = int(input('How many blue_parts in tray [0, 1, 2]?'))
    if num_green_parts >= 0:
        while green_inTray != 0 and green_inTray != 1 and green_inTray != 2:
            green_inTray = int(
                input('How many green_parts in tray [0, 1, 2]?'))
    if num_red_parts >= 0:
        while red_inTray != 0 and red_inTray != 1 and red_inTray != 2:
            red_inTray = int(input('How many red_parts in tray [0, 1, 2]?'))


if __name__ == '__main__':
    main()
