import json
import math

# 圓心的緯度和經度
center_latitude = 25.0396
center_longitude = 121.5124

# 圓的半徑（以度為單位，這裡我們選擇了一個非常小的值，以生成一個緊密的圓）
radius = 0.001

# 圓的高度
altitude = 100

# 點的數量
num_points = 200

# 每個點之間的角度（以弧度為單位）
angle_step = 2 * math.pi / num_points

path = []
for i in range(num_points):
    # 計算這個點的角度
    angle = i * angle_step

    # 計算這個點的緯度和經度
    latitude = center_latitude + radius * math.cos(angle)
    longitude = center_longitude + radius * math.sin(angle)

    # 將這個點添加到路徑中
    path.append({"latitude": latitude, "longitude": longitude, "altitude": altitude})

# 將路徑保存到一個 JSON 文件中
with open('path.json', 'w') as f:
    json.dump({"path": path}, f)
