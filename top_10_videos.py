

import unittest

'''
Assumptions:
1. Videos having same number of views will be ranked as per their index location in the list.
2. Each call to video view will always increase the views of that video by 1.

Approach and problem solution:
1. I have used 2 data structures to keep track of the videos in terms of their views and rankings.
2. A structure will hold information regarding the video and its number of views.
3. A list “videos_list” will maintain all these video structures. This list will be sorted in descending order on number of videos viewed.
    (Descending sort will help us get the top 10  videos easily which will be the first 10 elements in the list)
4. A Dictionary “rankMap(VideoId, ListIndex)” is used to maintain the index of the videos in the list.
    This will help in accessing the videos from the list in O(1). This eventually fetches the rank of the video in O(1).

Time complexity:
getRanking - O(1) - Will be a get operation in Dictionary
videoViewed - O(log n) - Worst case
getTopVideos - O(1) - Will be the first 10 videos in our list (as the list is sorted in descending order on number of views)


'''

rank_map = {} # Dictionary to track rank of video.
videos_list = [] # Sorted list of videos depending on (Ascending) views.

class video_class:
    '''
    Class to hold video object
    '''
    def __init__(self, videoId, views=1):
        self.videoId = videoId
        self.views = views


def binarySearch(theList, value, low, high):
    '''
    Binary search to get location for new insertion of video in videos_list.
    :param theList: videos_list
    :param value: video
    :param low: start of video_list
    :param high: end of video_list
    :return: location in video_list for new insertion depending on the rank of the video.
    '''
    if high <= low:
        return high + 1
    mid = (low + high)/2
    if theList[mid].views < value.views:
        return binarySearch(theList, value, low, mid-1)
    elif theList[mid].views > value.views:
        return binarySearch(theList, value, mid+1, high)
    else:
        return mid + 1


def insert_videos(videos_list, pre_location, video):
    '''
    Gets location from binarySearch to insert new video in videos_list.
    Function maintains stability in terms of relative location will not change.
    :param videos_list: videos_list
    :param pre_location: Previous location of currently viewed video.
    :param video: Video object of currently viewed video.
    :return: None
    '''
    locationToInsert = binarySearch(videos_list, video, 0, len(videos_list)-1)
    videos_list.insert(locationToInsert, video)
    for i in range(locationToInsert+1, pre_location):
        rank_map[videos_list[i]] += 1

def videoViewed(videoId):
    '''
    Increments views of an existing video and repositions it in videos_list, or adds a new video.
    Updates the rank of all the videos in rank_map from previous to new location of the video.
    :param videoId: Id of the Video
    :return: None
    '''
    if rank_map.has_key(videoId):
        videoAt_index = rank_map[videoId]
        video = videos_list[videoAt_index]
        if videoAt_index - 1 >= 0 and videos_list[videoAt_index - 1].views > video.views:
            video.views += 1
        else:
            temp_video = videos_list.pop(videoAt_index)
            insert_videos(videos_list, videoAt_index, temp_video)
    else:
        vObj = video_class(videoId)
        videos_list.append(vObj)
        rank_map['videoId'] = len(videos_list) - 1


def getRanking(videoId):
    '''
    Get index of particular video from the list of videos_list.
    :param videoId: Id of video
    :return: rank of video if found or -1 if not found
    '''
    if rank_map.has_key(videoId):
        return rank_map[videoId] + 1
    else:
        return -1

def getTopVideos():
    '''
    Gets top 10 videos
    :return: List of top 10 videos.
    '''
    if len(videos_list) > 9:
        return videos_list[0:9]
    else:
        return videos_list


