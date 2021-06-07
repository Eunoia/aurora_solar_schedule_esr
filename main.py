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

def schedulePrinter(work_order):
    days_of_week = ['Mon', 'Tues', 'Wed', 'Thurs', 'Fri']
    for job in work_order:
        print(f"{days_of_week[job[0]]} Building: {job[1]['address']}, worker: {job[2]['name']}")

if __name__ == '__main__':
    employees = [
        {
            'name': 'John',
            'tier': 'certified',
            'avail': [True, False, False, False, True],
        },
        {
            'name': 'Adam',
            'tier': 'certified',
            'avail': [False, False, True, False, True],
        }
    ]
    buildings = [
        {'address': 'i', 'type': 'short'},
        {'address': 'j', 'type': 'short'},
        {'address': 'k', 'type': 'short'},
        {'address': 'l', 'type': 'short'},
        {'address': 'm', 'type': 'short'},
        {'address': 'n', 'type': 'short'},
        {'address': 'o', 'type': 'short'},
        {'address': 'p', 'type': 'short'},
    ]
    work_order = schedule(buildings, employees)
    schedulePrinter(work_order)
