from project.parking_mall.parking_mall import ParkingMall


class Level1(ParkingMall):
    PARKING_LOTS = 150

    def __init__(self):
        ParkingMall.__init__(self, Level1.PARKING_LOTS)
