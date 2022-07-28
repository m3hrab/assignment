exam_marks =[
{
"ID":"204001",
"name": "A",
"CT": [18,7,17,11],#4 class test marks(out of 20 marks for each,total 60),consider only best 3
"Final_Exam": [[25,20,33],[10,34,15]], #marks of sectionA(out of 105) and sectionB (out of 105)

"Attendance": [27,36] # total presents, total classes (total marks 30)
},

{
"ID":"204002",
"name": "B",
"CT": [11,17,13,19],
"Final_Exam": [[28,0,33],[19,30,27]],
"Attendance": [28,36]
}
,
{
"ID":"204003",
"name": "C",
"CT": [10,14,9,18],
"Final_Exam": [[14,8,10],[6,13,9]],
"Attendance": [20,36]
},
{
"ID":"204004",
"name": "D",
"CT": [13,20,16,20],
"Final_Exam": [[29,17,33],[16,30,25]],
"Attendance": [32,36]
},
{
"ID":"204005",
"name": "E",
"CT": [0,8,6,0],
"Final_Exam": [[7,0,8],[11,0,0]],
"Attendance": [12,36]
}
]




def ct_marks(a):
    a.sort(reverse=True)
    x = (sum(a[:3]) * 20) / 100
    return x


def attendance(data):
    total_presents = data[0]
    total_class = data[1]
    attendance_parcentage = (total_presents * 100)/ total_class
    marks = (30 * attendance_parcentage)/100
    temp = (marks*10)/100
    return temp
    
    
def final_exam(marks):
    n = sum(marks[0]) + sum(marks[1])
    marks = (n * 100) / 210
    temp = (marks * 70)/ 100
    return temp


def grade(total):
    letter_grade = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'D']
    lt = 'F'
    temp = 80
    for grade in letter_grade:
        if total >= temp:
            lt = grade
            break
        temp -= 5
    
    return lt


for result in exam_marks:
    ct = result["CT"]
    final = result["Final_Exam"]
    at = result["Attendance"]
    total = ct_marks(ct) + attendance(at) + final_exam(final)

    msg = '"Hello, Student ' + result["name"] + " with ID: " + result["ID"] + " has obtained "
    msg += str(grade(total)) + '"'
    print(msg)
    