from boto3 import Session
import os
from dotenv import load_dotenv

load_dotenv('../OpenPapers/.env')



class FileObj(Session):
    def __init__(self,user_id,filename,*args):     
        super().__init__(*args)
        self.__session=Session(aws_access_key_id=os.getenv('ACCESS_KEY_ID'),
                               aws_secret_access_key=os.getenv('SECRET_ACCESS_KEY'),
                               region_name=os.getenv('REGION'))

        self.bucket=self.__session.resource('s3').Bucket(os.getenv('BUCKET_NAME'))            
        self.user_id=user_id
        self.Key=str(user_id)+'/'+str(filename)
        self.Filename=str(filename)       

    def upload(self):
        file_url=f"https://{os.getenv('BUCKET_NAME')}.s3.amazonaws.com/{self.Key}"
        self.bucket.upload_file(Filename=self.Filename,
                           Key=self.Key,
                           ExtraArgs={'ACL': 'public-read'})
        return file_url


