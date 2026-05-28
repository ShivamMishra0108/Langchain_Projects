from pydantic import BaseModel, EmailStr
from typing import Optional

class Student(BaseModel):

    name: str = 'shivam'
    age: Optional[int] = None
    emai: EmailStr

new_student = {'name':'shivam','age':32,'email':'abc@gmail.com'}

student = Student(**new_student)


print(student)
