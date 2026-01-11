from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.model.user import User
from app.core.security import hash_password, verify_password 


class UserAlreadyExistsError(Exception):
    pass

class InvalidUserInputError(Exception):
    pass

class UserNotFoundError(Exception):
    pass

class InvalidCredentialsError(Exception):
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

def authenticate_user(db: Session, username: str, password: str) -> User:
    if not isinstance(username, str) or not username.strip():
        raise InvalidUserInputError("Invalid username provided.")   
    if not isinstance(password, str) or not password:
        raise InvalidUserInputError("Invalid password provided.")
    
    user = (db.query(User).filter(User.username == username.strip()).first())

    if not user:
        raise UserNotFoundError("User not found.")
    if not verify_password(password, user.password_hash):
        raise InvalidCredentialsError("Invalid credentials provided.")
    
    return user
