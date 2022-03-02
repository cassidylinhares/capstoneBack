from django_extensions.management.jobs import DailyJob
from recommendation import lowestCategory, highestCategory


class Job(DailyJob):
    help = "My sample job."

    def execute(self):
        # executing empty sample job
        # for user in users:
        # lowestCategory()
        # highestCategory()
        # threshold()
        pass
