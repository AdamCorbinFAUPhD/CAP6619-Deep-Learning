# input X would be start (x,y) positions
# output Y would be be an array of [[x,y]] coordinates
import json
from pathlib import Path

array = [-0.064, 0.045, 1, -0.064, 0.045, 1, -0.057, 0.032, 1, -0.049, 0.026, 1, -0.045, 0.023, 1, -0.039, 0.019, 1,
         -0.021, 0.007, 1, -0.015, 0.004, 1, -0.011, 0.003, 1, -0.008, 0.002, 1, -0.006, 0.001, 1, -0.001, 0, 1, -0.001,
         0, 1, -0.001, 0, 1, -0.001, 0, 1, -0.001, 0, 1, -0.001, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0,
         0, 0]
array2 = [-0.064, 0.045, 1, -0.064, 0.045, 1, -0.057, 0.032, 1, -0.049, 0.026, 1, -0.045, 0.023, 1, -0.039, 0.019, 1,
          -0.021, 0.007, 1, -0.015, 0.004, 1, -0.011, 0.003, 1, -0.008, 0.002, 1, -0.006, 0.001, 1, -0.001, 0, 1,
          -0.001, 0, 1, -0.001, 0, 1, -0.001, 0, 1, -0.001, 0, 1, -0.001, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0,
          0, 1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0,
          0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0,
          0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0,
          0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0,
          0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0,
          0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0,
          0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0,
          0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0,
          0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0,
          0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0,
          0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0,
          0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1]
array3 = [-0.001,0.012,1,-0.001,0.012,1,0.006,0.003,1,0.008,0,1,0.01,-0.001,1,0.011,-0.002,1,0.012,-0.002,1,0.013,-0.004,1,0.014,-0.005,1,0.014,-0.005,1,0.014,-0.005,1,0.014,-0.005,1,0.014,-0.005,1,0.013,-0.005,1,0.012,-0.005,1,0.011,-0.005,1,0.011,-0.004,1,0.008,-0.004,1,0.008,-0.004,1,0.007,-0.004,1,0.005,-0.004,1,0.005,-0.004,1,0.005,-0.003,1,0.005,-0.003,1,0.005,-0.003,1,0.005,-0.003,1,0.005,-0.003,1,0.005,-0.003,1,0.005,-0.003,1,0.005,-0.003,1,0.005,-0.003,1,0.005,-0.003,1,0.005,-0.003,1,0.005,-0.003,1,0.005,-0.003,1,0.005,-0.003,1,0.005,-0.003,1,0.005,-0.003,1,0.005,-0.003,1,0.005,-0.003,1,0.005,-0.003,1,0.005,-0.003,1,0.005,-0.003,1,0.005,-0.003,1,0.005,-0.003,1,0.005,-0.003,1,0.005,-0.003,1,0.005,-0.003,1,0.005,-0.003,1,0.005,-0.003,1,0.005,-0.003,1,0.005,-0.003,1,0.005,-0.003,1,0.005,-0.003,1,0.005,-0.003,1,0.005,-0.003,1,0.005,-0.003,1,0.004,-0.003,1,0.004,-0.002,1,0.003,-0.002,1,0.001,-0.001,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1]
array4 = [-1.222,-0.149,1,-1.222,-0.149,1,-1.189,-0.154,1,-1.165,-0.161,1,-1.139,-0.17,1,-1.123,-0.18,1,-1.1,-0.194,1,-1.089,-0.2,1,-1.073,-0.203,1,-1.053,-0.204,1,-1.028,-0.204,1,-0.892,-0.204,1,-0.862,-0.204,1,-0.841,-0.204,1,-0.819,-0.204,1,-0.799,-0.204,1,-0.783,-0.206,1,-0.78,-0.207,1,-0.778,-0.208,1,-0.777,-0.209,1,-0.775,-0.21,1,-0.765,-0.214,1,-0.762,-0.217,1,-0.749,-0.225,1,-0.735,-0.231,1,-0.715,-0.238,1,-0.701,-0.242,1,-0.699,-0.243,1,-0.699,-0.243,1,-0.698,-0.243,1,-0.697,-0.243,1,-0.67,-0.245,1,-0.645,-0.248,1,-0.627,-0.249,1,-0.619,-0.249,1,-0.617,-0.249,1,-0.617,-0.249,1,-0.617,-0.249,1,-0.617,-0.249,1,-0.616,-0.249,1,-0.614,-0.249,1,-0.585,-0.249,1,-0.555,-0.251,1,-0.52,-0.252,1,-0.475,-0.253,1,-0.443,-0.253,1,-0.429,-0.247,1,-0.428,-0.244,1,-0.428,-0.243,1,-0.428,-0.242,1,-0.427,-0.242,1,-0.423,-0.242,1,-0.421,-0.241,1,-0.413,-0.241,1,-0.402,-0.241,1,-0.388,-0.241,1,-0.356,-0.24,1,-0.342,-0.236,1,-0.317,-0.228,1,-0.258,-0.211,1,-0.121,-0.161,1,0.004,-0.096,1,0.027,-0.069,1,0.031,-0.05,1,0.031,-0.035,1,0.031,-0.014,1,0.031,-0.007,1,0.031,-0.005,1,0.031,0,1,0.031,0.004,1,0.031,0.009,1,0.031,0.011,1,0.03,0.012,1,0.029,0.012,1,0.026,0.012,1,0.021,0.012,1,0.01,0.011,1,0.008,0.009,1,0.006,0.009,1,0.005,0.009,1,0.003,0.006,1,0.001,0.005,1,0.001,0.004,1,0.001,0.003,1,0.001,0.003,1,0.001,0.003,1,0.001,0.003,1,0.001,0.003,1,0,0.002,1,0,0.001,1,0,0,1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1]
array5 = [0.118,0.058,1,0.118,0.058,1,0.118,0.058,1,0.118,0.058,1,0.118,0.058,1,0.118,0.058,1,0.118,0.058,1,0.118,0.058,1,0.118,0.058,1,0.118,0.058,1,0.118,0.058,1,0.118,0.058,1,0.118,0.058,1,0.118,0.058,1,0.118,0.058,1,0.118,0.058,1,0.118,0.058,1,0.118,0.058,1,0.118,0.058,1,0.118,0.058,1,0.118,0.058,1,0.118,0.058,1,0.118,0.058,1,0.118,0.058,1,0.118,0.058,1,0.118,0.058,1,0.119,0.058,1,0.124,0.058,1,0.125,0.059,1,0.126,0.059,1,0.126,0.059,1,0.126,0.059,1,0.126,0.059,1,0.128,0.059,1,0.128,0.059,1,0.128,0.059,1,0.13,0.059,1,0.13,0.059,1,0.132,0.059,1,0.132,0.059,1,0.133,0.059,1,0.133,0.059,1,0.135,0.059,1,0.135,0.06,1,0.137,0.062,1,0.137,0.062,1,0.143,0.063,1,0.144,0.063,1,0.144,0.063,1,0.145,0.063,1,0.145,0.063,1,0.145,0.063,1,0.145,0.063,1,0.145,0.063,1,0.145,0.063,1,0.145,0.063,1,0.145,0.063,1,0.145,0.063,1,0.145,0.063,1,0.145,0.063,1,0.145,0.063,1,0.145,0.063,1,0.145,0.063,1,0.145,0.063,1,0.145,0.063,1,0.145,0.063,1,0.145,0.063,1,0.145,0.063,1,0.145,0.063,1,0.145,0.063,1,0.145,0.063,1,0.145,0.063,1,0.145,0.063,1,0.145,0.063,1,0.145,0.063,1,0.145,0.063,1,0.145,0.063,1,0.145,0.063,1,0.145,0.063,1,0.145,0.063,1,0.145,0.063,1,0.145,0.063,1,0.145,0.063,1,0.145,0.063,1,0.145,0.063,1,0.145,0.063,1,0.145,0.063,1,0.145,0.063,1,0.145,0.063,1,0.145,0.063,1,0.145,0.063,1,0.145,0.063,1,0.145,0.063,1,0.145,0.063,1,0.145,0.063,1,0.145,0.063,1,0.145,0.063,1,0.145,0.063,1,0.145,0.063,1,0.145,0.063,1,0.145,0.063,1,0.145,0.063,1,0.145,0.063,1,0.145,0.063,1,0.145,0.063,1,0.145,0.063,1,0.145,0.063,1,0.145,0.063,1,0.146,0.063,1,0.146,0.063,1,0.146,0.063,1,0.148,0.063,1,0.149,0.063,1,0.149,0.063,1,0.152,0.066,1,0.152,0.066,1,0.152,0.066,1,0.152,0.066,1,0.151,0.065,1,0.126,0.046,1,0.103,0.033,1,0.084,0.025,1,0.076,0.018,1,0.053,0.01,1,0.047,0.007,1,0.038,0.005,1,0.034,0.005,1,0.026,0.004,1,0.004,-0.002,1,0.004,-0.002,1,0.004,-0.002,1,0.004,-0.002,1,0.004,-0.002,1,0.004,-0.002,1,0.004,-0.002,1,0.004,-0.002,1,0.001,-0.002,1,0,0,1,0,0,1,0,0,1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1]
array6 = [-0.07,-0.006,0.096,-0.039,1,0.096,-0.039,1,0.095,-0.039,1,0.092,-0.039,1,0.076,-0.034,1,0.065,-0.033,1,0.039,-0.026,1,0.03,-0.021,1,0.027,-0.019,1,0.026,-0.017,1,0.023,-0.017,1,0.016,-0.014,1,0.016,-0.014,1,0.013,-0.012,1,0.011,-0.01,1,0.009,-0.009,1,0.001,-0.001,1,0,0,1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1]
print(len(array) / 3)
print(len(array2)/3)
print(len(array3)/3)
print(len(array4)/3)
print(len(array5)/3)
x_set = []
y_set = []
last = ()
arrays = [array, array2, array3, array4, array5]

# for aa in arrays:
#     for i in range(0, len(aa), 3):
#         x = aa[i]
#         y = aa[i+1]
#         complete = aa[i+2]
#         if last != (x,y,complete):
#             print(x,y,complete)
#         last = (x,y,complete)
#     print("-----------")


# startX = array6[0] * 1000
# startY = array6[1] * 1000
# print(startX,startY)
# array6 = array6[2:]
# for i in range(0, len(array6), 3):
#     x = array6[i] * 1000
#     y = array6[i+1] * 1000
#     complete = array6[i+2]
#     if last != (x,y,complete):
#         print(x,y,complete)
#     last = (x,y,complete)
# print("-----------")

for file in Path("C:\\Users\\C0rbin\\Documents\\GitHub\\BotDashboard\\mouse_data__2021_03_18").glob("*.*"):
    data = json.load(open(str(file)))
    for row in data:
        row = row.split(",")
        print(row)
        id = row[0]
        random_num = row[1]
        lastDeltaX = row[2]
        lastDeltaY = row[3]
        row = row[4:]
        print(f"size: {len(row)/3}")
        for i in range(0, len(row), 3):
            x = float(row[i]) * 1000
            y = float(row[i+1]) * 1000
            complete = row[i+2]
            if last != (x,y,complete):
                print(x,y,complete)
            last = (x,y,complete)

    exit()