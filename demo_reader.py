import redis

def read_and_acknowledge_stream(redis_conn, stream_name):
    try:
        # Read messages from the stream
        messages = redis_conn.xread({stream_name: 0}, count=10)

        for stream, message_data in messages:
            for message in message_data:
                message_id, message_values = message
                process_event(message_values)  # Implement your event processing logic here

                # Acknowledge the processed message
                redis_conn.xack(stream_name, '', message_id)  # Note the empty consumer name

                # Delete the processed message from the stream
                redis_conn.xdel(stream_name, message_id)
    except Exception as e:
        print(f"Error: {e}")

def process_event(event_data):
    # Implement your event processing logic here
    print(f"Processing event: {event_data}")

if __name__ == "__main__":
    # Replace these values with your actual Redis server details
    redis_host = 'localhost'
    redis_port = 6379
    redis_password = None

    # Replace this value with your stream name
    stream_name = 'ejfat'

    # Create a Redis connection
    redis_conn = redis.Redis(host=redis_host, port=redis_port, password=redis_password)

    # Start reading and acknowledging messages from the stream
    read_and_acknowledge_stream(redis_conn, stream_name)
