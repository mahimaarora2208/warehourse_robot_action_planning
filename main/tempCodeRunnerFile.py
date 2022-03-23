
#  while red != 0:
#         if(red_parts['bin']['name'] == 'bin1' or red_parts['bin']['name'] == 'bin2'):
#             robo = 'robot_floor'
#         else:
#             robo = 'robot_ceiling'
#         pickup_part(robo,
#                     red_parts['bin']['name'], 'red_part')
#         red -= 1
#         place_part(robo, tray_type, 'red_parts', 'agv' + str(agv))
#     while blue != 0:
#         if(blue_parts['bin']['name'] == 'bin1' or blue_parts['bin']['name'] == 'bin2'):
#             robo = 'robot_floor'
#         else:
#             robo = 'robot_ceiling'
#         pickup_part(robo,
#                     blue_parts['bin']['name'], 'blue_part')
#         blue -= 1
#         place_part(robo, tray_type, 'blue_parts', 'agv' + str(agv))
#     while green != 0:
#         if(green_parts['bin']['name'] == 'bin1' or green_parts['bin']['name'] == 'bin2'):
#             robo = 'robot_floor'
#         else:
#             robo = 'robot_ceiling'
#         pickup_part(robo,
#                     green_parts['bin']['name'], 'green_part')
#         green -= 1
#         place_part(robo, tray_type, 'green_parts', 'agv' + str(agv))

#     kit_tray[tray_type]['status'] = 'complete'
#     ship_agv('agv' + str(agv), tray_type, 'as' + str(assm))
#     print('=' * num)  # Formatting the output display