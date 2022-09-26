from typing import List
from urllib import response
from uuid import uuid4
from xml.dom import UserDataHandler
from fastapi import FastAPI,HTTPException
from models import Student,StudentUpdate,Course,CourseUpdate,Batch,BatchUpdate,Enrollment,EnrollmentUpdate
#from pydantic import BaseModel

app = FastAPI()

######################### STUDENT ################################################

db:List[Student]=[
    Student(
        student_id        = 1,
        student_name      = "Student_1",
        student_dob       = "12-04-2005",
        student_batchid   = 101,
        student_marks     = 34
        ),
    Student(
        student_id        = 2,
        student_name      = "Student_2",
        student_dob       = "27-11-2004",
        student_batchid   = 102,
        student_marks     = 23
        )
]


@app.get("/api/v1/getstudents",response_model=List[Student],response_model_exclude_unset=True)
async def get_students():
    return db


@app.get("/api/v1/getonestudent/{student_id}",response_model=Student,response_model_exclude_unset=True)
async def get_onestudent(student_id:int):
    for student in db:  
        if student.student_id == student_id:
            return student
    raise HTTPException(
        status_code=404,
        detail=f"Student with ID {student_id} does not exist !!"
    )

     
@app.post("/api/v1/addstudent",response_model=Student,response_model_exclude_unset=True)
async def add_student(student:Student):
    db.append(student)
    return student

@app.delete("/api/v1/deletestudent/{student_id}",response_model=Student,response_model_exclude_unset=True)
async def delete_student(student_id:int):
    for student in db:
        if student.student_id == student_id:
            db.remove(student)
            return student
    raise HTTPException(
        status_code=404,
        detail=f"Studnet with ID {student_id} does not exist !!"
    )
   
@app.put("/api/v1/updatestudent/{student_id}",response_model=Student,response_model_exclude_unset=True)
async def update_student(student_update:StudentUpdate,student_id:int):
    for student in db:
        if student.student_id == student_id:
            if student_update.student_name is not None:
                student.student_name = student_update.student_name
            if student_update.student_dob is not None:
                student.student_dob = student_update.student_dob
            if student_update.student_batchid is not None:
                student.student_batchid = student_update.student_batchid
            if student_update.student_marks is not None:
                student.student_marks = student_update.student_marks
            return student

    raise HTTPException(
        status_code=404,
        detail=f"Student with ID {student_id} does not exist !!"
    )
    
######################### COURSE ##############################################

db:List[Course]=[
    Course(
        course_id          = 200,
        course_name        = "Course_1",
        course_description = "Python",
        course_duration    = 6,
        course_fee         = 20000
        ),
    Course(
        course_id          = 201,
        course_name        = "Course_2",
        course_description = "Java",
        course_duration    = 4,
        course_fee         = 18000
        )
]
@app.get("/api/v1/getcourses",response_model=List[Course],response_model_exclude_unset=True)
async def get_courses():
    return db;

@app.get("/api/v1/getonecourse/{course_id}",response_model=Course,response_model_exclude_unset=True)
async def get_course(course_id:int):
    for course in db:
        if course.course_id == course_id:
            return course
    raise HTTPException(
        status_code=404,
        detail=f"Course with ID {course_id} does not exist !!"
    )

@app.post("/api/v1/addcourse",response_model=Course,response_model_exclude_unset=True)
async def add_course(course:Course):
    db.append(course)
    return course

@app.delete("/api/v1/deletecourse/{course_id}",response_model=Course,response_model_exclude_unset=True)
async def delete_course(course_id:int):
    for course in db:
        if course.course_id == course_id:
            db.remove(course)
            return course
    raise HTTPException(
        status_code=404,
        detail=f"Course with ID {course_id} does not exist !!"
    )

@app.put("/api/v1/updatecourse/{course_id}",response_model=Course,response_model_exclude_unset=True)
async def update_course(course_update:CourseUpdate,course_id:int):
    for course in db:
        if course.course_id == course_id:
            if course_update.course_name is not None:
                course.course_name = course_update.course_name
            if course_update.course_description is not None:
                course.course_description = course_update.course_description
            if course_update.course_duration is not None:
                course.course_duration = course_update.course_duration
            if course_update.course_fee is not None:
                course.course_fee = course_update.course_fee
            
            return course

    raise HTTPException(
        status_code=404,
        detail=f"Course with ID {course_id} does not exist !!"
    )

######################### BATCH ##############################################

db:List[Batch]=[
    Batch(
        batch_id            = 100,
        course_id           = 200,
        primary_trainerid   = 1000,
        secondary_trainerid = 2000,
        batch_startdate     = "10-10.2022",
        batch_enddate       = "01-03-2023"
        ),
    Batch(
        batch_id            = 101,
        course_id           = 201,
        primary_trainerid   = 1001,
        secondary_trainerid = 2001,
        batch_startdate     = "01-01.2023",
        batch_enddate       = "01-06-2023"
        )
]
@app.get("/api/v1/getbatches",response_model=List[Batch],response_model_exclude_unset=True)
async def get_batches():
    return db;

@app.post("/api/v1/addbatch",response_model=Batch,response_model_exclude_unset=True)
async def add_batch(batch:Batch):
    db.append(batch)
    return batch

@app.delete("/api/v1/deletebatch/{batch_id}",response_model=Batch,response_model_exclude_unset=True)
async def delete_batch(batch_id:int):
    for batch in db:
        if batch.batch_id == batch_id:
            db.remove(batch)
            return batch
    raise HTTPException(
        status_code=404,
        detail=f"Batch with ID {batch_id} does not exist !!"
    )

@app.put("/api/v1/updatebatch/{batch_id}",response_model=Batch,response_model_exclude_unset=True)
async def update_batch(batch_update:BatchUpdate,batch_id:int):
    for batch in db:
        if batch.batch_id == batch_id:
            if batch_update.course_id is not None:
                batch.course_id = batch_update.course_id
            if batch_update.primary_trainerid is not None:
                batch.primary_trainerid = batch_update.primary_trainerid
            if batch_update.secondary_trainerid is not None:
                batch.secondary_trainerid  = batch_update.secondary_trainerid 
            if batch_update.batch_startdate is not None:
                batch.batch_startdate  = batch_update.batch_startdate 
            if batch_update.batch_enddate is not None:
                batch.batch_enddate  = batch_update.batch_enddate 
            
            return batch

    raise HTTPException(
        status_code=404,
        detail=f"Batch with ID {batch_id} does not exist !!"
    )

######################### ENROLLMENT ##############################################

db:List[Enrollment]=[
    Enrollment(
        enrollment_id   = 10000,
        student_id      = 200,
        batch_id        = 100,
        enrollment_date = "11.12.2021"
        ),
    Enrollment(
        enrollment_id   = 10001,
        student_id      = 201,
        batch_id        = 101,
        enrollment_date = "01.01.2022"
        )
]
@app.get("/api/v1/getenrollments",response_model=List[Enrollment],response_model_exclude_unset=True)
async def get_enrollments():
    return db;

@app.post("/api/v1/addenrollment",response_model=Enrollment,response_model_exclude_unset=True)
async def add_enrollment(enrollment:Enrollment):
    db.append(enrollment)
    return enrollment

@app.delete("/api/v1/deleteenrollment/{enrollment_id}",response_model=Enrollment,response_model_exclude_unset=True)
async def delete_enrollment(enrollment_id:int):
    for enrollment in db:
        if enrollment.enrollment_id == enrollment_id:
            db.remove(enrollment)
            return enrollment
    raise HTTPException(
        status_code=404,
        detail=f"Enrollment with ID {enrollment_id} does not exist !!"
    )

@app.put("/api/v1/updateenrollment/{enrollment_id}",response_model=Enrollment,response_model_exclude_unset=True)
async def update_enrollment(enrollment_update:EnrollmentUpdate,enrollment_id:int):
    for enrollment in db:
        if enrollment.enrollment_id == enrollment_id:
            if enrollment_update.student_id is not None:
                enrollment.student_id = enrollment_update.student_id
            if enrollment_update.batch_id is not None:
                enrollment.batch_id = enrollment_update.batch_id
            if enrollment_update.enrollment_date is not None:
                enrollment.enrollment_date  = enrollment_update.enrollment_date 
            
            
            return enrollment

    raise HTTPException(
        status_code=404,
        detail=f"Enrollment with ID {enrollment_id} does not exist !!"
    )
