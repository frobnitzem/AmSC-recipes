# based on https://github.com/doe-iri/iri-facility-api-python

import asyncio
import json

import aiohttp

async def main(argv):
    assert len(argv) == 2, f"Usage: {argv[0]} <base url>"
    base_url = argv[1]
    headers = {"accept": "application/json"}

    async with aiohttp.ClientSession(base_url, headers=headers) as session:
        async with session.get('/api/v1/status/resources') as resp:
            if resp.status//100 == 2:
                print(f"Status for {base_url}")
            else:
                print(f"Status for {base_url} returned {resp.status}")
                return
            ans = await resp.json()
            print(json.dumps(ans, indent=2))

if __name__=="__main__":
    import sys
    asyncio.run( main(sys.argv) )
