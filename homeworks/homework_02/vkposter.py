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
        if follower_user_id != followee_user_id:
            if follower_user_id not in self.subs:
                self.subs[follower_user_id] = [followee_user_id]
            else:
                if followee_user_id not in self.subs[follower_user_id]:
                    self.subs[follower_user_id].append(followee_user_id)

    def get_recent_posts(self, user_id: int, k: int)-> list:
        lis = []
        if user_id not in self.subs.keys():
            return
        for j in range(len(self.subs[user_id])):
            user = self.subs[user_id][j]
            if user in self.posted:
                lis = lis + self.posted[user]
        lis = sorted(lis)
        lis.reverse()
        return lis[:k]

    def get_most_popular_posts(self, k: int) -> list:
            lis = []
            self.posts = {}
            for key in self.seen.keys():
                self.posts[key] = len(self.seen[key])
                lis.append(self.posts[key])
            print(self.posts)
            lis = []
            for key in self.posts.keys():
                lis.append(self.posts[key])
            lis = sorted(lis)[::-1]
            lis = lis[:k] + [-1]
            res = []
            for i in range(len(lis)):
                if lis[i] == -1:
                    so = sorted(res[p: i - 1])[::-1]
                    res[p: i - 1] = so
                    break
                if i == 0:
                    p = i
                else:
                    if lis[i - 1] != lis[i]:
                        so = sorted(res[p: i])[::-1]
                        res[p: i] = so
                        p = i
                for key in self.posts.keys():
                    if (self.posts[key] == lis[i]) and key not in res:
                        res.append(key)
                        break
            return res
