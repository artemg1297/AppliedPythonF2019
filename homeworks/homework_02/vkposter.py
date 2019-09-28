#!/usr/bin/env python
# coding: utf-8


class VKPoster:

    def __init__(self):
        self.posted = {}
        self.seen = {}
        self.subs = {}
        self.posts = {}

    def user_posted_post(self, user_id: int, post_id: int):
        if user_id not in self.posted:
            self.posted[user_id] = [post_id]
        else:
            self.posted[user_id].append(post_id)

    def user_read_post(self, user_id: int, post_id: int):
        if post_id not in self.seen:
            self.seen[post_id] = [user_id]
        else:
            if user_id not in self.seen[post_id]:
                self.seen[post_id].append(user_id)

    def user_follow_for(self, follower_user_id: int, followee_user_id: int):
        #if follower_user_id != followee_user_id:
            if follower_user_id not in self.subs:
                self.subs[follower_user_id] = [followee_user_id]
            else:
                if followee_user_id not in self.subs[follower_user_id]:
                    self.subs[follower_user_id].append(followee_user_id)

    def get_recent_posts(self, user_id: int, k: int)-> list:
                lis = []
                if user_id not in self.subs.keys():
                    return
                for j in self.subs[user_id]:
                    lis = lis + (self.posted[j])
                lis = sorted(lis)
                lis.reverse()
                return lis[:k]

    def get_most_popular_posts(self, k: int) -> list:
        lis = []
        for key in self.seen.keys():
            self.posts[key] = len(self.seen[key])
            lis.append(self.posts[key])
        lis = sorted(lis)
        lis = lis[::-1]
        res = []
        res2 = []
        i = 1
        j = 0
        while i <= k:
            for key in self.posts.keys():
                if (self.posts[key] == lis[j]) and key not in res2:
                    res2.append(key)
            if j < len(lis) - 1:
                j += 1
            else:
                break
            if (lis[j] != lis[j - 1]) or (j == len(lis) - 1):
                res2 = sorted(res2)
                res += res2[::-1]
                res2 = []
            i += 1
        return res
