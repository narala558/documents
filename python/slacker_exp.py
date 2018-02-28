import slacker
import os


s = slacker.Slacker(os.environ.get('AK_SLACK_TOKEN', None))


s.chat.post_message(
    channel=input('Recipient: '),
    text=input('Message: '),
    username='Aditya Pahuja',
    icon_url='https://avatars.slack-edge.com/2016-04-26/37731059143_55ad93daa31bf1846e2b_48.jpg',
)
