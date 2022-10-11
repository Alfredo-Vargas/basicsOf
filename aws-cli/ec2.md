- List your EC2 instances

```console
aws ec2 describe-instances --profile <profile-name>
```

- Copying from S3 to EC2

```console
aws s3 cp s3://<bucket-name>/object /path/to/destination/
```


- List Images, **IMPORTANT** use describe-images within a region, outputs are huge!


```console
aws ec2 describe-images \
  --region eu-central-1 \
```
