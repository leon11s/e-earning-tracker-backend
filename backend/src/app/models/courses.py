from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Date
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db import Base 





class Course(Base):
    __tablename__ = "courses"
    
    course_id = Column(Integer, primary_key=True, index=True)
    course_provider = Column(String())
    course_name = Column(String())
    course_start_date = Column(Date)
    course_status = Column(String())
    course_URL = Column(String())

    def __init__(self, course_provider, course_name, course_start_date, course_status, course_URL=None):
        self.course_provider = course_provider
        self.course_name = course_name
        self.course_start_date = course_start_date
        self.course_status = course_status
        self.course_URL = course_URL