followers = open("followers.txt", "r")
followers = followers.read()

following = open("following.txt", "r")
following = following.read()

followers_list = list(followers.split(" "))

following_list = list(following.split(" "))



for i in following_list:
    if i not in followers_list:
        print(i)
