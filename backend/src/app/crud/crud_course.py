from sqlalchemy.orm import Session

from app import models
from app.schemas import courses, user

def create_course(db_session: Session, course: courses.CourseCreate, user: user.User):
    db_course = models.Course(**course.dict(), owner_id=user.user_id)
    db_session.add(db_course)
    db_session.commit()
    db_session.refresh(db_course)
    return db_course

def get_courses(db_session: Session, user_id: int):
    return db_session.query(models.Course).filter(models.Course.owner_id == user_id).all()


def get_course(db_session: Session, course_id: int, user_id: int):
    return db_session.query(models.Course).filter(models.Course.owner_id == user_id) \
                                          .filter(models.Course.course_id == course_id).first()

def delete_course(db_session: Session, course_id: int, user_id: int):
    course_db = db_session.query(models.Course).filter(models.Course.owner_id == user_id) \
                                          .filter(models.Course.course_id == course_id).first()
    db_session.delete(course_db)
    db_session.commit()
    return course_db

def update_course(db_session: Session, db_course: courses.Course, course_update: courses.CourseCreate):
    db_course.course_provider = course_update.course_provider
    db_course.course_name = course_update.course_name
    db_course.course_start_date = course_update.course_start_date
    db_course.course_status = course_update.course_status
    db_course.course_URL = course_update.course_URL
    db_course.course_payment_type = course_update.course_payment_type
    db_session.commit()
    return db_course