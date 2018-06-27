from django.contrib.syndication.views import Feed
from manager.models import Dish


class OrderFeed(Feed):
    title = "Current Orders"
    link = ""
    description = "Updates on changes and additions to orders."

    def items(self):
        return Dish.objects.all()[:5]

    def item_title(self, item):
        return item.name

    def item_description(self, item):
        return item.description

    def item_link(self, item):
        return '/none/'
