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




# def put_update_device(db_session: Session, db_device: schemas.Device, device_update: schemas.DeviceBase):
#     db_device.device_name = device_update.device_name
#     db_device.description = device_update.description
#     db_session.commit()
#     return db_devicer