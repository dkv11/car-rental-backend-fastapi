from app.core.security import hash_password, verify_password

password = "TestPassword123!"
hashed = hash_password(password)

print("Hashed:", hashed)
print("Verify correct:", verify_password(password, hashed))
print("Verify wrong:", verify_password("WrongPass", hashed))