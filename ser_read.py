import serial

# 포트 설정
ser = serial.Serial('COM4', 115200, timeout=1)

# 데이터를 지속적으로 읽어오며 출력
try:
    print("실행중.")
    while True:
        # 데이터를 한 줄씩 읽음
        line = ser.readline()
        if line:  # 빈 줄이 아닌 경우만 출력
            #print(line.decode())
            #print(line);
            # 바이너리 데이터를 문자열로 디코드
            decoded_string = line.decode('ascii', errors='replace')
            print(decoded_string.strip())


except KeyboardInterrupt:
    print("프로그램을 종료합니다.")
finally:
    ser.close()
