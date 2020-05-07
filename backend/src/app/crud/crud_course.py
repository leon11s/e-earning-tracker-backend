# # # # ------------------ Device-----------------------
# def post_create_device(db_session: Session, device: schemas.DeviceCreate):
#     db_device = models.DeviceDB(owner_id=device.owner_id, 
#                                 device_name=device.device_name,
#                                 description=device.description
#                                 )
#     db_session.add(db_device)
#     db_session.commit()
#     db_session.refresh(db_device)
#     return db_device





# def get_devices(db_session: Session, skip: int = 0, limit: int = 100):
#     return db_session.query(models.DeviceDB).offset(skip).limit(limit).all()

# def delete_device(db_session: Session, device_id: int):
#     device_db = db_session.query(models.DeviceDB).filter(models.DeviceDB.device_id == device_id).first()
#     db_session.delete(device_db)
#     db_session.commit()
#     return device_db

# def put_update_device(db_session: Session, db_device: schemas.Device, device_update: schemas.DeviceBase):
#     db_device.device_name = device_update.device_name
#     db_device.description = device_update.description
#     db_session.commit()
#     return db_device