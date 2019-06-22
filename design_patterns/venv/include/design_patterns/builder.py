class Computer:
    def __init__(self, serial_number):
        self.serial = serial_number
        self.memory = None
        self.hdd = None
        self.gpu = None

    def __str__(self):
        info = ('Memory: {}GB'.format(self.memory),
                'Hard Disk: {}GB'.format(self.hdd),
                'Graphics Cards: {}'.format(self.gpu))
        return '\n'.join(info)


class ComputerBuilder:
    def __init__(self):
        self.computer = Computer('HT589426')

    def configure_memory(self, amount):
        self.computer.memory = amount

    def configure_hdd(self, amount):
        self.computer.hdd = amount

    def configure_gpu(self, gpu_model):
        self.computer.gpu = gpu_model


class Hardware:
    def __init__(self):
        self.builder = None

    def construct_computer(self, memory, hdd, gpu):
        self.builder = ComputerBuilder()
        [step for step in (self.builder.configure_memory(memory),
                           self.builder.configure_hdd(hdd),
                           self.builder.configure_gpu(gpu))]


    @property
    def computer(self):
        return self.builder.computer


def main():
    engineer = Hardware()
    engineer.construct_computer(hdd=input("Insert hdd:"), memory=input("Insert memory:"), gpu=input("Insert Gpu:"))
    computer = engineer.computer
    print(computer)


if __name__ == '__main__':
    main()