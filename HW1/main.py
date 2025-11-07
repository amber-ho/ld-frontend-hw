import asyncio
from aiohttp import ClientSession

URL1 = "https://example.com"
URL2 = "https://github.com/NTUEELightDance/LightDance-Editor/releases/latest/download/editor-blender.zip"

async def main():
    session = ClientSession()
    
    ## TODO start

    ## end

    await session.close()

if __name__ == "__main__":
    asyncio.run(main())