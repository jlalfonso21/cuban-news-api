import json
import feedparser


def get_posts_details(url=None):
    if url is not None:
        blog_feed = blog_feed = feedparser.parse(url)
        posts = blog_feed.entries

        post_list = []

        # iterating over individual posts
        for post in posts:
            temp = dict()

            # if any post doesn't have information then throw error.
            try:
                temp["title"] = post.title
                temp["link"] = post.link
                temp["author"] = post.author
                temp["time_published"] = post.published
                temp["tags"] = [tag.term for tag in post.tags]
                temp["authors"] = [author.name for author in post.authors]
                temp["summary"] = post.summary
            except:
                pass

            post_list.append(temp)

        return post_list
    else:
        return None
