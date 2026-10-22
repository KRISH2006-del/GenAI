from pydantic import BaseModel, Field, EmailStr, ValidationError

class Student(BaseModel):
    name: str = Field(..., description="The name of the student")
    age: int = Field(..., gt=0, description="The age of the student, must be greater than 0")
    email: EmailStr = Field(..., description="The email address of the student")
    cgpa: float = Field(..., ge=0.0, le=4.0, description="The CGPA of the student, must be between 0.0 and 4.0")


new_student ={'name':"John Doe", 'age':20, 'email':"john.doe@example.com", 'cgpa':3.5}

student = Student(**new_student)

print(student.dump(dict())) 