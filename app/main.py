from course import Course
from aud import download_audio, delete_temp_file
import time
import io
import json

def main():
    url = 'https://youtu.be/WbzNRTTrX0g?si=glpoyB2Rcbgsrfxx'
    audio_file_path = download_audio(url)
    time.sleep(20)
'''    create_course = Course(audio_file_path)
    course_data = create_course.run()

    print(course_data)
    with open("testing_data.json", "w", encoding="utf-8") as file:
        json.dump(course_data, file, sort_keys=True, indent=2)'''

    # Удаление временного файла
    delete_temp_file(audio_file_path)

if __name__ == '__main__':
    main()