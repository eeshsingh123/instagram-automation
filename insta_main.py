from instapy import InstaPy

from config import INSTA_USERNAME, INSTA_PASSWORD


class InstaAutomate:
    def __init__(self):
        print("logging into Insta py")
        self.session = InstaPy(username=INSTA_USERNAME, password=INSTA_PASSWORD)
        self.session.login()
        print("login successful!")

    def close_session(self):
        self.session.end()

    def set_usage_quota(self):
        print("SETTING QUOTA")
        self.session.set_quota_supervisor(
            enabled=True,
            sleepyhead=True,
            notify_me=True,
            peak_likes_hourly=30,
            peak_likes_daily=400,
            peak_comments_daily=140,
            peak_comments_hourly=30,
            peak_follows_hourly=49,
            peak_unfollows_hourly=35,
            peak_unfollows_daily=402,
            peak_server_calls_daily=4700
        )

        print("QUOTA SET")

    def like_posts_by_hashtags(self, hashtag_list, follow=False, comment=False):

        # self.session.set_smart_hashtags(['rakshabandhan', 'rakhi', 'rakhigift', 'rakhigifts'], limit=10, sort='top', log_tags=True)
        print("MANUAL LOG-> DOING LIKE BY TAGS")
        # self.session.like_by_tags(amount=10, use_smart_hashtags=True)
        # self.session.like_by_tags(hashtag_list, amount=3)
        self.session.set_do_follow(True, percentage=80)
        self.session.set_do_comment(True, percentage=80)
        self.session.set_comments([
            """Hey, We curate and deliver Specialized Hampers dedicated to the auspicious events across the country, Do check out profile out >>>> ❤.""",
            "Hey, Looking for a Gift Hamper this Raksha Bandhan Season? Check our profile out. We have best Hampers at the most reasonable prices ❤.",
            "Hi, Check our profile out for the best Hampers at the best Prices >>> We are currently selling hampers for Raksha Bandhan.",
            "Hey, Great Picture!, Do check our profile out for the Best and Reasonable Hampers for Raksha Bandhan and many more events.",
            "Hey, Great Picture!, Visit our profile and DM us to get your hands on the Best Gift Hampers for your Loved ones."
        ])
        self.session.like_by_tags(hashtag_list, amount=3)
        # self.session.set_do_comment(True, percentage=80)
        # self.session.set_comments([
        #     """Hey, We curate and deliver specialized Hampers dedicated to the auspicious events across the country, Do check out profile out >>>> ❤""",
        #     "Hey, Looking for a Gift Hamper this Raksha Bandhan Season? Check our profile out. We have best Hampers at the most reasonable prices ❤",
        #     "Hi, Check our profile out for the best Hampers at the best Prices >>> We are currently selling hampers for Raksha Bandhan",
        #     "Hey, Great Picture!. Do check out profile out for the Best and Reasonable Hampers for Raksha Bandhan and many more events",
        #     "Hey! Great Picture!, Visit our profile and DM us to get your hands on the Best Gift Hampers for your Loved ones."
        # ])

        print("ENDING SESSION")
        self.session.end()
        print("SESSION COMPLETE")

        return True


if __name__ == "__main__":
    htag_list = ['bhfyp', 'bhai', 'bhaibehen', 'rakshabandhan', 'happyrakshabandhan', 'rakhi', 'bestsister', 'photorakhi', 'rakhicelebration', 'independenceday', 'gift', 'rakhis', 'brothersisterlove', 'rakhi2021', 'hampers', 'rakshabandhangifts', 'rakhigifts', 'brotherandsister', 'siblings', 'bhai', 'rakshabandhanspecial', 'rakhigift']
    ia = InstaAutomate()
    ia.set_usage_quota()
    ia.like_posts_by_hashtags(
        hashtag_list=htag_list,
        follow=True,
        comment=True
    )