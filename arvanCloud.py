

ACCESS_KEY = '2159c713-f554-49d4-b0b5-c5025665fe18'
SECRET_KEY = '0e816c03cf097c12b9a0327db853d41b7f194e21bc3681de265e76ba607c66e3'
host = 'https://s3.ir-thr-at1.arvanstorage.com'

import boto3
import os
import sys
import threading

from cv2 import setRNGSeed





class ProgressPercentage(object):

    def __init__(self, filename,label):
        self._filename = filename
        self._size = float(os.path.getsize(filename))
        self._seen_so_far = 0
        self._lock = threading.Lock()
        self.label=label
    def __call__(self, bytes_amount):
        # To simplify, assume this is hooked up to a single filename
        with self._lock:
            self._seen_so_far += bytes_amount
            percentage = (self._seen_so_far / self._size) * 100
            sys.stdout.write(
                "\r%s  %s / %s  (%.2f%%)" % (
                    self._filename, self._seen_so_far, self._size,
                    percentage))
            self.label.setValue(percentage)
            sys.stdout.flush()
#____________________________________________________________________________________________________________
#
#____________________________________________________________________________________________________________
class Client:
    def __init__(self, access_key, secret_key, host,bukets):
        self.client = boto3.client('s3',
                    aws_access_key_id=access_key,
                    aws_secret_access_key=secret_key,
                    endpoint_url = host)

        self.resource = boto3.resource('s3',
                    aws_access_key_id=access_key,
                    aws_secret_access_key=secret_key,
                    endpoint_url = host)


        self.acess_bucket = bukets


    def check_acces(self, bucket):
        if bucket in self.acess_bucket:
            return True
        return False


class arvanCloud:

    def __init__(self, client):
        self.client = client
        #self.buckets = self.get_all_bucket()


    #____________________________________________________________________________________________________________
    #
    #____________________________________________________________________________________________________________
    def get_all_bucket(self):
        #print("{name}\t{created}".format(name = bucket.name,created = bucket.creation_date ))
        return list(self.client.resource.buckets.all())
    #____________________________________________________________________________________________________________
    #
    #____________________________________________________________________________________________________________
    def get_bucket(self, name):
        if not self.client.check_acces(name):
            print('acess denied')
            return -1
        bucket = self.client.resource.Bucket(name)
        return bucket
    #____________________________________________________________________________________________________________
    #
    #____________________________________________________________________________________________________________
    def get_bucket_names(self):
            buckets = self.get_all_bucket()
            names = list( map ( lambda x:x.name, buckets ))
            return names

    #____________________________________________________________________________________________________________
    #
    #____________________________________________________________________________________________________________
    def get_all_content(self, bucket):
        if not self.client.check_acces(bucket.name):
            print('acess denied')
            return -1
        return list(bucket.objects.all())

    #____________________________________________________________________________________________________________
    #
    #____________________________________________________________________________________________________________
    def get_content_names(self, contents):
            return list( map( lambda x:x.key, contents))


    #____________________________________________________________________________________________________________
    #
    #____________________________________________________________________________________________________________
    def get_directory_content(self, bucket, path):
        # if not client.check_acces(bucket.name):
        #     print('acess denied')
        #     return -1
        contents = self.get_all_content(bucket)
        content_names = self.get_content_names(contents)
        return self.get_hirechy_content(path, content_names)

    #____________________________________________________________________________________________________________
    #
    #____________________________________________________________________________________________________________
    def get_hirechy_content(self, path, contents):
            contents = list(filter( lambda x:x[:len(path)] == path, contents ))
            def get_root_path(x):
                    if x.find('/', len(path)) == -1:
                            return x[len(path):]
                    else:
                            return x[len(path): x.find('/', len(path)) + 1]

            contents = list( map( get_root_path, contents ))
            contents = set( contents )
            return list(contents)


    #____________________________________________________________________________________________________________
    #
    #____________________________________________________________________________________________________________
    def upload(self, bucket, src_path, dst_path ,Callback):
        if not self.client.check_acces(bucket.name):
            print('acess denied')
            return -1
        self.client.client.upload_file(
        src_path, bucket.name, dst_path,
        Callback=Callback)
        dst_path = os.path.join( dst_path, os.path.basename(src_path))
        #self.client.client.upload_file(
        #src_path, bucket.name, dst_path)
    #___________________________________________
    def upload_2(self, bucket, src_path, dst_path ):
        if not self.client.check_acces(bucket.name):
            print('acess denied')
            return -1
        self.client.client.upload_file(
        src_path, bucket.name, dst_path)
        dst_path = os.path.join( dst_path, os.path.basename(src_path))
        #self.client.client.upload_file(
        #src_path, bucket.name, dst_path)_________________________________________________________________
    #
    #____________________________________________________________________________________________________________
    def download(self,bucket, src_path, dst_path ):
        if not self.client.check_acces(bucket.name):
            print('acess denied')
            return -1
        src_path = os.path.join(src_path, os.path.basename(dst_path))
        with open(src_path, 'wb') as f:
            self.client.client.download_fileobj(bucket.name, dst_path, f)




if __name__ == '__main__':
        src_path = 'my.jpg'
        dst_path = 'mk/images/amir.jpg'
        access_buckets=['gits', 'malekzadeh', 'testpython']
        client = Client( ACCESS_KEY, SECRET_KEY, host,access_buckets)
        arvan = arvanCloud(client=client)
        buckets = arvan.get_all_bucket()
        bucket_names = arvan.get_bucket_names()
        print(bucket_names)
        bucket = arvan.get_bucket('testpython')
        contents = arvan.get_all_content(bucket)
        content_names = arvan.get_content_names(contents)
        print(content_names)

        #--------------------------------------------------
       # hirechy_contents = arvan.get_hirechy_content('asnad/', content_names)
       # hirechy_contents = arvan.get_directory_content(bucket, '')
        #for percent in iter(upload_large_data(bucket, src_path, dst_path)):
        #        print(percent,'%')

        #--------------------------------------------------
        
        src_path = 'G:\work/abrarvan/New folder (4)\data.xlsx'
        dst_path = 'mk/im/dtview/data.xlsx'
        qw=9
        perc=ProgressPercentage(src_path,qw)
        arvan.upload_2( bucket, src_path, dst_path)

        #arvan.download(bucket,src_path, dst_path)
        #--------------------------------------------------
        
      #  print(hirechy_contents)
        #print(content_names)
      #  print(bucket_names)
        

