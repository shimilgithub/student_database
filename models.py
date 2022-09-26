from ctypes import Union
from distutils.command.build_scripts import first_line_re
from typing import Optional,List,Union
from pydantic import BaseModel

class Student(BaseModel):
    student_id        : int
    student_name      : str
    student_dob       : str
    student_batchid   : int
    student_marks     : int


    
class StudentUpdate(BaseModel):
    student_name      : str
    student_dob       : str
    student_batchid   : int
    student_marks     : int

class Course(BaseModel):
    course_id           : int 
    course_name         : str
    course_description  : str
    course_duration     : int    
    course_fee          : int

class CourseUpdate(BaseModel):
    course_name         : str
    course_description  : str
    course_duration     : int    
    course_fee          : int

class Batch(BaseModel):
    batch_id                : int
    course_id               : int
    primary_trainerid       : int
    secondary_trainerid     : int
    batch_startdate         : str
    batch_enddate           : str

class BatchUpdate(BaseModel):
    course_id               : int
    primary_trainerid       : int
    secondary_trainerid     : int
    batch_startdate         : str
    batch_enddate           : str

class Enrollment(BaseModel):
    enrollment_id       : int
    student_id          : int
    batch_id            : int 
    enrollment_date     : str

class EnrollmentUpdate(BaseModel):
    student_id          : int
    batch_id            : int 
    enrollment_date     : str


    