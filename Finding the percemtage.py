if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    licz = student_marks[query_name]
    dlug = len(licz)
    suma = sum(licz)
    wynik = suma / dlug
    print("%.2f" % wynik)

