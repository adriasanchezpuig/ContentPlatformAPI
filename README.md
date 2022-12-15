# IMMFLY backend test

- Create a Django project to define an API.
< br /> The project was created following the steps on this blog: 
< br /> https://medium.com/swlh/build-your-first-rest-api-with-django-rest-framework-e394e39a482c

```bash
$ pip install virtualenv
$ pip install django
$ pip install djangorestframework
```

- Define models to represent the structure explained above.

![Diagrama sense títol drawio](https://user-images.githubusercontent.com/120499098/207666548-d0ea31bb-09ac-4c59-8feb-c04450343a45.png)

- Create a management command to efficiently calculate the ratings of every
channel and export them in a csv file sorted by rating (i.e. the highest rated
channels on top). The csv contains two columns: <channel title>, <average
rating>
<br /> To run the management command:
```bash
  $ python manag.py compute_ratings
```

- Create endpoints to retrieve the channels, their subchannels and its contents.
< br /> Endpoints were created following the steps on this blog:
< br /> https://dev.to/jenhsuan/day-23-of-100daysofcode-create-endpoints-with-query-string-on-django-rest-framework-d5o

