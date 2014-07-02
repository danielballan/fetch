from __future__ import print_function
import os
import boto

def fetch(bucket_name, key_name, local_only=False):
    """Fetch data from S3, and henceforth use a local copy.

    The file will be sought in the path specified by the environmental variable
    FETCH_STASH or, if that is not defined, it will be sought in the current
    working directory.

    If it is not found locally, fetch will download it from S3. The AWS
    credentials AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY must be defined
    as environemntal variables.

    Parameters
    ----------
    bucket_name : string
       identifing S3 bucket
    key_name : string
       file name ('key') of object to fetch

    Example
    -------
    In [2]: fetch('my-bucket', 'some-file')
    Fetching data from S3...
    Out[2]: '/path/to/some-file'
    """
    stash_directory = os.environ.get('FETCH_STASH', '.')
    path = os.path.join(stash_directory, key_name)
    if os.path.isfile(path):
        return path 
    directory = os.path.dirname(path)
    try: 
        os.makedirs(directory)
    except OSError:
        if not os.path.isdir(directory):
            raise
    if local_only:
        raise ValueError("No local copy at {0}".format(path))
    print("Fetching data from S3...")
    boto.connect_s3().get_bucket(bucket_name).get_key(key_name).get_contents_to_filename(path)
    return path
