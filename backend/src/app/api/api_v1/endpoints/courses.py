from typing import List

from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from app import schemas, models
from app.crud import crud_course
from app.api import deps

router = APIRouter()

@router.post("/", response_model=schemas.courses.Course, status_code=201)
def create_course(course: schemas.courses.CourseCreate, 
                db: Session = Depends(deps.get_db), 
                current_user: schemas.user.User = Depends(deps.get_current_active_user)):
    return crud_course.create_course(db_session=db, course=course, user=current_user)


@router.get("/", response_model=List[schemas.courses.Course])
def read_courses(db: Session = Depends(deps.get_db), 
                current_user: schemas.user.User = Depends(deps.get_current_active_user)):
    """
    Read all courses for current user.
    """
    courses = crud_course.get_courses(db_session=db, user_id=current_user.user_id)
    return courses


@router.delete("/{course_id}", response_model=schemas.courses.Course)
def delete_course(course_id: int, 
                    db: Session = Depends(deps.get_db), 
                    current_user: schemas.user.User = Depends(deps.get_current_active_user)):
    db_course = crud_course.get_course(db_session=db, course_id=course_id, user_id=current_user.user_id)
    if not db_course:
        raise HTTPException(status_code=404, detail="Course not found.")
    db_course = crud_course.delete_course(db_session=db, course_id=course_id, user_id=current_user.user_id)
    return db_course


@router.get("/{course_id}", response_model=schemas.courses.Course)
def read_course(course_id: int, 
                db: Session = Depends(deps.get_db),
                current_user: schemas.user.User = Depends(deps.get_current_active_user)):
    db_course = crud_course.get_course(db_session=db, user_id=current_user.user_id, course_id=course_id)
    if not db_course:
        raise HTTPException(status_code=404, detail="Course not found.")
    return db_course


@router.put("/{course_id}", response_model=schemas.courses.Course)
def update_course(course_id: int, 
                  course: schemas.courses.CourseUpdate, 
                  db: Session = Depends(deps.get_db), 
                  current_user: schemas.user.User = Depends(deps.get_current_active_user)):
    print(course, 'eeeeeeeeeeeeeeeeeeeeeeeeeeeeeee<')
    #check if course exists
    db_course = crud_course.get_course(db_session=db, user_id=current_user.user_id, course_id=course_id)
    if not db_course:
        raise HTTPException(status_code=404, detail="Course not found.")
    db_course = crud_course.update_course(db_session=db, db_course=db_course, course_update=course)
    return db_course






