#!/usr/bin/env python
# -*- coding: utf-8 -*- 

data = [
['红目鲫', [1, 2, 3, 11, 12], 'a', '900', 'r', 's'],
['锦鲤', [1,2,3,4,5,6,7,8,9,10,11,12], '16-9', 4000, 'pd', 'sb'],
['淡水龙虾', [4,5,6,7,8,9], 'a', 200, 'pd', 'ss'],
['塘鳢鱼', [1,2,3,4,5,6,7,8,9,10,11,12], '16-9', 400, 'r', 'ss'],
['黄鲈鱼', [1,2,3,10,11,12], 'a', 300, 'r', 'm'],
['香鱼 ',[7,8,9], 'a', 900, 'r', 'm'],
['鲑鱼',[9], 'a', 700, 'r', 'sb'],
['神仙鱼',[5,6,7,8,9,10], '16-9', 3000, 'r', 'ss'],
['骨舌鱼',[6,7,8,9], '16-9', 10000, 'r', 'sb'],
['鲟鱼',[1,2,3,9,10,11,12], 'a', 10000, 'r', 'eb'],
['耳带蝴蝶鱼',[4,5,6,7,8,9], 'a', 10000, 'o', 'ss'],
['凤尾鱼',[1,2,3,4,5,6,7,8,9,10,11,12], '4-21', 200, 'o', 's'],
['鲽鱼',[1,2,3,4,10,11,12], 'a', 300, 'o', 'm'],
['鲔鱼',[1,2,3,4,11,12], 'a', 7000, 'p', 'eb'],
['鳐鱼',[8,9,10,11], '4-21', 3000, 'o', 'b'],
['吸盘鱼',[6,7,8,9], 'a', 1500, 'o', 'sb'],
['溪哥',[1,2,3,4,5,6,7,8,9,10,11,12], '9-16', 200, 'r', 's'],
['金鱼',[1,2,3,4,5,6,7,8,9,10,11,12], 'a', 1300, 'pd', 's'],
['鳖',[8,9], '16-9', 3750, 'r', 'm'],
['泥鳅',[3,4,5], 'a', 4000, 'r', 'ss'],
['黑鲈鱼',[1,2,3,4,5,6,7,8,9,10,11,12], 'a', 320, 'r', 'sb'],
['樱花钩吻鲑',[3,4,5,6,9,10,11], '16-9', 1000, 'pd', 'm'],
['帝王鲑',[9], 'a', 1800, 'es', 'eb'],
['斗鱼',[5,6,7,8,9,10], '9-16', 2500, 'r', 's'],
['黄金河虎',[6,7,8,9], '4-21', 15000, 'r', 'b'],
['海蝴蝶',[1,2,3,12], 'a', 1000, 'o', 's'],
['苏眉鱼',[7, 8], '4-21', 10000, 'o', 'eb'],
['竹荚鱼',[1,2,3,4,5,6,7,8,9,10,11,12], 'a', 150, 'o', 'ss'],
['比目鱼',[1,2,3,4,5,6,7,8,9,10,11,12], 'a', 800, 'o', 'sb'],
['旗鱼',[1,2,3,4,7,8,9,11,12], 'a', 10000, 'p', 'eb'],
['锯鲨',[6,7,8,9], '16-9', 12000, 'o', 'shark'],
['灯笼鱼',[1,2,3,11,12], '16-9', 2500, 'o', 'sb'],
['鲫鱼',[1,2,3,4,5,6,7,8,9,10,11,12], 'a', 160, 'r', 'ss'],
['龙睛金鱼',[1,2,3,4,5,6,7,8,9,10,11,12], '9-16', 1300, 'pd', 's'],
['拟鳄龟',[4,5,6,7,8,9,10], '21-4', 5000, 'r', 'm'],
['鲶鱼',[5,6,7,8,9,10], '16-9', 800, 'pd', 'sb'],
['吴郭鱼',[6,7,8,9,10], 'a', 800, 'r', 'sb'],
['花羔红点熊',[3,4,5,6,9,10,11],'16-9', 3800, 'pd', 'sb'],
['中华绒螯蟹',[9,10,11], '16-9', 20000, 'r', 'ss'],
['霓虹灯鱼',[4,5,6,7,8,9,10,11], '9-16', 500, 'r', 's'],
['雀鳝',[6,7,8,9], '16-9', 6000, 'pd', 'eb'],
['海马',[4,5,6,7,8,9,10,11], 'a', 1100, 'o', 's'],
['狮子鱼',[4,5,6,7,8,9,10,11], 'a', 500, 'o', 'm'],
['条石鲷',[3,4,5,6,7,8,9,10,11], 'a', 5000, 'o', 'm'],
['鱿鱼',[1,2,3,4,5,6,7,8,12], 'a', 500, 'o', 'm'],
['白面弄鱼',[5,6,7,8,9,10], 'a', 4500, 'p', 'b'],
['双鬓鲨',[6,7,8,9], '16-9', 8000, 'o', 'shark'],
['皇带鱼',[1,2,3,4,5,12], 'a', 9000, 'o', 'eb'],
['雅罗鱼',[1,2,3,4,5,6,7,8,9,10,11,12], '16-9', 240, 'r', 'm'],
['兰寿金鱼',[1,2,3,4,5,6,7,8,9,10,11,12], '9-16', 4500, 'pd', 's'],
['蝌蚪',[3,4,5,6,7], 'a', 100, 'pd', 's'],
['黑鱼',[6,7,8], '9-16', 5500, 'pd', 'b'],
['白斑狗鱼',[9,10,11,12], 'a', 1800, 'r', 'b'],
['金鳟',[3,4,5,6,9,10,11], '16-9', 15000, 'c', 'm'],
['孔雀鱼',[4,5,6,7,8,9,10,11], '9-16', 1300, 'r', 's'],
['彩虹鱼',[5,6,7,8,9,10], '9-16', 800, 'r', 's'],
['巨骨舌鱼',[6,7,8,9], '16-9', 10000, 'r', 'eb'],
['小丑鱼',[4,5,6,7,8,9], 'a', 650, 'o', 's'],
['河豚',[11,12,1,2], '9-16, 21-4', 5000, 'o', 'm'],
['鲈鱼',[1,2,3,4,5,6,7,8,9,10,11,12], 'a', 400, 'o', 'b'],
['裸胸鳝',[8,9,10], 'a', 2000, 'o', 'eb'],
['鬼头刀',[5,6,7,8,9,10], 'a', 6000, 'p', 'eb'],
['鲨鱼',[6,7,8,9], '16-9', 15000, 'o', 'shark'],
['太平洋桶眼鱼',[1,2,3,4,5,6,7,8,9,10,11,12], '21-4', 15000, 'o', 'ss'],
['鲤鱼',[1,2,3,4,5,6,7,8,9,10,11,12], 'a', 300, 'pd', 'sb'],
['稻田鱼',[4,5,6,7,8], 'a', 300, 'pd', 's'],
['青蛙',[5,6,7,8], 'a', 120, 'pd', 'ss'],
['蓝腮太阳鱼',[1,2,3,4,5,6,7,8,9,10,11,12], '9-16',180, 'r', 's'],
['西太公鱼',[1,2,12], 'a', 400, 'r', 'ss'],
['远东哲罗鱼',[12,1,2,3], '16-9', 15000, 'c', 'eb'],
['温泉医生鱼',[5,6,7,8,9], '9-16', 1500, 'r', 'ss'],
['食人鱼',[6,7,8,9], '9-16,21-4', 2500, 'r', 'ss'],
['恩氏多鳍鱼',[6,7,8,9], '21-4', 4000, 'r', 'sb'],
['拟刺尾鲷',[4,5,6,7,8,9], 'a', 1000, 'o', 'ss'],
['刺豚',[7,8,9], 'a', 250, 'o', 'm'],
['鲷鱼',[1,2,3,4,5,6,7,8,9,10,11,12], 'a', 3000, 'o', 'm'],
['五彩鳗',[6,7,8,9,10], 'a', 600, 'o', 'snake'],
['翻车鱼',[7,8,9], '4-21', 4000, 'o', 'shark'],
['鲸鲨',[6,7,8,9], 'a', 13000, 'o', 'shark'],
['矛尾鱼',[1,2,3,4,5,6,7,8,9,10,11,12], 'a', 15000, 'or', 'eb']
]

a = "一整天"
location_map = {
    'r': '小河',
    'pd': '鱼塘',
    'o': '大海',
    'p': '码头',
    'es': '河口', 
    'c': '悬崖峭壁',
    'or': '下雨天的大海'
}
size_map = {
    's': '小',
    'm': '中',
    'b': '大',
    'sb': '有点儿大',
    'ss': '有点儿小',
    'eb': '超大',
    'shark': '鲨鱼形状',
    'snake': '🐍'
}
out = [None for _ in range(0, 80)]
for idx, line in enumerate(data):
    name = line[0]
    months = line[1]
    time = line[2]
    if time == 'a':
        time = a
    price = line[3]
    location = location_map[line[4]]
    size = size_map[line[5]]

    data = ('{{name:"{0}", price: {1}, location: "{2}", shadowSize: "{3}", time: "{4}", availMonths: {{north: {5}}}}},'.format(
        name, price, location, size, time, months
    ))

    out[(idx / 16) + (idx % 16) * 5] = data
for line in out:
    print(line)