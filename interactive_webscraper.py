from instagram_bot import InstaBot

username = input("Please give me your username: ")
password = input("Please give me your password: ")

bot_object = InstaBot(username, password)
bot_object.login()

prompt = input("Press 1 if you would like to search by account name , and 2 if by hashtag: ")

if prompt == '1':
    account_name = input("Please enter the account name: ")
    account_links = bot_object.get_photo_links_by_account(account_name)
    time_and_likes = bot_object.get_time_and_likes(account_links)
    print(time_and_likes)
    x = time_and_likes[0][2] < time_and_likes[1][2]
    print(x)

elif prompt == '2':
    hashtag = input("Please enter the hashtag: ")
    hashtag_links = bot_object.get_photo_links_by_account(hashtag)
    time_and_likes = bot_object.get_time_and_likes(hashtag_links)
    print(time_and_likes)