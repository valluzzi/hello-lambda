import json
import asyncio
import httpx

async def fetch_data(url):
    async with httpx.AsyncClient() as client:
        print(f"Fetching {url}...")
        response = await client.get(url)
        return response.text

async def downloads():
    response ={}
    urls = [
        "https://s3.amazonaws.com/saferplaces.co/lidar-rer-100m.tif",
        "https://s3.amazonaws.com/saferplaces.co/lidar-rer-100m(1).tif",
    ]

    tasks = [fetch_data(url) for url in urls]
    results = await asyncio.gather(*tasks)


    for url, result in zip(urls, results):
        response[url] = len(result)

    return response




def main_lambda(event):
    """
    main loop
    """
    
    response = asyncio.run(downloads())

    name = event["name"]

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "text/plain"
        },
        "body": json.dumps(response)
    }


def lambda_handler(event, context):
    """
    AWS Lambda handler
    """
    return main_lambda(event)


if __name__ == "__main__":
    """
    Local test
    """
    event = {
        "name": "world"
    }
    print(main_lambda(event))