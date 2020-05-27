from sqlalchemy import  Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship

from app.db.base_class import Base

class Course(Base):    
    course_id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("user.user_id"))
    course_provider = Column(String())
    course_name = Column(String())
    course_start_date = Column(Date)
    course_status = Column(String())
    course_URL = Column(String())
    course_payment_type = Column(String())

    users = relationship("User", back_populates="courses")


