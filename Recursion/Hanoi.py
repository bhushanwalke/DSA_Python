__author__ = 'bhushan'


def move_disk(fp, tp):
    print("Moving disk from", fp, "to", tp)


def move_tower(height, fromPole, toPole, withPole):
    if height >=1:
        move_tower(height-1, fromPole, withPole, toPole)
        move_disk(fromPole, toPole)
        move_tower(height-1, withPole, toPole, fromPole)


move_tower(4, "A", "B", "C")
