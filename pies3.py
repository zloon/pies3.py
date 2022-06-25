'''S3 Backup with pre-internet encryption'''

# TODO - add setup options
# TODO - custom mappings of local directories to specific s3 buckets or paths
# TODO - rate limit API calls, maybe with https://pypi.org/project/ratelimit/

'''Calculates the checksum of either a local file or an S3 object'''
def calculate_checksum(file: str, algorithm: str = "SHA-256") -> str:
  # If file is an S3 url
    # Call S3 metadata to get checksum

  # Else
    # Check if file exists locally
    # If it does, calculate & return checksum
    # If not, throw error

  pass

'''Returns the full S3 path for a local file'''
def s3_path(file_path: str, directory: str) -> str:
  pass

'''encrypts a file, placing it in the specified location'''
def encrypt(source_file_path: str, encrypted_file_path: str) -> str:
  pass # TODO - encrypt, return location of encrypted file

'''uploads a file to s3 and sets the checksum'''
def upload(file_path: str, checksum: str) -> str:
  pass # TODO - upload to S3 and set checksum metadata

uploadqueue = []
tmp_directory = "" # TODO - Set tmp directory

# Set up database connection
# Either DynamoDB or local DB

# Get backup folders for current host
list_of_directories = [] # TODO - get this from database


# Iterate over files in each backup folder
for directory in list_of_directories:
  checksum_local = ""

  for file_path in directory:
    # Calculate the file's checksum and the remote file's checksum
    try:
      checksum_local = calculate_checksum(file_path)
    except FileNotFoundError as err:
      pass # TODO - print error and skip

    try:
      checksum_s3 = calculate_checksum(s3_path(file_path, directory))
    except FileNotFoundError as err: # This (likely?) means that there's no backup of the file yet. TODO - differentiate errors
      checksum_s3 = ""
      
    # If the checksums doesn't match, add to queue for encryption & upload
    if checksum_local != checksum_s3:
      uploadqueue.append((file_path, checksum_local))

# Iterate over the upload queue
for file_path, checksum in uploadqueue:
  # Encrypt the file
  encrypted_file_path = encrypt(file_path, tmp_directory)

  # Upload it to S3 and set metadata
  try:
    upload(encrypted_file_path, checksum)
  except:
    pass # TODO - error handling

  # TODO - Remove temporary file when done