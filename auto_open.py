# encoding=utf-8
import rows
import os

APP = 'TextEdit'
opened_id = []
SUB_FOLDER = '/Users/blues/Downloads/subtitles/locales/zh-cn'
CSV_FILE = '/Users/blues/Desktop/subtitle_work/nd000.csv'
NAME = '權'


def find_subtitle_id(lesson_name):
    """
    return github id that match lesson name
    """
    subtitles = rows.import_from_csv(CSV_FILE)
    for s in subtitles:
        if lesson_name in s.google_drive:
            if s.github not in opened_id:
                opened_id.append(s.github)
                return s.github
    return None


def open_file_with_id(github_id):
    """
    open file with subtitle id
    """
    file_path = '{0}/{1}.srt'.format(SUB_FOLDER, github_id)
    cmd = 'open -a {0} {1}'.format(APP, file_path)
    os.system(cmd)


while True:
    lesson_name = os.popen('pbpaste').read()
    sub_id = find_subtitle_id(lesson_name)
    if sub_id is not None:
        open_file_with_id(sub_id)
        print('open file with:' + sub_id)
