from flask import render_template
from flaskweb import app
from bs4 import BeautifulSoup
import lxml, requests

@app.route('/')
@app.route('/home')
def home():
    eminem_info_list = get_eminem_video_link('https://www.youtube.com/user/EminemVEVO/videos')
    return render_template('index.html', eminem_info_list=eminem_info_list)

def get_eminem_video_link(target_url):
    response = requests.get(target_url)
    soup = BeautifulSoup(response.text, "lxml")
    lis = soup.find_all('li', {'class' : 'channels-content-item yt-shelf-grid-item'})
    eminem_info_list = []
    for li in lis :
        title = li.find('a', {'title' : True})['title']
        video_link = 'https://www.youtube.com' + li.find('a', {'href' : True})['href']
        img_link = li.find('img', {'src' : True})['src']
        play_time = li.find('span', {'class' : 'video-time'}).text
        hits = li.find_all('li')[3].text
        updated_time = li.find_all('li')[3].text
        eminem_video_info = {
            'title' : title,
            'video_link' : video_link,
            'img_link' : img_link,
            'play_time' : play_time,
            'hits' : hits,
            'updated_time' : updated_time
            }
        eminem_info_list.append(eminem_video_info)
    return eminem_info_list