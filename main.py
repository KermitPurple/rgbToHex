import unittest

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

if __name__ == "__main__":
    unittest.main()
