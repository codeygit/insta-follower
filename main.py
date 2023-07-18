import instaloader

L = instaloader.Instaloader()

L.login("justcodey", "Chockey10-")

profile = instaloader.Profile.from_username(L.context, "justcodey")

follow_list=[]

for follower in profile.get_followers():
    follow_list.append(follower.username)

for following in profile.get_followees():
    temp = str(following).split(" ")
    name = temp[1]
    if not name in follow_list:
        print(name)

