from services import random_date, get_random_role_id

import sys
sys.path = ['','..'] + sys.path[1:]

from db.base import Session
from db.models import User, Role



def save_worker(fio):
    role_id = get_random_role_id()
    r_date = random_date()
    with Session() as session:
        worker = User(
            fio=fio,
            datar=r_date,
            id_role=role_id
        )
        session.add(worker)
        session.commit()
