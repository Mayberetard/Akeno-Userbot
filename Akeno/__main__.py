#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2020-2023 (c) Randy W @xtdevs, @xtsea
#
# from : https://github.com/TeamKillerX
# Channel : @RendyProjects
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import asyncio
import logging
import sys
import importlib
import aiohttp
from pyrogram import idle

from Akeno import clients
from Akeno.core.logger import LOGS
from pyrogram.errors import *
from contextlib import closing, suppress
from uvloop import install

logging.basicConfig(level=logging.INFO)
logging.getLogger("pyrogram.syncer").setLevel(logging.WARNING)
logging.getLogger("pyrogram.client").setLevel(logging.WARNING)
loop = asyncio.get_event_loop()

async def main():
    try:
        for cli in clients:
            try:
                await cli.start()
                ex = await cli.get_me()
                LOGS.info(f"Started {ex.first_name}")
                await cli.send_message("me", "Starting Userbot")
            except Exception as e:
                LOGS.error(f"Error starting userbot: {e}")
        await idle()
    except Exception as e:
        LOGS.error(f"Error in main: {e}")
    finally:
        await asyncio.gather(
            aiohttpsession.close()
        )

        for task in asyncio.all_tasks():
            task.cancel()

        LOGS.info("All tasks completed successfully!")

if __name__ == "__main__":
    install()
    with closing(loop):
        with suppress(asyncio.exceptions.CancelledError):
            loop.run_until_complete(main())
        loop.run_until_complete(asyncio.sleep(3.0))