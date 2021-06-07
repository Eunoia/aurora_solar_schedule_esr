"""
This module lets solar installers prioritize and manage their installation
crew given a list of buildings that they need to install a PV system on.
"""

# worker_types = [
#     'certified', 'pending', 'handy'
# ]

# buildingType = [
#     'short',
#     'tall',
#     'commercial'
# ]

# employees = [
#     {
#         'name': 'John',
#         'tier': 'certified',
#         'avail': [True, False, False, False, True, True, True],
#     }
# ]

def schedule(buildings, employees):
    """
    assign employees to buildings, creating a work schedule
    """

    work_order = []
    dow = 0
    while dow <= 4 and buildings:
        building = buildings.pop(0)
        print(building['address'])
        if building['type'] == 'short':
            unqualified_employee_count = 0

            for emp in employees:
                if emp['avail'][dow] and emp['tier'] == 'certified':
                    emp['avail'][dow] = False
                    print(
                        f"assinging {emp['name']} to {building['address']} on {dow}")
                    work_order.append([dow, building, emp])
                    dow = 0
                    break
                else:
                    unqualified_employee_count +=1
            if unqualified_employee_count == len(employees):
                print(f"no one assignable to {building['address']} on {dow}")
                if dow <= 4:
                    buildings = [building] + buildings
                else:
                    dow = 0
                dow += 1

    return work_order
