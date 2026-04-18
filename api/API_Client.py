import googleapiclient.discovery
from config import YOUTUBE_API_KEY

youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)