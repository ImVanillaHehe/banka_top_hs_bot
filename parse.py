import aiohttp
import asyncio
import json

data_player = []
tier = set(["VanillaHehe", "GIGI", "thezevz", "mM1307", "RANDOM", "HATEmm1307"])
headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0;Win64;x64) AppleWebKit/537.36(KHTML, likeGecko)"
                      " Chrome/105.0.0.0 Safari/537.36",
        "accept": "*/*"}


async def fetch_data(session, page):
    url = f"https://hearthstone.blizzard.com/ru-ru/api/community/leaderboardsData?region=EU&leaderboardId=battlegrou" \
          f"nds&page={page}&seasonId=8"
    async with session.get(url=url, headers=headers, ssl=False) as response:
        data = await response.json()
        items = data["leaderboard"]["rows"]

        for item in items:
            account_name = item["accountid"]
            rating = item["rating"]
            rank = item["rank"]
            if account_name in tier:
                data_player.append(
                {
                "account_name": account_name,
                "rating": rating,
                "rank": rank,
                })


async def mainstream(start, end):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_data(session, page) for page in range(start, end)]
        await asyncio.gather(*tasks)

        with open(f"banka player_list.json", "w") as file:
            json.dump(data_player, file, indent=4, ensure_ascii=False)
        print("Файл перезаписан")
        data_player.clear()



