import glob, json
from public_data.api_caller import save_data
fl = glob.glob('./1202/'+"*.json")

all = []

print(len(fl))
cnt = 0
for fn in fl:
    with open(fn) as f:
        jo = json.loads(f.read())
        # print(jo)
        all += jo
    cnt += 1

print('cnt:', cnt)

save_data(all, './all.json')
