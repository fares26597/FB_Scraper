import sqlite3

#function for creating table for posts
def create_posts():
    connexion = sqlite3.connect('fb.db')
    cur = connexion.cursor()
    create_posts_table='''CREATE TABLE IF NOT EXISTS fbposts(
                                post_id TEXT, 
                                txt TEXT, 
                                time TEXT, 
                                likes INT, 
                                commentsnbr INT, 
                                shares INT, 
                                url TEXT PRIMARY KEY);'''
    cur.execute(create_posts_table)
    connexion.commit()
    connexion.close()
    print('Posts Table Created')

#function for creating table for comments. 
# Each comment is linked to its respective post with post_id
def create_comnts():
    connexion = sqlite3.connect('fb.db')
    cursor1 = connexion.cursor()
    create_comments_table='''CREATE TABLE IF NOT EXISTS comnts(
                            post_id TEXT REFERENCES fbposts(post_id), 
                            comment_id TEXT,
                            comment_url TEXT PRIMARY KEY,
                            commenter_name TEXT, 
                            comment_text TEXT, 
                            comment_time TEXT);'''
    cursor1.execute(create_comments_table)
    connexion.commit()
    connexion.close()
    print('Comments table created')

#function for inserting posts into posts table
def insert_post(post: dict):
    post_id = post["post_id"]
    txt = post["post_text"]
    time = str(post["time"])
    likes = post["likes"]
    commentsnbr = post["comments"]
    shares = post["shares"]
    url = post["post_url"]
    connexion = sqlite3.connect('fb.db')
    cursor = connexion.cursor()
    insert_post=''' INSERT INTO fbposts
    (post_id , txt, time, likes, commentsnbr, shares, url)
    values (?,?,?,?,?,?,?)'''
    cursor.execute(insert_post,(post_id , txt, time, likes, commentsnbr, shares, url))
    connexion.commit()
    connexion.close()

#function for inserting comments into comments table
def insert_comnts(post: dict):
    for c in post["comments_full"]:
            post_id=post["post_id"]
            comment_id=str(c["comment_id"])
            commenter_name=str(c["commenter_name"])
            comment_url=str(c["comment_url"])
            comment_text=str(c["comment_text"])
            comment_time=str(c["comment_time"])
            
            connexion = sqlite3.connect('fb.db')
            cursor = connexion.cursor()
            insert_comnt=''' INSERT INTO comnts 
            (post_id, comment_id, comment_url, commenter_name , comment_text, comment_time) 
            values (?,?,?,?,?,?)'''
            cursor.execute(insert_comnt,(post_id, comment_id, comment_url, commenter_name , comment_text, comment_time))
            connexion.commit()
            connexion.close()

#function for deleting all rows
def dlt_rows():
    connexion = sqlite3.connect('fb.db')
    cursor = connexion.cursor()
    cursor.execute('DELETE FROM fbposts; ',);
    connexion.commit()
    connexion.close()

    connexion = sqlite3.connect('fb.db')
    cursor = connexion.cursor()
    cursor.execute('DELETE FROM comnts; ',);
    connexion.commit()
    connexion.close()

#function for deleting all tables 
def drop_table():
    conn = sqlite3.connect('fb.db')
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS fbposts")
    conn.commit()
    conn.close()

    conn = sqlite3.connect('fb.db')
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS comnts")
    conn.commit()
    conn.close()