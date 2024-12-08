from dataclasses import dataclass
from typing import Optional

from dataclasses_json import dataclass_json
from typing_extensions import NotRequired, TypedDict


@dataclass_json
@dataclass
class RoomResource:
    """
    Class representation of a Nylas Room Resource object.

    Attributes:
        building: The name of the building where the room is located.
        capacity: The number of people the room can seat.
        email: The email address associated with the room resource.
        floor_name: The name of the floor where the room is located.
        floor_number: The floor number where the room is located.
        floor_section: The section of the floor where the room is located.
        object: The object type (always "room_resource").
    """

    email: str
    object: str
    building: Optional[str] = None
    capacity: Optional[int] = None
    floor_name: Optional[str] = None
    floor_number: Optional[int] = None
    floor_section: Optional[str] = None


class ListRoomResourcesQueryParams(TypedDict):
    """
    Interface representing the query parameters for listing room resources.

    Attributes:
        limit: The maximum number of objects to return.
            This field defaults to 10. The maximum allowed value is 200.
        page_token: Token to retrieve the next page of results.
    """

    limit: NotRequired[int]
    page_token: NotRequired[str]
