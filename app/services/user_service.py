from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.model.user import User
from app.core.security import hash_password


class UserAlreadyExistsError(Exception):
    pass

class InvalidUserInputError(Exception):
    pass

def register_user(db: Session, username: str, password: str) -> User:

    if not isinstance(username, str) or not username.strip():
        raise InvalidUserInputError("Invalid username provided.")
    
    if not isinstance(password, str) or len(password) < 8:
        raise InvalidUserInputError("Password must be at least 8 characters long.")
    
    if len(password.encode('utf-8')) > 72:
        raise InvalidUserInputError("Password is too long.")
    
    
    hashed_password = hash_password(password)

    user = User(username=username.strip(), password_hash=password_hash)

    db.add(user)
    try:        
        db.commit()
        db.refresh(user)
        
    except IntegrityError:
        db.rollback()
        raise UserAlreadyExistsError(f"User with username '{username}' already exists.")
    
    return user