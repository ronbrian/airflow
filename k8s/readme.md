# Airflow Container

Apache Airflow Version 1.10.9 running on 
    port : 8083
    Target port : 8080

Image name :
    [interinteltechnologies/airflow](https://hub.docker.com/r/interinteltechnologies/airflow)

## Storage
This container does not require a PVC & PV since it is directly mounted to an Azure fileshare, which is mounted to the path /mnt/azure inside the container.

Before deploying the container, create a Azure Storage account and a File Share. 

## Secrets
For authentication, Azure File share uses the Storage account name and Storage Account Key.
If you'll  use the secrets file, both the storage account name and key must be encoded in Base64.

    echo -n 'storageaccountname' | openssl base64

If you'll manually create the secret, use the following command 

```
kubectl create secret generic azure-secret --from-literal=azurestorageaccountname=MYSTORAGEACCOUNT --from-literal=azurestorageaccountkey=STORAGEKEY
```



