from project.parking_mall.parking_mall import ParkingMall


class Level2(ParkingMall):
    PARKING_LOTS = 100

    def __init__(self):
        ParkingMall.__init__(self, Level2.PARKING_LOTS)
