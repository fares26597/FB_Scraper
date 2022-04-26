from facebook_scraper import get_posts
import sql_mng

#scraping function.
#sends warning when nb of pages (nb of scrolls) is less than 3. we can ignore it.
def scraper(page: str, pagenb: int):
    posts_list = []
    for post in get_posts(page, pages=pagenb, cookies="facebook.com_cookies.txt", options={"comments":True}):
        posts_list.append(post)
        sql_mng.insert_post(post)
        sql_mng.insert_comnts(post)