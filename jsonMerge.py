
with open(r'.\json\data1.json') as f1:
    f1data = f1.read()

with open(r'.\json\data2.json') as f2:
    f2data = f2.read()

with open(r'.\json\data3.json')as f3:
    f3data = f3.read()

f1data += "\n"
f2data += "\n"
f1data += f2data + f3data

with open(r'.\json\data4.json', 'a') as f4:
    f4.write(f1data)


print('the merged json is', f1data)