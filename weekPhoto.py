from ast import arg
import pyppeteer
import asyncio
import os
import sys
import json

args = sys.argv

if len(args) < 2:
    print("Not enough arguments")
    exit(1)

async def main():
    weekSelector = f"#app > div > div.container-fluid.results-container.px-5 > div.row.bg-white.rounded.my-2.footer > div > nav > ul > li:nth-child({int(args[1]) + 1}) > a"
    cookiesSelector = "#QXZpc28hRXN0YSUyMHdlYiUyMHV0aWxpemElMjBjb29raWVzJTIwcGFyYSUyMG1lam9yYXIlMjBsYSUyMGV4cGVyaWVuY2lhJTIwZGUlMjB1c3VhcmlvYmx1ZQ > div.iziToast-body > div.iziToast-buttons > button"

    print(weekSelector)
    browser = await pyppeteer.launch(
        headless=True,
        args=['--no-sandbox', '--disable-setuid-sandbox', '--window-size=1920,1080']
    )
    page = await browser.newPage()
    await page.setViewport({'width': 1920, 'height': 1080})
    await page.goto("https://quinielaluislopez.com/quinielas/")
    await page.waitForSelector(weekSelector)
    await page.click(weekSelector)
    await page.waitForSelector(cookiesSelector)
    await page.click(cookiesSelector)
    await page.waitFor(5000)
    tableSelector = '#app > div > div.container-fluid.results-container.px-5 > div.row.table-responsive.bg-white.rounded.shadow-sm'
    table = await page.querySelector(tableSelector)
    # remove maxheight
    await page.evaluate('''(table) => table.style.maxHeight = "none"''', table)
    await table.screenshot({'path': f'./bkups/week{args[1]}.png', 'fullPage': True})

asyncio.get_event_loop().run_until_complete(main())