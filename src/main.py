"""Module defines the main entry point for the Apify Actor.

Feel free to modify this file to suit your specific needs.

To build Apify Actors, utilize the Apify SDK toolkit, read more at the official documentation:
https://docs.apify.com/sdk/python
"""

from __future__ import annotations

import datetime
import os
import traceback

# Beautiful Soup - A library for pulling data out of HTML and XML files. Read more at:
# https://www.crummy.com/software/BeautifulSoup/bs4/doc
# Apify SDK - A toolkit for building Apify Actors. Read more at:
# https://docs.apify.com/sdk/python
from apify import Actor
from basecommons.scrapers.producthunt_nodriver_scraper import ProductHuntNodriverScraper
from basecommons.utils import time_utils


# HTTPX - A library for making asynchronous HTTP requests in Python. Read more at:
# https://www.python-httpx.org/

async def main() -> None:
    """Define a main entry point for the Apify Actor.

    This coroutine is executed using `asyncio.run()`, so it must remain an asynchronous function for proper execution.
    Asynchronous execution is required for communication with Apify platform, and it also enhances performance in
    the field of web scraping significantly.
    """
    async with Actor:
        # Retrieve the input object for the Actor. The structure of input is defined in input_schema.json.
        actor_input = await Actor.get_input() or {}
        cycle = actor_input.get("cycle", "day")
        date = actor_input.get("date", "2025-11-05")
        week = actor_input.get("week", 1)
        limit = actor_input.get("limit", 10)

        max_paid_items = os.getenv("ACTOR_MAX_PAID_DATASET_ITEMS", 0) or 2000
        max_paid_items = int(max_paid_items)
        if max_paid_items and limit > max_paid_items:
            limit = max_paid_items
            Actor.log.warning(f"limit > actor_max_paid_dataset_items, max_items: {max_paid_items}, limit: {limit}, final use: {limit}")

        Actor.log.info(f'Launching Product Hunt Scraper Actor, actor_max_paid_dataset_items: {max_paid_items}, input: {actor_input}')

        year, month, day = date.split("-")
        date = datetime.date(int(year), int(month), int(day))

        key_value_store = await Actor.open_key_value_store(name="producthunt-config")
        product_hunt_config = await key_value_store.get_value("producthunt-headers.json")
        if not product_hunt_config:
            Actor.log.error("config not found in key-value store")
            return

        results = []
        try:
            product_hunt_scraper = ProductHuntNodriverScraper(
                logger=Actor.log,
                leaderboard_daily_page_sha256_hash=product_hunt_config.get("leaderboard_daily_page_sha256_hash"),
                leaderboard_weekly_page_sha256_hash=product_hunt_config.get("leaderboard_weekly_page_sha256_hash"),
                leaderboard_monthly_page_sha256_hash=product_hunt_config.get("leaderboard_monthly_page_sha256_hash"),
                leaderboard_yearly_page_sha256_hash=product_hunt_config.get("leaderboard_yearly_page_sha256_hash"),
                products_page_layout_sha256_hash=product_hunt_config.get("products_page_layout_sha256_hash"),
                post_page_comments_sha256_hash=product_hunt_config.get("post_page_comments_sha256_hash"),
                product_about_page_sha256_hash=product_hunt_config.get("product_about_page_sha256_hash"),
                product_page_launching_today_sha256_hash=product_hunt_config.get("product_page_launching_today_sha256_hash"),
            )
            await product_hunt_scraper.init()
            results = await product_hunt_scraper.get_apps(cycle=cycle, date=date, week=week, limit=limit)
        except Exception as e:
            trace_log = traceback.format_exc()
            producthunt_actor_errors = await Actor.open_dataset(name="producthunt-actor-errors")
            await producthunt_actor_errors.push_data({
                "create_time": time_utils.format_datetime(datetime.datetime.now()),
                "cycle": cycle,
                "date": time_utils.format_datetime(date),
                "week": week,
                "limit": limit,
                "trace": trace_log,
            })

            Actor.log.error(f"get product hunt app error, trace: {trace_log}")

        await Actor.push_data(results)
        Actor.log.info(f"get product hunt app success, count: {len(results)}")
