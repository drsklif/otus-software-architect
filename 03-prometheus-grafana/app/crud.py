from sqlalchemy.orm import Session

import models


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def create_user(db: Session, user: models.User):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def delete_user(db: Session, user_id: int):
    db_user = get_user(db, user_id)
    if db_user is None:
        return None
    db.delete(db_user)
    db.commit()
    return db_user


def update_user(db: Session, user: models.User):
    db_user = get_user(db, user.id)
    if db_user is None:
        return None
    db_user.username=user.username
    db_user.firstname=user.firstname
    db_user.lastname=user.lastname
    db_user.email=user.email
    db_user.phone=user.phone
    db.commit()
    return db_user
