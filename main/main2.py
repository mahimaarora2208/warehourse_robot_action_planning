'''
Contains program implementation to prompt user for kitting information.

'''

# from robot.gantry_robot import GantryRobot
# from robot.linear_robot import LinearRobot
# from gripper.gripper import Gripper
# from utils.utils import current_state
# import sys
# sys.path.insert(1, 'D:\projects\ENPM809E\rwa2_arora_mahima')

import pprint

# from gripper.gripper import Gripper
# from robot.gantry_robot import GantryRobot
# from robot.linear_robot import LinearRobot


def get_dig_from_str(list_str):
    int_ele_in_str = []
    for ele in list_str:
        for s in ele:
            if s.isdigit():
                int_ele_in_str.append(int(s))
    return int_ele_in_str


def main():
    ##################### User Interface to Input kitting information #####################
    current_state = {
        'parts': ['red_part', 'green_part', 'blue_part'],
        'agvs': {
            "agv1": {
                "possible_destination": ["as1", "as2"],
                "destination": None
            },
            "agv2": {
                "possible_destination": ["as1", "as2"],
                "destination": None
            },
            "agv3": {
                "possible_destination": ["as3", "as4"],
                "destination": None
            },
            "agv4": {
                "possible_destination": ["as3", "as4"],
                "destination": None
            },
        },
        'trays': {
            'yellow_tray': {
                'location': 'table',
                'expected_parts': [],
                'current_parts': []
            },
            'gray_tray': {
                'location': 'table',
                'expected_parts': [],
                'current_parts': []
            }
        },
        'bins': {
            'bin1': {
                'part_type': None,
                'part_quantity': 0
            },
            'bin2': {
                'part_type': None,
                'part_quantity': 0
            },
            'bin3': {
                'part_type': None,
                'part_quantity': 0
            },
            'bin4': {
                'part_type': None,
                'part_quantity': 0
            },
        },
        'kit': {
            'tray': None,
            'complete': False,
            'agv': None
        }
    }

    num = 100  # number to format display
    assm_for_agv = ''
    valid_parts_in_workcell = [0, 4, 9]
    parts_in_workcell = ''
    bin_for_part = ''
    red_bin = 0  # initalise the bin0 if no parts in bin
    green_bin = 0  # initalise the bin0 if no parts in bin
    blue_bin = 0  # initalise the bin0 if no parts in bin
    blue_inTray = -1
    red_inTray = -1
    green_inTray = -1
    tray_color = ''
    tray_type = ''
    agv = ''
    red_bin = ''
    green_bin = ''
    blue_bin = ''
    assm = ''
    num_blue_parts = -1
    num_green_parts = -1
    num_red_parts = -1

    # Get agvs from dictionary
    agv_dict = current_state['agvs']
    agv_list = list(agv_dict.keys())
    int_agv_list = get_dig_from_str(agv_list)

    # Get bins from dictionary
    bin_dict = current_state['bins']
    bin_list = list(bin_dict.keys())
    valid_bin_list = get_dig_from_str(bin_list)

    print('=' * num)  # Formatting the output display
    total_parts = len(current_state['parts'])

    for part in current_state['parts']:
        while parts_in_workcell not in valid_parts_in_workcell:
            parts_in_workcell = int(
                input('How many {} in the workcell [0, 4, 9]?'.format(part)))
        if parts_in_workcell > 0:
            while bin_for_part not in valid_bin_list:
                bin_for_part = int(
                    input('In which bin are {0} located {1}?'.format(part, valid_bin_list)))
            if bin_for_part in valid_bin_list:
                # to remove bins already in use
                valid_bin_list.remove(bin_for_part)
            current_state['bins']['bin' +
                                  str(bin_for_part)]['part_type'] = part
            current_state['bins']['bin' +
                                  str(bin_for_part)]['part_quantity'] = parts_in_workcell
            if part == 'red_part':
                num_red_parts = parts_in_workcell
            if part == 'green_part':
                num_green_parts = parts_in_workcell
            if part == 'blue_part':
                num_blue_parts = parts_in_workcell
            # if current_state['bins']['bin' +
            #                       str(bin_for_part)]['part_type'] == 'red_parts':
            #     num_red_parts =  current_state['bins']['bin' +
            #                       str(bin_for_part)]['part_type']
        parts_in_workcell = ''

    # Get Tray information
    while tray_color != 'y' and tray_color != 'g':
        tray_color = input('Which tray to use [(y)ellow, (g)ray]?')

    if tray_color == 'y':
        tray_type = 'yellow_tray'
        # tray_location = 'yellow_tray_table'
    elif tray_color == 'g':
        tray_type = 'gray_tray'
        # tray_location = 'gray_tray_table'
    else:
        print('ERROR: Enter a valid choice!')


# Get AGV information
    while agv not in int_agv_list:
        agv = int(input('Which AGV to use {}?'.format(int_agv_list)))

    agv_str = 'agv' + str(agv)
    selected_agv = current_state['agvs'][agv_str]
    destination_agv = selected_agv['possible_destination']
    int_assm_list = get_dig_from_str(destination_agv)
    if agv == 1 or agv == 2:
        while assm_for_agv != 1 and assm_for_agv != 2:
            assm_for_agv = int(
                input('Which assembly station to ship {0} {1}?'.format(agv_str, int_assm_list)))

    if agv == 3 or agv == 4:
        while assm_for_agv != 3 and assm_for_agv != 4:
            assm_for_agv = int(
                input('Which assembly station to ship {0} {1}?'.format(agv_str, int_assm_list)))

    selected_agv['destination'] = 'as' + str(assm_for_agv)

    print('=' * num)  # Formatting the output display

    # Update expected List and Current List
    # Red part

    if num_red_parts > 0:
        while red_inTray != 0 and red_inTray != 1 and red_inTray != 2:
            red_inTray = int(input('How many red_parts in tray [0, 1, 2]?'))
    if num_blue_parts > 0:
        while blue_inTray != 0 and blue_inTray != 1 and blue_inTray != 2:
            blue_inTray = int(input('How many blue_parts in tray [0, 1, 2]?'))
    if num_green_parts > 0:
        while green_inTray != 0 and green_inTray != 1 and green_inTray != 2:
            green_inTray = int(
                input('How many green_parts in tray [0, 1, 2]?'))

    # check if parts in bin are less than required
    if(blue_inTray > num_blue_parts or red_inTray > num_red_parts or green_inTray > num_green_parts):
        print('ERROR: Parts in the bin are not enough!')
        print('NO SOLUTION FOUND!')
        exit()

    while red_inTray != 0 and red_inTray > 0:
        current_state['trays'][tray_type]['expected_parts'].append('red_part')
        red_inTray -= 1

    while blue_inTray != 0 and blue_inTray > 0:
        current_state['trays'][tray_type]['expected_parts'].append('blue_part')
        blue_inTray -= 1

    while green_inTray != 0 and green_inTray > 0:
        current_state['trays'][tray_type]['expected_parts'].append(
            'green_part')
        green_inTray -= 1
    # pprint.pprint(current_state)

# Kitting Information
    current_state['kit']['agv'] = agv_str
    current_state['kit']['tray'] = tray_type

# Instantiating Gripper and Plan Robot Path
    gantry_g = Gripper('gantry_gripper')
    gantry_r = GantryRobot()
    gantry_r.plan()

    linearg = Gripper('linear_gripper')
    gantry_r = LinearRobot()

    if current_state['trays'][tray_type]['expected_parts'] == current_state['trays'][tray_type]['current_parts']:
        current_state['kit']['complete'] = True
    print('=' * num)  # Formatting the output display

    pprint.pprint(current_state)


if __name__ == '__main__':
    main()
