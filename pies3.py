#!/usr/bin/python3

## setup
#db = dbconnection()
#db.connect

#for file in backupfolder:
  #chksum = checksum(file)
  #chksum_aws = dynamodb_select(file.name)

  ## improvement of below - batch uploading
  #if chksum != chksum_aws:
    #enc_file = encrypt(file,folder,key)
    #s3 put enc_file
    #dynamodb_insert(file.name,chksum)

#def dynamodb_select(filename)
  #return db.select(filename)

#def dynamodb_insert(filename,checksum)
  #return db.insert(filename,checksum)
