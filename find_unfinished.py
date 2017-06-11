import rows
import datetime

CSV_FILE = '/Users/blues/Desktop/subtitle_work/nd000.csv'
NAME = '權'

def get_date(date_text):
    return datetime.datetime.strptime(date_text, '%Y-%m-%d').date()

def find_unfinished():
    unfinished = []
    subtitles = rows.import_from_csv(CSV_FILE)
    for s in subtitles:
        if s.field_4 == NAME and s.field_5 != '已完成':
            unfinished.append(s)
    return unfinished

def out_put_subtitle(subtitle):
    print('Time: ' + subtitle.field_5)
    print('\t|section: ' + subtitle.field_8)
    print('\t|lesson: ' + subtitle.google_drive)
    print("-"*8)

def quicksort(x):
    if len(x) == 1 or len(x) == 0:
        return x
    else:
        pivot = get_date(x[0].field_5)
        i = 0
        for j in range(len(x)-1):
            if get_date(x[j+1].field_5) < pivot:
                x[j+1],x[i+1] = x[i+1], x[j+1]
                i += 1
        x[0],x[i] = x[i],x[0]
        first_part = quicksort(x[:i])
        second_part = quicksort(x[i+1:])
        first_part.append(x[i])
        return first_part + second_part


result = find_unfinished()
result = quicksort(result)
for s in result:
    out_put_subtitle(s)
