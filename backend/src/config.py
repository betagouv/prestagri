import os
import sentry_sdk

SENTRY_DSN = os.environ['SENTRY_DSN']

def setup_sentry():
    sentry_sdk.init(
        dsn=SENTRY_DSN,
        environment="staging",
        # Add data like request headers and IP for users,
        # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
        send_default_pii=True,
        enable_logs=True,
    )