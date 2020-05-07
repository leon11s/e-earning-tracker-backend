import datetime

class CourseBase(BaseModel):
    course_provider: str
    course_name: str
    course_start_date: datetime.date
    course_status: str
    course_URL: str = None


    # course_end_date: datetime.date = None
    # course_type: str
    # course_payment_type: str
    # course_price: float
    # course_payment_date: str
    # course_is_cert: bool
    # course_main_topic: str

class CourseCreate(CourseBase):
    pass

class CourseUpdate(CourseBase):
    pass

class Course(CourseBase):
    course_id: int

    class Config:
        orm_mode = True