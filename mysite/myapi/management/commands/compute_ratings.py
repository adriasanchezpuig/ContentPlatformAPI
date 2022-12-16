from django.core.management.base import BaseCommand
from myapi.models import Channel, Content
from statistics import mean
import csv



class Command(BaseCommand):
    help = 'Computes ratings of the channels by their contents and exports the result to a .csv file'

    def handle(self, *args, **kwargs):
        ratings = {}
        for content in Content.objects.all():
            ratings.setdefault(content.parent_channel.title, []).append(content.rating)
        for channel in Channel.objects.all():
            if channel.parent_channel:
                ratings.setdefault(channel.parent_channel.title, [])
                for rating in ratings[channel.title]: ratings[channel.parent_channel.title].append(rating)
        mean_ratings = self.calculate_channel_means(ratings)
        sorted_ratings = self.order_ratings(mean_ratings)
        self.export_csv(sorted_ratings)
        return str(sorted_ratings)
    
    def calculate_channel_means(self, ratings):
        means = {}
        for channel in ratings:
            means[channel] = round(mean(ratings[channel]),2)
        return means
    
    def order_ratings(self, ratings):
        sorted_ratings = sorted(ratings.items(),
            key=lambda x:x[1],
            reverse=True
        )
        return sorted_ratings

    def export_csv(self, sorted_ratings):
        with open('ratings.csv', 'w') as f:
            write = csv.writer(f)
            write.writerow(["Channel", "Rating"])
            write.writerows(sorted_ratings)
