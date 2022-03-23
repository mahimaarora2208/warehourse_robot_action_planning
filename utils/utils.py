from pprint import pprint

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


def main():
    pprint(current_state)


if __name__ == '__main__':
    main()
