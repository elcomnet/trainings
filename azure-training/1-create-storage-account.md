# Lab 01 - Create Azure Storage Account

## Lab introduction

In this lab you learn to create first resource Storage Accounts for Azure blobs

## Estimated timing: 15 minutes

## Task 1: Create and configure a storage account. 

In this task, you will create and configure a storage account. The storage account will use geo-redundant storage and will not have public access. 

1. Sign in to the **Azure portal** - `https://portal.azure.com`.

1. Search for and select `Storage accounts`, and then click **+ Create**.

1. On the **Basics** tab of the **Create a storage account** blade, specify the following settings (leave others with their default values):

    | Setting | Value |
    | --- | --- |
    | Subscription          | the name of your Azure subscription  |
    | Resource group        | **workshop-X** |
    | Storage account name  | **azworkshopstudentX** |
    | Region                | **(Europe) West/North Europe**  |
    | Performance           | **Standard**  |
    | Redundancy            | **Geo-redundant storage** |
    | Make read access to data in the event of regional availability | Check the box |

1. Click **Review + create**, wait for the validation process to complete, and then click **Create**.

## Task 2: Create blob storage

In this task, you will create a blob container and upload an image. Blob containers are directory-like structures that store unstructured data.

1. Continue in the Azure portal, working with your storage account.

1. In the **Data storage** section, click **Containers**. 

1. Click **+ Container** and **Create** a container with the following settings:

    | Setting | Value |
    | --- | --- |
    | Name | `data`  |
    | Public access level | Notice the access level is set to private |

## Task 3: Upload file
1. Return to the containers page, select your **data** container and then click **Upload**.

1. On the **Upload blob** blade, expand the **Advanced** section.

    >**Note**: Locate a file to upload. This can be any type of file, but a small file is best. A sample file can be downloaded from the AllFiles directory. 

    | Setting | Value |
    | --- | --- |
    | Browse for files | add the file you have selected to upload |
    | Select **Advanced** | |
    | Blob type | **Block blob** |
    | Block size | **4 MiB** |
    | Access tier | **Hot**  (notice the other options) |
    | Encryption scope | Use existing default container scope |

1. Click **Upload**.
