from typing import List, Dict, Optional
from app.models.schemas import Message

class ConversationMemory:
    """In-memory conversation storage"""
    
    def __init__(self):
        self.conversations: Dict[str, List[Message]] = {}
    
    def add_message(self, user_id: str, role: str, content: str) -> None:
        """Add a message to the conversation history"""
        if user_id not in self.conversations:
            self.conversations[user_id] = []
        
        message = Message(role=role, content=content)
        self.conversations[user_id].append(message)
    
    def get_history(self, user_id: str, limit: Optional[int] = None) -> List[Dict]:
        """Get conversation history for a user"""
        if user_id not in self.conversations:
            return []
        
        history = self.conversations[user_id]
        if limit:
            history = history[-limit:]
        
        return [{"role": msg.role, "content": msg.content} for msg in history]
    
    def clear_history(self, user_id: str) -> None:
        """Clear conversation history for a user"""
        if user_id in self.conversations:
            self.conversations[user_id] = []
    
    def get_all_users(self) -> List[str]:
        """Get all users with conversation history"""
        return list(self.conversations.keys())
