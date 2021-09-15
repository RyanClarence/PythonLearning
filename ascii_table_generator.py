#!/usr/bin/env python3
###########################################################
#  Author Name : Sboniso Gordon Mziz                      #
###########################################################
def to_binary(value):
    binary_data = [0,0,0,0,0,0,0,0]
    status = True
    count = -1
    final_binary_data = ""
    while status:
        binary_value = value % 2
        binary_data[count] = binary_value
        value = int(value / 2)
        if value <= 0:
            status = False
        count += -1
    for bit in binary_data:
        final_binary_data += str(bit)
    return(final_binary_data)


def to_octal(value):
    binary_data = to_binary(value)
    splited_binary_data = []
    splited_binary_data.append(binary_data[:2])
    splited_binary_data.append(binary_data[2:5])
    splited_binary_data.append(binary_data[5:])
    octal_result = ""

    for octal in splited_binary_data:
        if octal == "000" or octal == "00":
            octal_result += "0"
        elif octal == "001" or octal == "01":
            octal_result += "1"
        elif octal == "010":
            octal_result += "2"
        elif octal == "011":
            octal_result += "3"
        elif octal == "100":
            octal_result += "4"
        elif octal == "101":
            octal_result += "5"
        elif octal == "110":
            octal_result += "6"
        elif octal == "111":
            octal_result += "7"

    return octal_result

def to_hexedecimal(value):
    binary_data = to_binary(value)
    splited_binary_data = []
    splited_binary_data.append(binary_data[:4])
    splited_binary_data.append(binary_data[4:])
    hexa_result = ""

    for hexa in splited_binary_data:
        if hexa == "0000":
            hexa_result += "0"
        if hexa == "0001":
            hexa_result += "1"
        if hexa == "0010":
            hexa_result += "2"
        if hexa == "0011":
            hexa_result += "3"
        if hexa == "0100":
            hexa_result += "4"
        if hexa == "0101":
            hexa_result += "5"
        if hexa == "0110":
            hexa_result += "6"
        if hexa == "0111":
            hexa_result += "7"
        if hexa == "1000":
            hexa_result += "8"
        if hexa == "1001":
            hexa_result += "9"
        if hexa == "1010":
            hexa_result += "A"
        if hexa == "1011":
            hexa_result += "B"
        if hexa == "1100":
            hexa_result += "C"
        if hexa == "1101":
            hexa_result += "D"
        if hexa == "1110":
            hexa_result += "E"
        if hexa == "1111":
            hexa_result += "F"
        
    return hexa_result


def to_char(value):
    list_of_character ={"0":"NUL","1":"SOH","2":"STX","3":"ETX","4":"EOT","5":"ENQ","6":"ACK","7":"BEL","8":"BS","9":"TAB","10":"LF",
    "11":"VT","12":"FF","13":"CR","14":"CR","15":"SI","16":"DLE","17":"CD1","18":"CD2","19":"CD3","20":"CD4","21":"NAK","22":"SYN",
    "23":"ETB","24":"CAN","25":"EM","26":"SUB","27":"ESC","28":"FS","29":"GS","30":"RS","31":"US","32":"SPACE","33":"!","34":"\"",
    "35":"#","36":"$","37":"%","38":"&","39":"\'","40":"(","41":")","42":"*","43":"+","44":",","45":"-","46":".","47":"/","48":"0",
    "49":"1","50":"2","51":"3","52":"4","53":"5","54":"6","55":"7","56":"8","57":"9","58":":","59":";","60":"<","61":"=","62":">",
    "63":"?","64":"@","65":"A","66":"B","67":"C","68":"D","69":"E","70":"F","71":"G","72":"H","73":"I","74":"J","75":"K","76":"L",
    "77":"M","78":"N","79":"O","80":"P","81":"Q","82":"R","83":"S","84":"T","85":"U","86":"V","87":"W","88":"X","89":"Y","90":"Z",
    "91":"[","92":"\\","93":"]","94":"^","95":"_","96":"`","97":"a","98":"b","99":"c","100":"d","101":"e","102":"f","103":"g",
    "104":"h","105":"i","106":"j","107":"k","108":"l","109":"m","110":"n","111":"o","112":"p","113":"q","114":"r","115":"s",
    "116":"t","117":"u","118":"v","119":"w","120":"x","121":"y","122":"z","123":"{","124":"|","125":"}","126":"~","127":"DEL"
    }
    return list_of_character.get(str(value))

if __name__ == "__main__":
    print(""" _______________ASCII TABLE GENERATOR_______________ \n""")
    print("Decimal\t\tBinary\t\tOctal    Hex    Char\n")
    for i in range(128):
        print(f"{i}\t\t{to_binary(i)}\t{to_octal(i)}\t{to_hexedecimal(i)}\t{to_char(i)}")