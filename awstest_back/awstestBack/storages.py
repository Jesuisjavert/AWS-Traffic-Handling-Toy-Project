from storages.backends.s3boto3 import S3Boto3Storage

__all__ = (
    'S3StaticStorage',
    'S3DefaultStorage',
)

class S3DefaultStorage(S3Boto3Storage):
    default_acl = 'private'
    location = 'media'

class S3StaticStorage(S3Boto3Storage):
    default_acl = 'public-read'
    location = 'static' 