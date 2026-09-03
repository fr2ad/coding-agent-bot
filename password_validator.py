import re

def validate_password(pwd: str) -> bool:
    """
    Validate password strength.
    Returns True if the password has:
    - At least 8 characters
    - At least one uppercase letter
    - At least one number
    - At least one special character
    """
    if not isinstance(pwd, str):
        return False
    
    if len(pwd) < 8:
        return False
    
    if not re.search(r'[A-Z]', pwd):
        return False
        
    if not re.search(r'[0-9]', pwd):
        return False
        
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', pwd):
        return False
        
    return True
