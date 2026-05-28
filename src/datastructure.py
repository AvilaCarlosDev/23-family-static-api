"""
Family Static API - Data Structures
FamilyStructure class to manage family tree data
"""

class FamilyMember:
    """Represents a member of the Jackson family"""
    
    def __init__(self, id, first_name, age, lucky_numbers=None):
        self.id = id
        self.first_name = first_name
        self.age = age
        self.lucky_numbers = lucky_numbers or []
    
    def serialize(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "age": self.age,
            "lucky_numbers": self.lucky_numbers
        }


class FamilyStructure:
    """
    Manages the Jackson family data structure
    - Stores all family members
    - Generates unique IDs for new members
    """
    
    def __init__(self, last_name):
        self.last_name = last_name
        self._members = []
        self._next_id = 1
        
        # Initialize with the Jackson family members
        self._initialize_family()
    
    def _initialize_family(self):
        """Initialize with default Jackson family members"""
        john = FamilyMember(
            id=1,
            first_name="John",
            age=33,
            lucky_numbers=[7, 13, 22]
        )
        jane = FamilyMember(
            id=2,
            first_name="Jane",
            age=35,
            lucky_numbers=[10, 14, 3]
        )
        jimmy = FamilyMember(
            id=3,
            first_name="Jimmy",
            age=5,
            lucky_numbers=[1]
        )
        self._members = [john, jane, jimmy]
        self._next_id = 4
    
    def _generate_id(self):
        """Generate a unique ID for a new member"""
        new_id = self._next_id
        self._next_id += 1
        return new_id
    
    def add_member(self, member_dict):
        """Add a new member to the family"""
        if "id" not in member_dict or member_dict["id"] is None:
            member_dict["id"] = self._generate_id()
        
        member = FamilyMember(
            id=member_dict["id"],
            first_name=member_dict["first_name"],
            age=member_dict.get("age", 0),
            lucky_numbers=member_dict.get("lucky_numbers", [])
        )
        self._members.append(member)
        return member.serialize()
    
    def delete_member(self, id):
        """Delete a member from the family by ID"""
        for i, member in enumerate(self._members):
            if member.id == id:
                self._members.pop(i)
                return True
        return False
    
    def get_member(self, id):
        """Get a specific member by ID"""
        for member in self._members:
            if member.id == id:
                return member.serialize()
        return None
    
    def get_all_members(self):
        """Get all family members"""
        return [member.serialize() for member in self._members]
