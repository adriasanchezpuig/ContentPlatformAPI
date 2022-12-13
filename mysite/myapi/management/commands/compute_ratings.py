from django.core.management.base import BaseCommand
from myapi.models import Channel, Content
from statistics import mean
import csv



class Command(BaseCommand):
    help = 'Computes ratings of the channels by their contents and exports the result to a .csv file'

    def handle(self, *args, **kwargs):
        ratings = {}
        for channel in Channel.objects.all():
            ratings.setdefault(channel.title, [])
        for content in Content.objects.all():
            ratings[content.cahnnel.title].append(content.rating)
        for channel in ratings:
            ratings[channel] = mean(ratings[channel])
        sorted_ratings = sorted(ratings.items(), key=lambda x:x[1], reverse=True)
        with open('ratings.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(['Channel title','Rating'])
            for channel in sorted_ratings:
                f.write("%s,%s\n"%(channel[0],channel[1]))
        pass