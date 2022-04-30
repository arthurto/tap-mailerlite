"""Stream type classes for tap-mailerlite."""

from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_mailerlite.client import MailerLiteStream

# Based on new-api documentation
# https://mailerlite.github.io/reference

class SubscribersStream(MailerLiteStream):
    """Define custom stream."""
    name = "subscribers"
    path = "/subscribers"
    primary_keys = ["id"]
    replication_key = None
    # Optionally, you may also use `schema_filepath` in place of `schema`:
    # schema_filepath = SCHEMAS_DIR / "users.json"
    schema = th.PropertiesList(
        th.Property("id",th.StringType),
        th.Property("email",th.StringType),
        th.Property("status",th.StringType),
        th.Property("source",th.StringType),
        th.Property("sent",th.IntegerType),
        th.Property("opens_count",th.IntegerType),
        th.Property("click_count",th.IntegerType),
        th.Property("open_rate",th.IntegerType),
        th.Property("ip_address",th.StringType),
        th.Property("subscribed_at",th.DateTimeType),
        th.Property("unsubscribed_at",th.DateTimeType),
        th.Property("created_at",th.DateTimeType),
        th.Property("updated_at",th.DateTimeType),
        th.Property("fields",
                    th.PropertiesList(
                        th.Property("name",th.StringType),
                        th.Property("last_name",th.StringType),
                        th.Property("company",th.StringType),
                        th.Property("country",th.StringType),
                        th.Property("city",th.StringType),
                        th.Property("phone",th.StringType),
                        th.Property("state",th.StringType),
                        th.Property("z_i_p",th.StringType)
                    )),
        th.Property("opted_in_at",th.StringType),
        th.Property("opted_ip",th.StringType)
    ).to_dict()


class GroupsStream(MailerLiteStream):
    """Define Groups Stream."""
    name = "groups"
    path = "/groups"
    primary_keys = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("name", th.StringType),
        th.Property("active_count", th.IntegerType),
        th.Property("sent_count", th.IntegerType),
        th.Property("opens_count", th.IntegerType),
        th.Property("open_rate",
                    th.PropertiesList(
                        th.Property("float",th.IntegerType),
                        th.Property("string",th.StringType)    
                    )),
        th.Property("clicks_count",th.IntegerType),
        th.Property("click_rate",
                    th.PropertiesList(
                        th.Property("float",th.IntegerType),
                        th.Property("string",th.StringType)    
                    )),
        th.Property("unsubscribed_count",th.IntegerType),
        th.Property("unconfirmed_count",th.IntegerType),
        th.Property("bounced_count",th.IntegerType),
        th.Property("junk_count",th.IntegerType),
        th.Property("created_at",th.DateTimeType)
    ).to_dict()

# It seems that the new api-documentation :
# https://mailerlite.github.io/reference
# is being updated just now, last update dates
# 29/04/2022 (yesterday) 10:57:33
# and this might be the reason the campaigns stream 
# is not working properly (not getting any data)
# even thoug it passes the tests.  

class CampaignsStream(MailerLiteStream):
    """Define Campaigns Stream"""
    name = "campaigns"
    path = "/campaigns"
    primary_keys = ["id"]
    replication_key = None 
    schema = th.PropertiesList( # based on old-api documentation
        th.Property("id",th.IntegerType),
        th.Property("total_recipients",th.IntegerType),
        th.Property("type",th.StringType),
        th.Property("date_created",th.StringType),
        th.Property("date_send",th.StringType),
        th.Property("name",th.StringType),
        th.Property("subject",th.StringType),
        th.Property("status",th.StringType),
        th.Property("opened",th.PropertiesList(
            th.Property("count",th.IntegerType),
            th.Property("rate",th.NumberType)
        )),
        th.Property("clicked",th.PropertiesList(
            th.Property("count",th.IntegerType),
            th.Property("rate",th.NumberType)
        )),
    ).to_dict()