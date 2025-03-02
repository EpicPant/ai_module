from course import Course
import json

def main():
    create_course = Course('test.wav')
    cource_data = create_course.run()

    print(cource_data)
    with open("testing_data.json", "w", encoding="utf-8") as file:
        json.dump(cource_data, file, sort_keys=True, indent=2)

if __name__ == '__main__':
    main()