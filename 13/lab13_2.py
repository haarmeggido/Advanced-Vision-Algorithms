import matplotlib.pyplot as plt

def read_events(file_path, num_events=None):
    events = []
    with open(file_path, 'r') as file:
        for i, line in enumerate(file):
            if num_events is not None and i >= num_events:
                break
            timestamp, x, y, polarity = map(float, line.strip().split())
            events.append((timestamp, x, y, polarity))
    return events

def visualize_events(xs, ys, timestamps, polarities, title, save = False):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(xs, ys, timestamps, c=polarities, cmap='coolwarm')
    ax.set_xlabel('X Coordinate')
    ax.set_ylabel('Y Coordinate')
    ax.set_zlabel('Timestamp')
    ax.set_title(title)
    ax.view_init(elev=-90, azim=-90)
    plt.show()

    if save:
        plt.savefig(title + '.png')

events_1 = read_events('13/mats/events.txt', num_events=8000)
timestamps_1 = [event[0] for event in events_1]
xs_1 = [event[1] for event in events_1]
ys_1 = [event[2] for event in events_1]
polarities_1 = [event[3] for event in events_1]
visualize_events(xs_1, ys_1, timestamps_1, polarities_1, 'First 8000 Events')

print('Number of events:', len(events_1))
events_2 = read_events('13/mats/events.txt')
filtered_events_2 = [event for event in events_2 if 0.5 <= event[0] <= 1]
timestamps_2 = [event[0] for event in filtered_events_2]
xs_2 = [event[1] for event in filtered_events_2]
ys_2 = [event[2] for event in filtered_events_2]
polarities_2 = [event[3] for event in filtered_events_2]
visualize_events(xs_2, ys_2, timestamps_2, polarities_2, 'Events with Timestamp between 0.5 and 1')

plt.show()