import boto
import boto.s3.connection
import math, os
#from filechunkio import FileChunkIO

access_key = '2159c713-f554-49d4-b0b5-c5025665fe18'
secret_key = '0e816c03cf097c12b9a0327db853d41b7f194e21bc3681de265e76ba607c66e3'
host = 's3.ir-thr-at1.arvanstorage.com'

def connect(access_key, secret_key, host):
        conn = boto.connect_s3(
                aws_access_key_id = access_key,
                aws_secret_access_key = secret_key,
                host = host,
                #is_secure=False,               # uncomment if you are not using ssl
                calling_format = boto.s3.connection.OrdinaryCallingFormat(),
                )

        return conn



def getAllBucket(conn):
        buckets = []
        for bucket in conn.get_all_buckets():
                print("{name}\t{created}".format(
                        name = bucket.name,
                        created = bucket.creation_date,
                ))
                buckets.append(buckets)
        return buckets



# def getBucketByName(name, conn):
#         for bucket in conn.get_all_buckets():
#             if bucket.name == name:
#                 for key in bucket.list(prefix=name): 
#                         print(key)
#                         print('q')
#                 return bucket



def new_bucket(fname, bucket):
        key = bucket.new_key(fname)
        fs = open(fname, mode='r')
        key.set_contents_from_filename(fname)


def getbucket(name,conn):
        mybucket = conn.get_bucket(name) # Substitute in your bucket name
        return mybucket
        mybucket.list()
        print(mybucket)


def get_all(conn):
        rs = conn.get_all_buckets()
        for b in rs:
                print(b.name)
        b = rs[2]
        # print(rs[1])
        # b.set_acl('public-read')
        # acp = b.get_acl()
        # print(acp)
        # print(acp.acl.grants)
        # for grant in acp.acl.grants:
        #         print (grant.permission, grant.display_name, grant.email_address, grant.id)
        return b


from boto.s3.key import Key

def setting_metadata(conn,b):
        k = Key(b)
        k.key = 'has_metadata'
        k.set_metadata('meta1', 'This is the first metadata value')
        k.set_metadata('meta2', 'This is the second metadata value')
        k.set_contents_from_filename('your_file.txt')

def storing_data(conn,b):
        b = conn.get_bucket('malekzadeh')
        k = Key(b)
        k.key = 'has_metadata'
        k.get_contents_as_string()
        print(k.get_contents_to_filename('your_file.txt'))

        
def access_bucket(conn,name):
       mybucket = conn.get_bucket(name, validate=False) 
       lis=mybucket.list()
       for key in mybucket.list(prefix='dir-in-bucket/'): 
               print(key)

       print(lis)





def upload_large_data(conn):
        b=conn.get_bucket('amirhoseinebrahimi')
        print(b)
        source_path = 'G:\work/abrarvan\images\dorsa2.png'
        source_size = os.stat(source_path).st_size
        print(source_size)
        # Create a multipart upload request
        mp = b.initiate_multipart_upload(os.path.basename(source_path))
        chunk_size = 52428800
        chunk_count = int(math.ceil(source_size / float(chunk_size)))
        for i in range(chunk_count):
                offset = chunk_size * i
                bytes = min(chunk_size, source_size - offset)
                with FileChunkIO(source_path, 'r', offset=offset,bytes=bytes) as fp:
                        mp.upload_part_from_file(fp, part_num=i + 1)
        mp.complete_upload()


def get_content(conn):
        content=[]
        bucket = conn.get_bucket('amirhoseinebrahimi')
        for key in bucket.list():
               # print('content')
                #print(key.name.encode('utf-8'))
                content.append(key.name.encode('utf-8'))
        print(content)
        return content

def upload(conn,b):
        k = Key(b)
        k.key = 'myfile'
        k.set_contents_from_filename('G:\work\PySide-Responsive-ui-master\myqr.png')
        k.get_contents_to_filename('G:\work\PySide-Responsive-ui-master\data.xlsx')
conn = connect( access_key, secret_key, host)
# b=buckets=get_all(conn)
# storing_data(conn,b)
# #setting_metadata(conn,b)
# access_bucket(conn,'malekzadeh')
#upload_large_data(conn)
# x=get_content(conn)
# print(x)
# x=get_content(conn)
# print(getAllBucket(conn))
y=get_all(conn)
print(y)
a=getbucket(y,conn)
# upload(conn,a)

print(get_content(conn)

possible_key = a.get_key('myfile')
print(possible_key) 
m