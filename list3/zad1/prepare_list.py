class Preparer:
    @staticmethod
    def prepare_list(length):
        array = []
        f = open("/dev/urandom", 'rb')
        for i in range(100, 10001, 100):
            for j in range(length):
                array.append([int.from_bytes(f.read(4), byteorder='big') for _ in range(i)])
        return array
