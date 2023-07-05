import time

with open('replay.txt', 'r', encoding='utf-8') as f:
    replayFile = f.read()

splitData = replayFile.split('\n')

indicator = 0

resultData = ''

fmt = '%H:%M:%S'

firstTimestamp = 0

multiplyTime = 4

while indicator < len(splitData):
    if splitData[indicator] == '':
        indicator += 1
        continue
    orgTime = splitData[indicator][1:9]
    convertedTime = time.strptime("2023-07-05 " + orgTime, "%Y-%m-%d %H:%M:%S")
    timeStamp = int(time.mktime(convertedTime))
    if firstTimestamp == 0:
        firstTimestamp = timeStamp

    processedTime = time.localtime(((timeStamp - firstTimestamp) / multiplyTime) + firstTimestamp)
    finalTimeStr = time.strftime('%H:%M:%S', processedTime)
    resultData += splitData[indicator][0] + finalTimeStr + splitData[indicator][9:] + '\n'
    indicator += 1
    resultData += splitData[indicator] + '\n\n'
    indicator += 1

with open('result.txt', 'w', encoding='utf-8') as f:
    f.write(resultData)
