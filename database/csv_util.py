import csv
import time


# 保存 数据
def save(rows=None, header=None, save_file=""):
    if rows is None:
        rows = []
    if header is None:
        header = []
    if save_file == "":
        save_file = "tmp_" + str(int(time.ctime()))
    if len(rows) <= 0:
        return False
    if len(header) <= 0:
        header = rows[0]
        rows = rows[1:]
    with open(file=save_file, mode='w+', newline='', encoding='utf-8') as csvFile:
        csv_writer = csv.writer(csvFile)
        csv_writer.writerow(header)
        if len(rows) > 0:
            csv_writer.writerows(rows)
        csvFile.close()
        return True


# if __name__ == "__main__":
#    save(rows=[[1, 2, 3, 0], [1, 2, 3, 4]], header=["db", "sql", "lang", "name"], save_file="db.csv")

def transform(items=None):
    if items is None:
        return []
    arr = []
    for index in items:
        dit = {
            '期号': index['code'],
            '开奖日期': index['date'],
            '红球': index['red'],
            '蓝球': index['blue'],
            '一等奖中奖注数': index['prizegrades'][0]['typenum'],
            '一等奖中奖金额': index['prizegrades'][0]['typemoney'],
            '二等奖中奖注数': index['prizegrades'][1]['typenum'],
            '二等奖中奖金额': index['prizegrades'][1]['typemoney'],
            '三等奖中奖注数': index['prizegrades'][2]['typenum'],
            '三等奖中奖金额': index['prizegrades'][2]['typemoney'],
            '四等奖中奖注数': index['prizegrades'][3]['typenum'],
            '四等奖中奖金额': index['prizegrades'][3]['typemoney'],
            '五等奖中奖注数': index['prizegrades'][4]['typenum'],
            '五等奖中奖金额': index['prizegrades'][4]['typemoney'],
            '六等奖中奖注数': index['prizegrades'][5]['typenum'],
            '六等奖中奖金额': index['prizegrades'][5]['typemoney'],
            '一等奖中奖地区': index['content'],
            '奖池金额': index['poolmoney']
        }
        arr.append(dit)
    return arr


# 保存对象数据
def save_dicts(fieldnames=None, rowsDit=None, file_name='ssq.csv'):
    if rowsDit is None:
        return False
    if fieldnames is None:
        fieldnames = []
    f = open(file_name, mode='a', encoding='utf-8', newline='')
    csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
    # 写入表头
    csv_writer.writeheader()
    # 写入数据
    csv_writer.writerows(rowsDit)
    f.close()
    return True
