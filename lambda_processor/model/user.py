from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class User:
    user_id: int
    name: str
    password: str
    email: str
    phone: str
    crate_time: str
    update_time: str
