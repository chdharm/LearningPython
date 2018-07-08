# Thanking everyone who wished me on my birthday
import requests
import json

#Aman's post time
AFTER = 1353233754
TOKEN = ' EAACEdEose0cBAASbMlaacylqa9UlowzwPoOSympZC0IGVtkaNQwBYti3A0cQRD5TEF1rrbhs9hv1TNI93jpHLZBoRjfkHL3TO4XZC0n8bMnSk4MSc77hzTsXYtN2HB10xK2freHg88v4nGnIVlMVAr31UW4aoZCtXCZB3AKoaCxRGIZCqRkIjZCDHTvHQQH3l4ZD'


def get_posts():
    """Returns dictionary of id, first names of people who posted on my wall
    between start and end time"""
    query = ("SELECT post_id, actor_id, message FROM stream WHERE "
             "filter_key = 'others' AND source_id = me() AND "
             "created_time > 1353233754 LIMIT 200")

    payload = {'q': query, 'access_token': TOKEN}
    r = requests.get('https://graph.facebook.com/fql', params=payload)
    print "response:",r
    result = json.loads(r.text)
    return result['data']


def commentall(wallposts):
    """Comments thank you on all posts"""
    # TODO convert to batch request later
    for wallpost in wallposts:
        r = requests.get('https://graph.facebook.com/%s' %
                         wallpost['actor_id'])
        url = 'https://graph.facebook.com/%s/comments' % wallpost['post_id']
        user = json.loads(r.text)
        message = 'Thanks %s :)' % user['first_name']
        payload = {'access_token': TOKEN, 'message': message}
        s = requests.post(url, data=payload)

        print "Wall post %s done" % wallpost['post_id']


if __name__ == '__main__':
    commentall(get_posts())