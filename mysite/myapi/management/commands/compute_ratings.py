from django.core.management.base import BaseCommand
from myapi.models import Channel, Content
from statistics import mean
import csv



class Command(BaseCommand):
    help = 'Computes ratings of the channels by their contents and exports the result to a .csv file'

    def handle(self, *args, **kwargs):
        ratings = {}
        for channel in Channel.objects.all(): ratings.setdefault(channel.title, [])
        for content in Content.objects.all(): ratings[content.cahnnel.title].append(content.rating)
        mean_ratings = self.calculate_channel_means(ratings)
        sorted_ratings = self.order_ratings(mean_ratings)
        self.export_csv(sorted_ratings)
        return sorted_ratings
    
    def calculate_channel_means(self, ratings):
        means = {}
        for channel in ratings:
            means[channel] = mean(ratings[channel])
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
