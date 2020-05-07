from fastapi import APIRouter, Depends, HTTPException


router = APIRouter()

@router.get("/")
def test_course():
    return {"endpoit":"course"}


# @router.get("/", response_model=List[schemas.Course]) # TODO: dodaj auth za endpoint 
# def read_devices(db: Session = Depends(get_db)):
#     """
#     Read all courses for current user.
#     """
#     courses = crud.get_courses(db)
#     return courses

# @router.post("/", response_model=schemas.Course, status_code=201) # TODO: dodaj auth za endpoint 
# def create_device(course: schemas.CourseCreate, db: Session = Depends(get_db)):
#     return crud.create_course(db_session=db, course=course)



# @router_devices.get("/{device_id}", response_model=schemas.Device)
# def read_device(device_id: int, db: Session = Depends(get_db)):
#     db_device = crud.get_device(db_session=db, device_id=device_id)
#     if not db_device:
#         raise HTTPException(status_code=404, detail="Device not found.")
#     return db_device

# @router_devices.delete("/{device_id}", response_model=schemas.Device)
# def delete_device(device_id: int, db: Session = Depends(get_db)):
#     db_device = crud.get_device(db_session=db, device_id=device_id)
#     if not db_device:
#         raise HTTPException(status_code=404, detail="Device not found.")
#     db_device = crud.delete_device(db_session=db, device_id=device_id)
#     return db_device

# @router_devices.put("/{device_id}", response_model=schemas.Device)
# def update_device(device_id: int, device_update: schemas.DeviceBase, db: Session = Depends(get_db)):
#     #check if device id exists
#     db_device = crud.get_device(db_session=db, device_id=device_id)
#     if not db_device:
#         raise HTTPException(status_code=404, detail="Device not found.")
#     #check if device name already exists
#     db_device_name = crud.get_device_by_name(db, device_name=device_update.device_name)
#     if db_device_name and not (db_device.device_name == db_device_name.device_name):
#         raise HTTPException(status_code=400, detail="This device name is already used. Select another name.")
#     db_device = crud.put_update_device(db_session=db, db_device=db_device, device_update=device_update)
#     return db_device


# from typing import Any, List

# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session

# from app import crud, models, schemas
# from app.api import deps

# router = APIRouter()


# @router.get("/", response_model=List[schemas.Item])
# def read_items(
#     db: Session = Depends(deps.get_db),
#     skip: int = 0,
#     limit: int = 100,
#     current_user: models.User = Depends(deps.get_current_active_user),
# ) -> Any:
#     """
#     Retrieve items.
#     """
#     if crud.user.is_superuser(current_user):
#         items = crud.item.get_multi(db, skip=skip, limit=limit)
#     else:
#         items = crud.item.get_multi_by_owner(
#             db=db, owner_id=current_user.id, skip=skip, limit=limit
#         )
#     return items


# @router.post("/", response_model=schemas.Item)
# def create_item(
#     *,
#     db: Session = Depends(deps.get_db),
#     item_in: schemas.ItemCreate,
#     current_user: models.User = Depends(deps.get_current_active_user),
# ) -> Any:
#     """
#     Create new item.
#     """
#     item = crud.item.create_with_owner(db=db, obj_in=item_in, owner_id=current_user.id)
#     return item


# @router.put("/{id}", response_model=schemas.Item)
# def update_item(
#     *,
#     db: Session = Depends(deps.get_db),
#     id: int,
#     item_in: schemas.ItemUpdate,
#     current_user: models.User = Depends(deps.get_current_active_user),
# ) -> Any:
#     """
#     Update an item.
#     """
#     item = crud.item.get(db=db, id=id)
#     if not item:
#         raise HTTPException(status_code=404, detail="Item not found")
#     if not crud.user.is_superuser(current_user) and (item.owner_id != current_user.id):
#         raise HTTPException(status_code=400, detail="Not enough permissions")
#     item = crud.item.update(db=db, db_obj=item, obj_in=item_in)
#     return item


# @router.get("/{id}", response_model=schemas.Item)
# def read_item(
#     *,
#     db: Session = Depends(deps.get_db),
#     id: int,
#     current_user: models.User = Depends(deps.get_current_active_user),
# ) -> Any:
#     """
#     Get item by ID.
#     """
#     item = crud.item.get(db=db, id=id)
#     if not item:
#         raise HTTPException(status_code=404, detail="Item not found")
#     if not crud.user.is_superuser(current_user) and (item.owner_id != current_user.id):
#         raise HTTPException(status_code=400, detail="Not enough permissions")
#     return item


# @router.delete("/{id}", response_model=schemas.Item)
# def delete_item(
#     *,
#     db: Session = Depends(deps.get_db),
#     id: int,
#     current_user: models.User = Depends(deps.get_current_active_user),
# ) -> Any:
#     """
#     Delete an item.
#     """
#     item = crud.item.get(db=db, id=id)
#     if not item:
#         raise HTTPException(status_code=404, detail="Item not found")
#     if not crud.user.is_superuser(current_user) and (item.owner_id != current_user.id):
#         raise HTTPException(status_code=400, detail="Not enough permissions")
#     item = crud.item.remove(db=db, id=id)
#     return item