import os
import struct
import enum
import numpy as np

def readtimeStampFile(path):
    # Open the .fit file
    timeStamp = int(path.split("/")[1].split("-")[0])

    with open(path, 'rb') as f:
        data = f.read()

    uint16_array = struct.unpack('H' * (len(data) // 2), data)
    
    return [ (int(x) + timeStamp) for x in uint16_array]

def readPowerAndGCTFile(path):
    with open(path, 'rb') as f:
        data = f.read()

    uint16_array = struct.unpack('H' * (len(data) // 2), data)
    
    return [ int(x) for x in uint16_array]

def readLocationFile(path):
    with open(path, 'rb') as f:
        binary_data = f.read()

    # create a format string to specify the data type and byte order of the binary data
    format_string = '<' + 'f' * (len(binary_data) // 4)

    # unpack the binary data into a float array
    float_array = struct.unpack(format_string, binary_data)
    
    tuples_list = [(float_array[i], float_array[i+1]) for i in range(len(float_array)-1)]

    # print the contents of the float array to verify that the data was imported correctly
    return tuples_list

#returns float array
def readVerticalAndStrideFile(path):
    with open(path, 'rb') as f:
        binary_data = f.read()

    # create a format string to specify the data type and byte order of the binary data
    format_string = '<' + 'f' * (len(binary_data) // 4)

    # unpack the binary data into a float array
    float_array = struct.unpack(format_string, binary_data)

    # print the contents of the float array to verify that the data was imported correctly
    return float_array

# converts to int
def readHeartRateFile(path):

    with open(path, 'rb') as f:
        # read the binary data into a numpy array of uint8 data type
        uint8_array = np.fromfile(f, dtype=np.uint8)

    # print the contents of the uint8 array to verify the data was read correctly
    return uint8_array.astype(np.int32)
    


def main(directory):
    file_names = os.listdir(directory)

    HeartRateTvalues = []
    HeartRateQvalues = []
    
    LocationValues = []
    
    RunPowerTvalues = []
    RunPowerQvalues = []
    
    VerticalOscTvalues = []
    VerticalOscQvalues = []
    
    GroundContactTimeTvalues = []
    GroundContactTimeQvalues = []
    
    StrideTvalues = []
    StrideQvalues = []

    # Print the file names
    for file_name in file_names:
        path = "binFiles/" + file_name
        if "HeartRateT.bin" in file_name :
            # int array
            HeartRateTvalues = readtimeStampFile(path)
        elif "HeartRateQ.bin" in file_name :
            # int arraye çevirdim orijinali uint8
            HeartRateQvalues = readHeartRateFile(path)
        elif "Location" in file_name:
            # her arrayin elemanı tuple, lat long biçiminde
            LocationValues = readLocationFile(path)
        elif "RunPowerT.bin" in file_name :
            # int array
            RunPowerTvalues = readtimeStampFile(path)
        elif "RunPowerQ.bin" in file_name :
            # int array orijinali uint16
            RunPowerQvalues = readPowerAndGCTFile(path)
        elif "VerticalQ.bin" in file_name :
            # float array
            VerticalOscQvalues = readVerticalAndStrideFile(path)
        elif "VerticalT.bin" in file_name :
            VerticalOscTvalues = readtimeStampFile(path)
        elif "GCTQ.bin" in file_name :
            # int array orijinali uint16
            GroundContactTimeQvalues = readPowerAndGCTFile(path)
        elif "GCTT" in file_name:
            # int array
            GroundContactTimeTvalues = readtimeStampFile(path)
        elif "StrideT" in file_name:
            # int array
            StrideTvalues = readtimeStampFile(path)
        elif "StrideQ" in file_name:
            # float array
            StrideQvalues = readVerticalAndStrideFile(path)
        else:
            continue
    return


if __name__ == "__main__":
    main('binFiles/')
