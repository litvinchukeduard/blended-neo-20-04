import random

"""
 ---
|___|
|___|
|___|
 ---
"""

dice_faces = [
    [
        ' _________ ',
        '|         |',
        '|    *    |',
        '|         |',
        '|_________|'
    ],
    [
        ' _________ ',
        '|         |',
        '|  *   *  |',
        '|         |',
        '|_________|'
    ],
    [
        ' _________ ',
        '|         |',
        '|  * * *  |',
        '|         |',
        '|_________|'
    ],
    [
        ' _________ ',
        '|         |',
        '|  * * *  |',
        '|    *    |',
        '|_________|'
    ],
    [
        ' _________ ',
        '|         |',
        '|  * * *  |',
        '|  * *    |',
        '|_________|'
    ],
    [
        ' _________ ',
        '|         |',
        '|  * * *  |',
        '|  * * *  |',
        '|_________|'
    ]
]

def draw_dice_face(n: int) -> str:
    if n < 1 or n > 6:
        return ""
    dice_face = dice_faces[n - 1]
    return '\n'.join(dice_face)

def roll_dice() -> list[str]:
    dice_one_value = random.randint(1, 6)
    dice_two_value = random.randint(1, 6)

    dice_one_face = draw_dice_face(dice_one_value)
    dice_two_face = draw_dice_face(dice_two_value)
    return [dice_one_face, dice_two_face]

print("Result:")
for dice_face in roll_dice():
    print(dice_face)

# lst = ['1', '2', '3'] # str()
# print(', '.join(lst))
