import rows

CSV_FILE = '/Users/blues/Desktop/nd000.csv'
NAME = '權'


def find_unfinished():
    subtitles = rows.import_from_csv(CSV_FILE)
    for s in subtitles:
        if s.field_4 == NAME and s.field_5 != '已完成':
            print('section: ' + s.field_8)
            print('lesson: ' + s.google_drive)
            print('\t-' + s.field_5)
            print("----")
            
find_unfinished()
