"""MailerLite tap class."""

from typing import List

from singer_sdk import Tap, Stream
from singer_sdk import typing as th  # JSON schema typing helpers
# TODO: Import your custom stream types here:
from tap_mailerlite.streams import (
    MailerLiteStream,
    SubscribersStream,
    GroupsStream,
    CampaignsStream
)

# TODO: Compile a list of custom stream types here
#       OR rewrite discover_streams() below with your custom logic.
STREAM_TYPES = [
    SubscribersStream,
    GroupsStream,
    CampaignsStream
]


class TapMailerLite(Tap):
    """MailerLite tap class."""
    name = "tap-mailerlite"

    config_jsonschema = th.PropertiesList(
        th.Property( # the old api-docuemntation uses api-key, while the new one uses token bearer
            "auth_token",
            th.StringType,
            required=True,
            description="The token to authenticate against the API service"
        ),
        th.Property(
            "start_date",
            th.DateTimeType,
            description="The earliest record date to sync"
        ),
        th.Property(
            "api_url",
            th.StringType,
            default="https://connect.mailerlite.com/api"
        ),
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]
