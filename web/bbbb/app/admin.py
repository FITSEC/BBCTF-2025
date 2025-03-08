import asyncio
from pyppeteer import launch
from sys import argv

async def main():
    browser = await launch(args=['--no-sandbox'])
    page = await browser.newPage()
    await page.setCookie({
        'name': 'session',
        'value': argv[1],
        'domain': '127.0.0.1:31337',
        'path': '/',
    },
    {
        'name': 'flag',
        'value': 'bbctf{w0w_7hi5_w45_4_p4in_in_7h3_bbu77}',
        'domain': '127.0.0.1:31337',
        'path': '/',
    })
    cookies = await page.cookies()
    await page.goto('http://127.0.0.1:31337/', {'waitUntil' : 'domcontentloaded'})
    await page.waitFor(2000)
    await browser.close()

asyncio.run(main())
