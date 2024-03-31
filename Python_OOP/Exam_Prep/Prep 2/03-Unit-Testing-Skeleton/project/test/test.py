from collections import deque
from unittest import TestCase, main
from project.railway_station import RailwayStation

class TestRailwayStation(TestCase):
    def setUp(self):
        self.s = RailwayStation("Sofia")
    def test_init_correctly(self):
        s = RailwayStation("Sofia")
        self.assertEqual(s.name, "Sofia")
        self.assertEqual(s.arrival_trains, deque())
        self.assertEqual(s.departure_trains, deque())

    def test_less_name_chars_raises_error(self):
        with self.assertRaises(ValueError) as ex:
            s = RailwayStation("So")
        self.assertEqual(str(ex.exception), "Name should be more than 3 symbols!")
        with self.assertRaises(ValueError) as ex:
            s = RailwayStation("Sof")
        self.assertEqual(str(ex.exception), "Name should be more than 3 symbols!")

    def test_new_arrival_on_board(self):
        self.assertEqual(len(self.s.arrival_trains), 0)
        self.assertEqual(self.s.arrival_trains, deque())
        self.s.new_arrival_on_board("Some info")

        self.assertEqual(len(self.s.arrival_trains), 1)
        self.assertEqual(self.s.arrival_trains, deque(["Some info"]))
    

if __name__ == '__main__':
    main()