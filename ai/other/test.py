import math

class Grade:
    def __init__(self,grade,weight):
        self.grade = grade
        self.weight = weight


def main():
    grades = []
    int_des = Grade(7,5)
    web_tech = Grade(12,5)
    sem3proj = Grade(10,10)
    osds = Grade(4,5)
    mat1 = Grade(10,5)
    so = Grade(10,10)
    dm = Grade(10,5)
    vop = Grade(12,5)
    sem2proj = Grade(7,10)
    sem1proj = Grade(7,9)
    oop = Grade(12,10)
    stat = Grade(12,5)
    cos = Grade(10,5)
    grades.append(int_des)
    grades.append(web_tech)
    grades.append(sem3proj)
    grades.append(osds)
    grades.append(mat1)
    grades.append(so)
    grades.append(dm)
    grades.append(vop)
    grades.append(sem2proj)
    grades.append(sem1proj)
    grades.append(oop)
    grades.append(stat)
    grades.append(cos)
    print(weighted_avg(grades))


def weighted_avg(grades):
    sum = 0
    colWeight = 0
    for grade in grades:
        sum+= grade.weight * grade.grade
        colWeight += grade.weight
    return sum/colWeight
    

if __name__ == "__main__":
    main()