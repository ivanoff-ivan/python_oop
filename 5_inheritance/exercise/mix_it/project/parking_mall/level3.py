from project.parking_mall.parking_mall import ParkingMall


class Level3(ParkingMall):
    PARKING_LOTS = 80

    def __init__(self):
        ParkingMall.__init__(self, Level3.PARKING_LOTS)
