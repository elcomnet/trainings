# Lab 07 - Manage Virtual Machine

## Lab introduction

In this lab you your first Virtual Machine using Portal, Powershell and CLI

## Estimated time: 50 minutes

## Task 1:  Create a virtual machine 

1. Sign in to the **Azure portal** - `https://portal.azure.com`.

1. Search for and select `Virtual Machines`.

1. From the virtual machines page, select **Create** then select **Azure Virtual Machine**.

1. On the Basics tab, use the following information to complete the form, and then select **Next: Disks >**. For any setting not specified, leave the default value.
 
    | Setting | Value | 
    | --- | --- |
    | Subscription |  *your subscription* |
    | Resource group |  `workshop-X` 
    | Virtual machine name |    `vm-student-X` |
    | Region | (Europe) ** West/North Europe**  |
    | Availability options | No infrastructure redundancy required |
    | Security type | **Standard** |
    | Image | **Ubuntu Server 20.04 LTS - x64 Gen2**  |
    | Size | **Standard_B1s** |
    | Authentication type | 'Password' |
    | Username | `localadmin` | 
    | Password | **Provide a complex password** |
    | Public inbound ports | **Allow selected ports** |
    | Select inbound ports | **SSH (22)** |
  
1. On the **Disks** tab take the defaults and then select **Next: Networking >**.

1. On the **Networking** tab, for Virtual network, select **Create new**.

1. Use the following information to configure the virtual network, and then select **Ok**. If necessary, remove or replace the existing information.

    | Setting | Value | 
    | --- | --- |
    | Name | `CoreServicesVnet` (Create new) |
    | Address range | `10.Z.0.0/16` (Z = 20 + X)  |
    | Subnet Name | `Core` | 
    | Subnet address range | `10.Z.0.0/24` |

1. On the **Networking** tab, for Public IP, select **Create new**.

1. Use the following information to configure the virtual network, and then select **Ok**. If necessary, remove or replace the existing information.
   
   | Public IP |  select **Create new** and type Name = 'ip-public-student-X'|
   
1. Select the **Monitoring** tab. For Boot Diagnostics, select **Disable**.

1. Select **Review + Create**, and then select **Create**.

## Task 2: Resize compute of VM

1. On the **vm-student-X** virtual machine, in the **Availability + scale** blade, select **Size**.

1. Set the virtual machine size to **Standard_B2s** and click **Resize**. When prompted, confirm the change.

## Task 3: Add disk to VM

1. Go to the **vm-student-X** virtual machine

1. In the **Settings** area, select **Disks**.

1. Under **Data disks** select **+ Create and attach a new disk**. Configure the settings (leave other settings at their default values).

    | Setting | Value |
    | --- | --- |
    | Disk name | `vm1-disk1` |
    | Storage type | **Standard HDD** |
    | Size (GiB) | `32` |

1. Click **Apply**.

1. After the disk has been created, click **Detach** (if necessary, scroll to the right to view the detach icon), and then click **Apply**.

    >**Note**: Detaching removes the disk from the VM but keeps it in storage for later use.

1. Search for and select `Disks`. From the list of disks, select the **vm1-disk1** object.

    >**Note:** The **Overview** blade also provides performance and usage information for the disk.

1. In the **Settings** blade, select **Size + performance**.

1. Set the storage type to **Standard SSD**, and then click **Save**.

1. Navigate back to the **vm-student-X** virtual machine and select **Disks**.

1. In the **Data disk** section, select **Attach existing disks**.

1. In the **Disk name** drop-down, select **vm1-disk1**. 

1. Verify the disk is now **Standard SSD**.

1. Select **Apply** to save your changes.

## Task 4: Extend data disk

1. Navigate back to the **vm-student-X** virtual machine and select **Disks**.

1. In the **Data disk** section, click on **vm1-disk1**
   
1. In section **Size + performance** select **64 GiB** size of disk, Tier E6
   
1. Click **Save**

## Task 5: Extend boot disk

1. Navigate back to the **vm-student-X** virtual machine and select **Disks**.

1. In the **Data disk** section **OS disk**
   
1. Click on Name od disk
   
1.  In section **Size + performance** select **64 GiB** size of disk, Tier S6

1. Click **Save**

1. Restart the VM, and then access the VM using the root user account.

1. Verify that the OS disk now displays an increased file system size.
  ```shell
  df -Th
  ```
