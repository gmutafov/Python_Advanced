from unittest import TestCase, main

from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self):
        self.mammal = Mammal(
            "someName",
            "someType",
            "someSound",
        )

    def test_correct_init(self):
        self.assertEqual("someName", self.mammal.name)
        self.assertEqual("someType", self.mammal.type)
        self.assertEqual("someSound", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_make_sound_returns_correct_string(self):
        self.assertEqual(f"someName makes someSound", self.mammal.make_sound())

    def test_get_kingdom_returns_correct_str(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_info_returns_correct_string(self):
        self.assertEqual(f"someName is of type someType", self.mammal.info())


if __name__ == '__main__':
    main()