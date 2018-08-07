import unittest
from src import City


class TestCity(unittest.TestCase):
    def test_set_cube_count(self):
        test_city_atlanta = City.City("ATLANTA")
        test_city_atlanta.set_cube_count("BLACK", 3)
        test_city_atlanta.set_cube_count("BLUE", 2)
        test_city_atlanta.set_cube_count("RED", 1)
        test_city_atlanta.set_cube_count("YELLOW", 0)
        # Test if setting the cube values worked
        self.assertEqual(test_city_atlanta.black_cubes, 3)
        self.assertEqual(test_city_atlanta.blue_cubes, 2)
        self.assertEqual(test_city_atlanta.red_cubes, 1)
        self.assertEqual(test_city_atlanta.yellow_cubes, 0)
        # Test a cube value over 3
        self.assertRaises(ValueError, test_city_atlanta.set_cube_count, "BLACK", 4)
        # Test a bad color name
        self.assertRaises(ValueError, test_city_atlanta.set_cube_count, "BLAC", 2)

    def test_get_cube_count(self):
        test_city_atlanta = City.City("ATLANTA")
        test_city_atlanta.set_cube_count("BLACK", 3)
        test_city_atlanta.set_cube_count("BLUE", 2)
        test_city_atlanta.set_cube_count("RED", 1)
        test_city_atlanta.set_cube_count("YELLOW", 0)
        # Test if the function returns to correct number of cubes
        self.assertEqual(test_city_atlanta.get_cube_count("BLACK"), 3)
        self.assertEqual(test_city_atlanta.get_cube_count("BLUE"), 2)
        self.assertEqual(test_city_atlanta.get_cube_count("RED"), 1)
        self.assertEqual(test_city_atlanta.get_cube_count("YELLOW"), 0)
        # Test sending a bad color name
        self.assertRaises(ValueError, test_city_atlanta.get_cube_count, "BLAC")

    def test_add_one_cube(self):
        test_city_atlanta = City.City("ATLANTA")
        # Testing to see if cubes are added correctly for each color
        test_city_atlanta.set_cube_count("BLACK", 2)
        test_city_atlanta.set_cube_count("BLUE", 1)
        test_city_atlanta.set_cube_count("RED", 2)
        test_city_atlanta.set_cube_count("YELLOW", 1)
        test_city_atlanta.add_one_cube("BLACK")
        test_city_atlanta.add_one_cube("BLUE")
        test_city_atlanta.add_one_cube("RED")
        test_city_atlanta.add_one_cube("YELLOW")
        self.assertEqual(test_city_atlanta.get_cube_count("BLACK"), 3)
        self.assertEqual(test_city_atlanta.get_cube_count("BLUE"), 2)
        self.assertEqual(test_city_atlanta.get_cube_count("RED"), 3)
        self.assertEqual(test_city_atlanta.get_cube_count("YELLOW"), 2)
        # Test if an error occurs when trying to add a cube to a city with 3 cubes
        test_city_atlanta.set_cube_count("BLACK", 3)
        self.assertRaises(ValueError, test_city_atlanta.add_one_cube, "BLACK")
        # Test sending a bad color name
        self.assertRaises(ValueError, test_city_atlanta.add_one_cube, "BLAC")

    def test_remove_one_cube(self):
        test_city_atlanta = City.City("ATLANTA")
        # Test removing one cube from a city with cubes
        test_city_atlanta.set_cube_count("BLACK", 3)
        test_city_atlanta.set_cube_count("BLUE", 2)
        test_city_atlanta.set_cube_count("RED", 1)
        test_city_atlanta.set_cube_count("YELLOW", 3)
        test_city_atlanta.remove_one_cube("BLACK")
        test_city_atlanta.remove_one_cube("BLUE")
        test_city_atlanta.remove_one_cube("RED")
        test_city_atlanta.remove_one_cube("YELLOW")
        self.assertEqual(test_city_atlanta.get_cube_count("BLACK"), 2)
        self.assertEqual(test_city_atlanta.get_cube_count("BLUE"), 1)
        self.assertEqual(test_city_atlanta.get_cube_count("RED"), 0)
        self.assertEqual(test_city_atlanta.get_cube_count("YELLOW"), 2)
        # Test removing one cube from a city without cubes
        test_city_atlanta.set_cube_count("BLACK", 0)
        self.assertRaises(ValueError, test_city_atlanta.remove_one_cube, "BLACK")
        # Test sending a bad color name
        self.assertRaises(ValueError, test_city_atlanta.remove_one_cube, "BLAC")

    def test_get_largest_cube_count_color(self):
        test_city_atlanta = City.City("ATLANTA")
        # Test if it returns the cities largest cube count color
        test_city_atlanta.set_cube_count("BLACK", 3)
        test_city_atlanta.set_cube_count("BLUE", 2)
        test_city_atlanta.set_cube_count("RED", 1)
        test_city_atlanta.set_cube_count("YELLOW", 0)
        self.assertEqual(test_city_atlanta.get_largest_cube_count_color(), "BLACK")
        # Test if it returns the city's color if all of the cube counts are equal
        test_city_atlanta.set_cube_count("BLACK", 1)
        test_city_atlanta.set_cube_count("BLUE", 1)
        test_city_atlanta.set_cube_count("RED", 1)
        test_city_atlanta.set_cube_count("YELLOW", 1)
        self.assertEqual(test_city_atlanta.get_largest_cube_count_color(), test_city_atlanta.color)

    def test_remove_all_cubes(self):
        test_city_atlanta = City.City("ATLANTA")
        # Test to see if it removes all of the cubes from each color
        test_city_atlanta.set_cube_count("BLACK", 3)
        test_city_atlanta.set_cube_count("BLUE", 2)
        test_city_atlanta.set_cube_count("RED", 1)
        test_city_atlanta.set_cube_count("YELLOW", 0)
        test_city_atlanta.remove_all_cubes("BLACK")
        test_city_atlanta.remove_all_cubes("BLUE")
        test_city_atlanta.remove_all_cubes("RED")
        test_city_atlanta.remove_all_cubes("YELLOW")
        self.assertEqual(test_city_atlanta.get_cube_count("BLACK"), 0)
        self.assertEqual(test_city_atlanta.get_cube_count("BLUE"), 0)
        self.assertEqual(test_city_atlanta.get_cube_count("RED"), 0)
        self.assertEqual(test_city_atlanta.get_cube_count("YELLOW"), 0)
        # Test sending a bad color name
        self.assertRaises(ValueError, test_city_atlanta.remove_all_cubes, "BLAC")

    def test_add_max_cubes(self):
        test_city_atlanta = City.City("ATLANTA")
        # Test to see if it removes all of the cubes from each color
        test_city_atlanta.set_cube_count("BLACK", 3)
        test_city_atlanta.set_cube_count("BLUE", 2)
        test_city_atlanta.set_cube_count("RED", 1)
        test_city_atlanta.set_cube_count("YELLOW", 0)
        test_city_atlanta.add_max_cubes("BLACK")
        test_city_atlanta.add_max_cubes("BLUE")
        test_city_atlanta.add_max_cubes("RED")
        test_city_atlanta.add_max_cubes("YELLOW")
        self.assertEqual(test_city_atlanta.get_cube_count("BLACK"), 3)
        self.assertEqual(test_city_atlanta.get_cube_count("BLUE"), 3)
        self.assertEqual(test_city_atlanta.get_cube_count("RED"), 3)
        self.assertEqual(test_city_atlanta.get_cube_count("YELLOW"), 3)
        # Test sending a bad color name
        self.assertRaises(ValueError, test_city_atlanta.add_max_cubes, "BLAC")


if __name__ == "__main__":
    unittest.main()
