import serial

class hw():
    PORT = 'COM6'  # PC에 연결된 포트
    baud = 19200  # 보드레이트
    ser = serial.Serial(PORT, baud, timeout=1)
    startBit = 0xAA

    def start(self):

        #data =[0xAA,0x05, 0x01, 0x01, 0xF8] #0x 데이터 값
        main_command = 0x01
        sub_command = 0x01
        packet = bytearray()
        packet.append(hw.startBit)
        data = [main_command, sub_command]
        length = len(data) + 0x03
        packet.append(length)
        for d in data:
            packet.append(d)
        checksum =~(length + sum(data)) & 0xFF
        packet.append(checksum)
        print(packet)
        hw.ser.write(packet)

    def stop(self):
        main_command = 0x01
        sub_command = 0x00
        packet = bytearray()
        packet.append(hw.startBit)
        data = [main_command, sub_command]
        length = len(data) + 0x03
        packet.append(length)
        for d in data:
            packet.append(d)
        checksum = ~(length + sum(data)) & 0xFF
        packet.append(checksum)
        print(packet)
        hw.ser.write(packet)

    def path_A(self):
        main_command = 0x03
        sub_command = 0x01
        packet = bytearray()
        packet.append(hw.startBit)
        data = [main_command, sub_command]
        length = len(data) + 0x03
        packet.append(length)
        for d in data:
            packet.append(d)
        checksum = ~(length + sum(data)) & 0xFF
        packet.append(checksum)
        print(packet)
        hw.ser.write(packet)

    def path_B(self):
        main_command = 0x03
        sub_command = 0x02
        packet = bytearray()
        packet.append(hw.startBit)
        data = [main_command, sub_command]
        length = len(data) + 0x03
        packet.append(length)
        for d in data:
            packet.append(d)
        checksum = ~(length + sum(data)) & 0xFF
        packet.append(checksum)
        print(packet)
        hw.ser.write(packet)

    def path_C(self):
        main_command = 0x03
        sub_command = 0x03
        packet = bytearray()
        packet.append(hw.startBit)
        data = [main_command, sub_command]
        length = len(data) + 0x03
        packet.append(length)
        for d in data:
            packet.append(d)
        checksum = ~(length + sum(data)) & 0xFF
        packet.append(checksum)
        print(packet)
        hw.ser.write(packet)

    def speed_up(self):
        main_command = 0x04
        sub_command = 0x01
        packet = bytearray()
        packet.append(hw.startBit)
        data = [main_command, sub_command]
        length = len(data) + 0x03
        packet.append(length)
        for d in data:
            packet.append(d)
        checksum = ~(length + sum(data)) & 0xFF
        packet.append(checksum)
        print(packet)
        hw.ser.write(packet)

    def speed_down(self):
        main_command = 0x04
        sub_command = 0x02
        packet = bytearray()
        packet.append(hw.startBit)
        data = [main_command, sub_command]
        length = len(data) + 0x03
        packet.append(length)
        for d in data:
            packet.append(d)
        checksum = ~(length + sum(data)) & 0xFF
        packet.append(checksum)
        print(packet)
        hw.ser.write(packet)


