"""
Unit tests for scheduling work crews to install solar setups
"""

import unittest
import main


class TestSkedOneEmployeee(unittest.TestCase):
    """
    Tests if one employee can install one system. This test is to make sure
    the code works in the simplest case
    """

    # @unittest.skip("skipping")
    def test_schedule(self):
        employees = [
          {
            'name': 'John',
            'tier': 'certified',
            'avail': [True, True, True, True, True],
          }
        ]
        buildings = [{
          'address': '1', 'type': 'short',
        }]
        work_order = main.schedule(buildings, employees)
        self.assertTrue(work_order)
        self.assertEqual(len(work_order), 1)
        dow, building, worker = work_order[0]
        self.assertEqual(dow, 0)
        self.assertEqual(building['type'], 'short')
        self.assertEqual(worker['name'], 'John')


class TestSkedTwoEmployeesThreeBuildings(unittest.TestCase):
    """
    Tests if a coupe employees with different availabilities can install a few
    systems over the course of the week.
    """
    # @unittest.skip("skipping")
    def test_schedule(self):
        employees = [
          {
              'name': 'John',
              'tier': 'certified',
              'avail': [True, False, False, False, True],
          },
          {
              'name': 'Adam',
              'tier': 'certified',
              'avail': [True, False, True, False, False],
          }
        ]
        buildings = [
          {'address': 'd', 'type': 'short'},
          {'address': 'e', 'type': 'short'},
          {'address': 'f', 'type': 'short'},
        ]
        work_order = main.schedule(buildings, employees)
        # pdb.set_trace()
        self.assertTrue(work_order)
        self.assertEqual(len(work_order), 3)
        # John should get the first day
        dow, building, worker = work_order[0]
        self.assertEqual(dow, 0)
        self.assertEqual(building['address'], 'd')
        self.assertEqual(worker['name'], 'John')
        # Then Adam should get the third day
        dow, building, worker = work_order[1]
        self.assertEqual(dow, 0)
        self.assertEqual(building['address'], 'e')
        self.assertEqual(worker['name'], 'Adam')
        # Then either should get the fifth day
        dow, building, worker = work_order[2]
        self.assertEqual(dow, 2)
        self.assertEqual(building['address'], 'f')
        self.assertEqual(worker['name'], 'Adam')


class TestSkedMoreJobsThanEmployees(unittest.TestCase):
    """
    Tests what happens when there are too many jobs to be done.
    """
    # @unittest.skip("skipping")
    def test_schedule(self):
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
        worker_avail = sum([sum(e['avail']) for e in employees])
        work_order = main.schedule(buildings, employees)
        # pdb.set_trace()
        self.assertTrue(work_order)
        # All available labor is assigned to a job
        self.assertEqual(len(work_order), worker_avail)
        # Order of importance is perserved in assignments
        addresses = [wo[1]['address'] for wo in work_order]
        self.assertEqual(addresses, ['i', 'j', 'k', 'l'])

        # John should get the first day
        dow, _building, worker = work_order[0]
        self.assertEqual(dow, 0)
        self.assertEqual(worker['name'], 'John')
        # Then Adam should get the next day
        dow, _building, worker = work_order[1]
        self.assertEqual(dow, 2)
        self.assertEqual(worker['name'], 'Adam')

        # Both are working the last day
        dow, _building, worker = work_order[2]
        self.assertEqual(dow, 4)
        self.assertEqual(worker['name'], 'John')
        # Both are working the last day
        dow, _building, worker = work_order[3]
        self.assertEqual(dow, 4)
        self.assertEqual(worker['name'], 'Adam')

if __name__ == '__main__':
    unittest.main()
