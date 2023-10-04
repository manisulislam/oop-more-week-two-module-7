class CPU:
    def __init__(self, cores) -> None:
        self.cores= cores
    

class RAM:
    def __init__(self,size) -> None:
        self.size= size

class hardDrive:
    def __init__(self, capacity) -> None:
        self.capacity= capacity


class Computer:
    def __init__(self, cores, rm_size, hd_capacity) -> None:
        self.cores= CPU(cores)
        self.ram= RAM(rm_size)
        self.hard_disc= hardDrive(hd_capacity)

mac= Computer(8,100,512)