def get_distance(address1, address2, distance_list):
    address_row = 0
    address_row_found = False
    address_column = 0
    address_column_found = False
    distance = 0
    for sublist in distance_list:
        if address1 in sublist[0]:
            address_row = distance_list.index(sublist)
            address_row_found = True
            break
    if not address_row_found:
        raise Exception("ADDRESS NOT FOUND ERROR\n" + address1 + "\n not found in distance table.")

    for element in distance_list[0]:
        if (element.find(address2) > 0) or (address2 == element):
            address_column = distance_list[0].index(element)
            address_column_found = True
            break
    if not address_column_found:
        raise Exception("ADDRESS NOT FOUND ERROR\n" + address2 + " \n not found in distance table.")
    distance = distance_list[address_row][address_column]
    if distance == '':
        distance = distance_list[address_column][address_row]
    return float(distance)
