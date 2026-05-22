def format_message(message: str) -> str:
    """Format message for processing"""
    return message.strip().lower()

def validate_user_id(user_id: str) -> bool:
    """Validate user ID format"""
    return bool(user_id and len(user_id) > 0)

def truncate_text(text: str, max_length: int = 1000) -> str:
    """Truncate text to maximum length"""
    if len(text) > max_length:
        return text[:max_length] + "..."
    return text

def is_valid_json(data: dict) -> bool:
    """Check if data is valid JSON-serializable"""
    try:
        import json
        json.dumps(data)
        return True
    except (TypeError, ValueError):
        return False
