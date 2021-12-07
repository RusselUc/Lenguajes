from datetime import date, timedelta, datetime
import pandas as pd

def bin(decimal):
    binario = ''
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario

def basica(line):

     if line[0:4] == '>REV':

        if line[1:2] == 'R':
            print('Indice calificador: Response')
        elif line[1:2] == 'Q':
            print('Indice calificador: Query')
        elif line[1:2] == 'S':
            print('Indice calificador: Set')

        if line[2:4] == 'EV':
            print('Event Message')
        print('Indice del evento: '+ line[4:6])

        static_date = datetime(1980, 1, 6, 00, 00, 00)

        ts = timedelta(weeks = int(line[6:10]),days = int (line[10:11]))

        static_date = static_date + ts
        tseg = timedelta(seconds = int(line[11:16]))
        static_date = static_date + tseg
        horaR = timedelta(hours=6)
        static_date = static_date - horaR

        print('Fecha: '+ str(static_date.day) + "-" + str(static_date.month) + "-" + str(static_date.year))

        dateToday = str(static_date.year) + "-" + str(static_date.month) + "-" + str(static_date.day)

        temp = pd.Timestamp(dateToday)
        print(temp.day_name())
        
        # if line[10:11] == '0':
        #     print('Dia de la semana: Domingo')
        # elif line[10:11] == '1':
        #     print('Dia de la semana: Lunes')
        # elif line[10:11] == '2':
        #     print('Dia de la semana: Martes')
        # elif line[10:11] == '3':
        #     print('Dia de la semana: Miercoles')
        # elif line[10:11] == '4':
        #     print('Dia de la semana: Jueves')
        # elif line[10:11] == '5':
        #     print('Dia de la semana: Viernes')
        # elif line[10:11] == '6':
        #     print('Dia de la semana: Sabado')
        
        # static_date = datetime(1980, 1, 6, 00,00, 00)
        # print(type(hora))
        print('Hora del evento: '+ str(static_date.hour) + ':' + str(static_date.minute)+ ':' + str(static_date.second))
        
        latitud = float(line[17:24])/100000
        longitud = float(line[25:33])/100000
        print('Latitud: '+ line[16:17]+str(latitud))
        print('Longitud: '+ line[24:25]+str(longitud))

        velocidad = float(line[33:36]) * 1.61
        print('Velocidad: '+ str(velocidad) + ' km/h')

        print('Orientacion: '+ line[36:39])

        if line[39:40] == '0':
            print('2D GPS')
        elif line[39:40] == '1':
            print('3D GPS')
        elif line[39:40] == '2':
            print('2D DGPS')
        elif line[39:40] == '3':
            print('3D DGPS')
        elif line[39:40] == '9':
            print('UNKNOWN')

        if line[40:41] == '0':
            print('NOT AVAILABLE')
        elif line[39:40] == '1':
            print('OLDER THAN 10 SECONDS')
        elif line[39:40] == '2':
            print('FRESH, LESS THAN 10 SECONDS')
        elif line[39:40] == '9':
            print('GPS FAILURE')

def extendida(line):
    basica(line)
    io = line[45:48]
    numero = int(io[0:1])
    io = bin(numero)

    if io[0:1] == '1':
        print('Ignicion: ACTIVO')
    else:
        print('Ignicion: INACTIVO')

    if io[1:2] == '1':
        print('Fuente de alimentación: EXT-PWR')
    else:
        print('Fuente de alimentación: BACKUP-BATTERY')

    print(line[49:53])
    print(line[54:58])
    if line[59:61] == 'VO':
        print(line[59:67])

def imei(line, flag):
    if flag:
        print(line[42:60])
    else:
         print(line[68:86])
        

file = open('Clase.txt', 'r')
cont = 0
start = 0
end = 0
for line in file:
    # else:
    #     cont += 1

    for i in line:
        if i == ">":
            start = cont
            #print(start)
        elif i == "<":
            end = cont
            # print(end)
        lineaN = line[start:end]
        if lineaN[0:4] == '>REV':
            if lineaN[42:44] == 'ID':
                basica(lineaN)
                imei(lineaN, True)
                print('')
            else:
                extendida(lineaN)
                imei(lineaN, False)
                print('')
        # print(lineaN)
        cont += 1
    start = 0
    end = 0
    cont = 0
    # print(str(start) + " : " + str(end))
    # 


file.close()
