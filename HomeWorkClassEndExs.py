class Building:
    total = 0
    def __init__(self):
        Building.total += 1


build_ = []
for i in range(40):
    build_.append(Building())
    print(build_[i], Building.total)
print(build_)