from csv import reader, writer

with open('hacker_news.csv', 'r', encoding='utf-8') as csv_file:
	data = reader(csv_file)
	hn = list(data)
	headers = hn[0]
	hn = hn[1:]

ask_posts = []
show_posts = []
other_posts = []

for row in hn:
	title = row[1].lower()
	if title.startswith('ask hn'):
		ask_posts.append(row)
	elif title.startswith('show hn'):
		show_posts.append(row)
	else:
		other_posts.append(row)

print(headers, end="\n\n")
print(hn[:3])
print(ask_posts[0])
print(show_posts[0])
print(other_posts[0], end="\n\n")

avg_ask_comments = 0
for post in ask_posts:
	num_comments = int(post[4])
	avg_ask_comments += num_comments/len(ask_posts)

avg_show_comments = 0
for post in show_posts:
	avg_show_comments += int(post[4])/len(show_posts)

print("The average of 'Show HN' posts: " + str(round(avg_show_comments, 2)))
print("The average of 'Ask HN' posts: " + str(round(avg_ask_comments, 2)) + "\n")

import datetime as dt

result_1_list = []
for row in ask_posts:
	result_1_list.append([row[-1],row[4]])

counts_by_hour = {}
comments_by_hour = {}

for row in result_1_list:
	hour = dt.datetime.strptime(row[0], "%m/%d/%Y %H:%M").strftime("%H")
	if  hour in counts_by_hour:
		counts_by_hour[hour] += 1
		comments_by_hour[hour] += int(row[1])
	else:
		counts_by_hour[hour] = 1
		comments_by_hour[hour] = int(row[1])
print("The amount of comments for 'Ask HN' posts by Hour: ", comments_by_hour, end="\n\n")

avg_by_hour = []
for hour in comments_by_hour:
	avg_by_hour.append([hour,comments_by_hour[hour]/counts_by_hour[hour]])
print("The average of comments for a 'Ask HN' post by Hour: ", avg_by_hour, end="\n\n")

swap_avg_by_hour = []
for avg in avg_by_hour:
	swap_avg_by_hour.append([avg[1],avg[0]])
sorted_swap = sorted(swap_avg_by_hour, reverse=True)

print("Top 5 Hours for 'Ask HN' Comments")
for avg, hour in sorted_swap[:5]:
    print("{0}: {1:.2f} average comments per post".format(dt.datetime.strptime(hour, "%H").strftime("%H:%M"), avg))
print("\nBased on our analysis, to maximize the amount of comments a post receives, we'd recommend the post be categorized as ask post and created between 15:00 and 16:00 (2:00 - 3:00 in Hanoi, Vietnam).")

print("\n----------------\n")

avg_ask_points = 0
avg_show_points = 0
for row in ask_posts:
	avg_ask_points += int(row[3])/len(ask_posts)
for row in show_posts:
	avg_show_points += int(row[3])/len(show_posts)
print("The average of 'Show HN' points: " + str(round(avg_show_points, 2)))
print("The average of 'Ask HN' points: " + str(round(avg_ask_points, 2)) + "\n")

result_2_list = []
for row in show_posts:
	result_2_list.append([row[-1],row[3]])

counts_2_by_hour = {}
points_by_hour = {}

for row in result_2_list:
	hour = dt.datetime.strptime(row[0], "%m/%d/%Y %H:%M").strftime("%H")
	if  hour in counts_2_by_hour:
		counts_2_by_hour[hour] += 1
		points_by_hour[hour] += int(row[1])
	else:
		counts_2_by_hour[hour] = 1
		points_by_hour[hour] = int(row[1])
print("The amount of points for 'Show HN' posts by Hour: ", points_by_hour, end="\n\n")

avg_points_by_hour = []
for hour in points_by_hour:
	avg_points_by_hour.append([hour,points_by_hour[hour]/counts_2_by_hour[hour]])
print("The average of points for a 'Show HN' post by Hour: ", avg_points_by_hour, end="\n\n")

swap_avg_points_by_hour = []
for avg in avg_points_by_hour:
	swap_avg_points_by_hour.append([avg[1],avg[0]])
sorted_swap_points = sorted(swap_avg_points_by_hour, reverse=True)

print("Top 5 Hours for 'Show HN' points")
for avg, hour in sorted_swap_points[:5]:
    print("{0}: {1:.2f} average points per post".format(dt.datetime.strptime(hour, "%H").strftime("%H:%M"), avg))
print("\nBased on our analysis, to maximize the amount of points a post receives, we'd recommend the post be categorized as show post and created between 23:00 and 00:00 (10:00 - 11:00 in Hanoi, Vietnam).")
print("\n----------------\n")
print("In conclusion, readers/users usually learn by finding new projects at night (22:00 - 01:00), whereas the admin working & answer users' asks at the last of the day (15:00 - 16:00).")