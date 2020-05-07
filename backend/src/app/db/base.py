# Import all the models, so that Base has them before being
# imported by Alembic

from app.db.base_class import Base
from app.models.user import User

# Tukaj uvozimo vse naše modele
# from app.models.courses import Course 