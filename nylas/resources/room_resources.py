from nylas.config import RequestOverrides
from nylas.handler.api_resources import ListableApiResource
from nylas.models.response import ListResponse
from nylas.models.room_resources import ListRoomResourcesQueryParams, RoomResource


class RoomResources(ListableApiResource):
    """
    Nylas Room Resources API

    The Room Resources API allows you to list room resources available on your Nylas account.
    """

    def list(
        self,
        identifier: str,
        query_params: ListRoomResourcesQueryParams = None,
        overrides: RequestOverrides = None,
    ) -> ListResponse[RoomResource]:
        """
        Return all Room Resources.

        Args:
            identifier: The identifier of the Grant to act upon.
            query_params: The query parameters to include in the request.
            overrides: The request overrides to use for the request.

        Returns:
            The list of Room Resources.
        """
        return super().list(
            path=f"/v3/grants/{identifier}/resources",
            response_type=RoomResource,
            query_params=query_params,
            overrides=overrides,
        )
