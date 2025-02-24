import asyncio
import time
import aiofiles

async def file_read():
    async with aiofiles.open("C:/Users/karthikeyan.muniraj/Documents/asyncio_doc.txt", 'r') as f:
        content = await f.read()
        await asyncio.sleep(3)
        return "read complete"

async def file_write():
    async with aiofiles.open("C:/Users/karthikeyan.muniraj/Documents/async_doc_write.txt", 'w') as f:
        await f.write(" hi this is one")
        await asyncio.sleep(2)
        print("Written into the file")
        return "Write complete"

async def main():
    start1 = time.time()
    batch =await asyncio.gather(file_read(), file_write())
    res_file_read, res_file_write = batch
    end1 = time.time()
    time_elapsed = end1 - start1

    print(f"File Read Result: {res_file_read}")
    print(f"File Write Result: {res_file_write}")
    print(f"Time elapsed: {time_elapsed:.2f} seconds")

asyncio.run(main())
