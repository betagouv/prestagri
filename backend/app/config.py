import os
from .services.properties import properties
import sentry_sdk

def setup_sentry():

    sentry_sdk.init(
        dsn=properties.sentry_dsn,
        environment="staging",
        # Add data like request headers and IP for users,
        # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
        send_default_pii=True,
        enable_logs=True,
    )