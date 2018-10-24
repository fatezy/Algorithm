class Car:
    def __init__(self,status,code,time):
        """
        初始化车
        :param status: 状态 A代表到达，D代表离开
        :param code: 车牌号
        :param time: 到达或离开的时间
        """
        self.status = status
        self.code = code
        self.time = time

#
# class ParkingArea:
#     def cost