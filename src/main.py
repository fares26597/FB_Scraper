import scraper
import sql_mng
from fastapi import FastAPI
from uvicorn import run
from databases import Database


database = Database("sqlite:///fb.db")
app = FastAPI()

@app.get("/")
async def get_data():
    page=input("page name (e.g. Marvel): ") #no constraints unfortunately
    nb=int(input("Number of scrolls: "))
    tb=" "
    t=" "
    while tb!="posts" and tb!="comments": #choosing whether to recieve posts table or comments table
        tb=input("posts or comments? ")
        if tb=="posts":
            t="fbposts"
        else:
            t="comnts"
    sql_mng.drop_table() #refreshing the tables with empty columns
    sql_mng.create_posts()
    sql_mng.create_comnts()

    scraper.scraper(page,nb) #scraping

    query = "SELECT * FROM "+t
    results = await database.fetch_all(query=query) #sending tables to output

    return results

if __name__ == "__main__":
    run(app, host="0.0.0.0", port=8000)