# The Telescope API
#
# Copyright 2022 Telescope Inc. All rights reserved.
#
# Sharing of any piece of code to any unauthorized third-party is not allowed.
from fastapi import Header

from capture.database import User, verify_token


async def get_user(authorization: str | None = Header(None)) -> User | None:
    if authorization is None:
        return None

    return await verify_token(token=authorization)