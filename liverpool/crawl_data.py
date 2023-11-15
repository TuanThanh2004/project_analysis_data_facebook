from facebook_scraper import get_posts
import pandas as pd
import numpy as np

FANPAGE_LINK ="LiverpoolFC"
FOLDER_PATH = "C:/Users/Admin/aim/crawl_data_facebook/liverpool/"
COOKIE_PATH = "C:/Users/Admin/aim/crawl_data_facebook/liverpool/www.facebook.com_cookies.txt"

PAGES_NUMBER = 1 # Number of pages to crawl

post_list = []
for post in get_posts(FANPAGE_LINK,
                    options={"comments": True, "reactions": True, "allow_extra_requests": True},
                    extra_info=True, pages=PAGES_NUMBER, cookies=COOKIE_PATH):
    print(post)
    post_list.append(post)
    # Initialize dataframe to scrape Facebook post
post_df_full = pd.DataFrame(columns=post_list[0].keys(), index=range(len(post_list)), data=post_list)


# To df
path=FOLDER_PATH + FANPAGE_LINK + ".csv"
post_df_full.to_csv(path, index=False)
print(path)

