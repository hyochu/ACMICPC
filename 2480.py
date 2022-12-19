a = list(map(int, input().split(" ")))
setArr = []
duple = []
for i in a:
  if i not in setArr:
    setArr.append(i)
    setArr = sorted(setArr)
  else:
    duple.append(i)
if len(setArr) == 3:
  for i in setArr:
    result = setArr[-1]
  print(result*100)
if len(setArr) == 2:
  for i in duple:
    result = duple[-1]
  print(1000+result*100)
if len(setArr) == 1:
  for i in setArr:
    result = setArr[-1]
  print(10000+result*1000)
