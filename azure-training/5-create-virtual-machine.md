# Lab 05 - Create Virtual Machine

## Lab introduction

In this lab you your first Virtual Machine using Portal, Powershell and CLI

## Estimated time: 20 minutes

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

1. On the **Networking** tab, for Virtual network, select
    | Setting | Value | 
    | --- | --- |
    | Virtual Network |  *vnet_core_student_X* |
    | Subnet |  `SharedServicesSubnet` |
    | Public IP |  select **Create new** and type Name = 'ip-public-student-X'|
    
1. Select the **Monitoring** tab. For Boot Diagnostics, select **Disable**.

1. Select **Review + Create**, and then select **Create**.

## Task 2: Connect to VM
1. Go to Virtual machine - vm-student-X and read Public IP of your VM

1. Run the following command in your SSH client. In this example, 20.51.230.13 is the public IP Address of your VM and localadmin is the username you created when you created the VM.

   ```ssh localadmin@20.51.230.13```
   
## Task 3: Create a virtual machine using Azure PowerShell

1. Use the icon (top right) to launch a **Cloud Shell** session. Alternately, navigate directly to `https://shell.azure.com`.

1. Be sure to select **PowerShell**. If necessary, configure the shell storage.

1. Run the following command to create a virtual machine. When prompted, provide a username and password for the VM. While you wait check out the [New-AzVM](https://learn.microsoft.com/powershell/module/az.compute/new-azvm?view=azps-11.1.0) command reference for all the parameters associated with creating a virtual machine.

    ```powershell
    New-AzVm `
    -ResourceGroupName 'workshop-X' `
    -Name 'vm-student-X-ps' `
    -Location 'North Europe' `
    -Image 'Win2019Datacenter' `
    -Zone '1' `
    -Size 'Standard_B1s' ` 
    -Credential (Get-Credential)
    ```

1. Once the command completes, use **Get-AzVM** to list the virtual machines in your resource group.

    ```powershell
    Get-AzVM `
    -ResourceGroupName 'workshop-X' `
    -Status
    ```

1. Verify your new virtual machine is listed and the **Status** is **Running**.

1. Use **Stop-AzVM** to deallocate your virtual machine. Type **Yes** to confirm.

    ```powershell
    Stop-AzVM `
    -ResourceGroupName 'workshop-X' `
    -Name 'vm-student-X-ps' 
    ```

1. Use **Get-AzVM** with the **-Status** parameter to verify the machine is **deallocated**.

    >**Did you know?** When you use Azure to stop your virtual machine, the status is *deallocated*. This means that any non-static public IPs are released, and you stop paying for the VM’s compute costs.

## Task 4: Create a virtual machine using the CLI 

1. Use the icon (top right) to launch a **Cloud Shell** session. Alternately, navigate directly to `https://shell.azure.com`.

1. Be sure to select **Bash**. If necessary, configure the shell storage.

1. Run the following command to create a virtual machine. When prompted, provide a username and password for the VM. While you wait check out the [az vm create](https://learn.microsoft.com/cli/azure/vm?view=azure-cli-latest#az-vm-create) command reference for all the parameters associated with creating a virtual machine.

    ```sh
    az vm create --name vm-student-cli --resource-group workshop-X --image Ubuntu2204 --admin-username localadmin --generate-ssh-keys
    ```

1. Once the command completes, use **az vm show** to verify your machine was created.

    ```sh
    az vm show --name  vm-student-X-cli --resource-group workshop-X --show-details
    ```

1. Verify the **powerState** is **VM Running**.

1. Use **az vm deallocate** to deallocate your virtual machine. Type **Yes** to confirm.

    ```sh
    az vm deallocate --resource-group workshop-X --name vm-student-X-cli
    ```

1. Use **az vm show** to ensure the **powerState** is **VM deallocated**.

    >**Did you know?** When you use Azure to stop your virtual machine, the status is *deallocated*. This means that any non-static public IPs are released, and you stop paying for the VM’s compute costs.
