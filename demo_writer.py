import redis

def write_file_to_redis_stream(file_path, stream_name, chunk_size=8192):
    """
    Args:
      - chunk_size: chunck size in bytes.
    """
    r = redis.StrictRedis(host='localhost', port=6379, db=0)

    # Open the file in binary mode
    with open(file_path, 'rb') as file:
        entry_id = 0
        while True:
            # Read a chunk of data from the file
            chunk = file.read(chunk_size)

            # Break the loop if the end of the file is reached
            if not chunk:
                break

            # Convert the entry ID to bytes
            entry_id_bytes = str(entry_id).encode('utf-8')

            # Create a dictionary representing the data to be stored in the stream
            data = {'data': chunk.decode('utf-8')}  # Adjust decoding based on your file format

            # Write the data to the Redis Stream
            r.xadd(stream_name, {'entry_id': entry_id_bytes, **data})

            # Increment the entry ID for the next iteration
            entry_id += 1

if __name__ == "__main__":
    file_path = 'test_file'
    stream_name = 'ejfat'

    write_file_to_redis_stream(file_path, stream_name)
