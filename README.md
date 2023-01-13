# Python back-end project
## Content Platform API using Django

**- Define models to represent the structure explained above.**<br/>

<img width="610" alt="image" src="https://user-images.githubusercontent.com/120499098/208117958-33157314-46a3-41bb-80b3-0405f08b504e.png">

**- Create a management command to efficiently calculate the ratings of every
channel and export them in a csv file sorted by rating (i.e. the highest rated
channels on top). The csv contains two columns: channel title, average rating.**<br/>
<br/> To run the management command:
  
```bash
  $ python manage.py compute_ratings
```
  
**- Create endpoints to retrieve the channels, their subchannels and its contents.**<br/>
<br/> There are enpoints created to:
<br/> - http://127.0.0.1/platform -> returns all the channels, subchannels and contents of the platform.
<br/> - http://127.0.0.1/channels/parent_channel=id -> returns the subchannels of the parent_channel, if no arguments are specified it returns all the channels. 
<br/> - http://127.0.0.1/contents/parent_channel=id -> returns the contents of the parent_channel, if no arguments are specified it returns all the contents.

**- Add unit tests to test the channel rating algorithm.**<br/>
Added unit tests for two methods inside the management command (calculate_channel_means and order_ratings). 
<br/> To execute them run the command:
```bash
  $ python manag.py test
```
**- Adding Groups to the channels. Considering that each channel can belong to
multiple groups. Allow filtering by group on Channels API.
Note: Take into account that any channel’s groups set should be included in its
parent’s group set**<br/>
The model for Groups was created, having the channels Model as a field with ManyToMany relation. Also an endpoint was created:
<br/> - http://127.0.0.1/groups/name=name -> returns the channels of the group, if no arguments are specified it returns all the groups.<br/>
The part of editting the Group Model adding a channel to the group of a subchannel was not developed.

