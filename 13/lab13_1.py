import matplotlib.pyplot as plt

def read_events_file(file_path):
    with open(file_path, 'r') as file:
        events = file.readlines()
    return events

def filter_events(events):
    filtered_events = []
    for event in events:
        timestamp = float(event.split()[0])
        if timestamp < 1:
            filtered_events.append(event)
        else:
            break
    return filtered_events

def split_events(filtered_events):
    timestamps, xs, ys, polarities = [], [], [], []
    for event in filtered_events:
        timestamp, x, y, polarity = event.split()
        timestamps.append(float(timestamp))
        xs.append(int(x))
        ys.append(int(y))
        polarities.append(int(polarity))
    return timestamps, xs, ys, polarities

def analyze_events(timestamps, xs, ys, polarities):
    num_events = len(timestamps)
    first_timestamp = timestamps[0]
    last_timestamp = timestamps[-1]
    max_x = max(xs)
    min_x = min(xs)
    max_y = max(ys)
    min_y = min(ys)
    num_positive_events = sum(1 for p in polarities if p == 1)
    num_negative_events = sum(1 for p in polarities if p == 0)

    print("Number of events:", num_events)
    print("First timestamp:", first_timestamp)
    print("Last timestamp:", last_timestamp)
    print("Maximum x coordinate:", max_x)
    print("Minimum x coordinate:", min_x)
    print("Maximum y coordinate:", max_y)
    print("Minimum y coordinate:", min_y)
    print("Number of positive polarity events:", num_positive_events)
    print("Number of negative polarity events:", num_negative_events)

    return num_events, first_timestamp, last_timestamp, max_x, min_x, max_y, min_y, num_positive_events, num_negative_events

def visualize_events(xs, ys, timestamps, polarities):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(xs, ys, timestamps, c=polarities, cmap='coolwarm')
    ax.set_xlabel('X Coordinate')
    ax.set_ylabel('Y Coordinate')
    ax.set_zlabel('Timestamp')
    ax.set_title('Event Data Visualization')
    plt.show()

def main():
    events_file_path = "events.txt"
    events = read_events_file(events_file_path)
    filtered_events = filter_events(events)
    timestamps, xs, ys, polarities = split_events(filtered_events)

    analyze_events(timestamps, xs, ys, polarities)
    visualize_events(xs, ys, timestamps, polarities)

if __name__ == "__main__":
    main()
