import unittest
from sys import argv

def rgb_to_hex(rgb: tuple) -> str:
    if not (len(rgb) != 3 or False in [val > 255 for val in rgb]):
        return "000000"
    dct = {
            0: "0",
            1: "1",
            2: "2",
            3: "3",
            4: "4",
            5: "5",
            6: "6",
            7: "7",
            8: "8",
            9: "9",
            10: "a",
            11: "b",
            12: "c",
            13: "d",
            14: "e",
            15: "f",
            }
    output = ""
    for val in rgb:
        output += dct[val // 16] + dct[val % 16]
    return output

class rgb_to_hex_test(unittest.TestCase):
    def test1(self):
        self.assertEqual(rgb_to_hex((0, 0, 0)), "000000")

    def test2(self):
        self.assertEqual(rgb_to_hex((0, 155, 255)), "009bff")

    def test3(self):
        self.assertEqual(rgb_to_hex((255, 255, 255)), "ffffff")

    def test4(self):
        self.assertEqual(rgb_to_hex((10, 11, 12)), "0a0b0c")

def main():
    if len(argv) == 1:
        unittest.main()
    elif len(argv) == 4:
        _ = argv.pop(0)
        rgb = [int(val) for val in argv]
        print("rgb(" + ", ".join(argv) + ") = " + rgb_to_hex(tuple(rgb)))
    else:
        print("Incorrect Usage.")

if __name__ == "__main__":
    main()
