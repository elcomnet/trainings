# Lab 06 - Network Connectivity

## Lab introduction

In this lab you explore communication between virtual networks. You implement virtual network peering and test connections. You will also create a custom route. 

## Estimated time: 50 minutes

## Task 1:  Create a core services virtual machine and virtual network

In this task, you create a core services virtual network with a virtual machine. 

1. Sign in to the **Azure portal** - `https://portal.azure.com`.

1. Search for and select `Virtual Machines`.

1. From the virtual machines page, select **Create** then select **Azure Virtual Machine**.

1. On the Basics tab, use the following information to complete the form, and then select **Next: Disks >**. For any setting not specified, leave the default value.
 
    | Setting | Value | 
    | --- | --- |
    | Subscription |  *your subscription* |
    | Resource group |  `workshop-X` (If necessary, **Create new**. )
    | Virtual machine name |    `vm-core-student-X` |
    | Region | (Europe) ** West/North Europe**  |
    | Availability options | No infrastructure redundancy required |
    | Security type | **Standard** |
    | Image | **Windows Server 2019 Datacenter: x64 Gen2** (notice your other choices) |
    | Size | **Standard_B2s** |
    | Authentication type | 'Password' |
    | Username | `localadmin` | 
    | Password | **Provide a complex password** |
    | Public inbound ports | **None** |

1. On the **Disks** tab take the defaults and then select **Next: Networking >**.

1. On the **Networking** tab, for Virtual network, select **Create new**.

1. Use the following information to configure the virtual network, and then select **Ok**. If necessary, remove or replace the existing information.

    | Setting | Value | 
    | --- | --- |
    | Name | `vnet_core_student_X` |
    | Address range | `10.Z.0.0/16` (Z = 20 + X)`  |
    | Subnet Name | `Core` | 
    | Subnet address range | `10.Z.0.0/24` |

1. Select the **Monitoring** tab. For Boot Diagnostics, select **Disable**.

1. Select **Review + Create**, and then select **Create**.

1. You do not need to wait for the resources to be created. Continue on to the next task.

    >**Note:** Did you notice in this task you created the virtual network as you created the virtual machine? You could also create the virtual network infrastructure then add the virtual machines. 

## Task 2: Create a virtual machine in a different virtual network

In this task, you create a manufacturing services virtual network with a virtual machine. 

1. From the Azure portal, search for and navigate to **Virtual Machines**.

1. From the virtual machines page, select **Create** then select **Azure Virtual Machine**.

1. On the Basics tab, use the following information to complete the form, and then select **Next: Disks >**. For any setting not specified, leave the default value.
 
    | Setting | Value | 
    | --- | --- |
    | Subscription |  *your subscription* |
    | Resource group |  `workshop-X` |
    | Virtual machine name |    `vm-manu-student-X` |
    | Region | (Europe) ** West/North Europe**  |
    | Security type | **Standard** |
    | Availability options | No infrastructure redundancy required |
    | Image | **Ubuntu Server 20.04 LTS - x64 Gen2** |
    | Size | **Standard_B1s** | 
    | Authentication type | 'Password' |
    | Username | `localadmin` | 
    | Password | **Provide a complex password** |
    | Public inbound ports | **None** |

1. On the **Disks** tab take the defaults and then select **Next: Networking >**.

1. On the Networking tab, for Virtual network, select **Create new**.

1. Use the following information to configure the virtual network, and then select **Ok**.  If necessary, remove or replace the existing address range.

    | Setting | Value | 
    | --- | --- |
    | Name | `vnet_manu_student_X` |
    | Address range | `172.Z.0.0/16` (Z = 16 + X)  |
    | Subnet Name | `Manufacturing` |
    | Subnet address range | `172.Z.0.0/24` |

1. Select the **Monitoring** tab. For Boot Diagnostics, select **Disable**.

1. Select **Review + Create**, and then select **Create**.

## Task 3: Use Network Watcher to test the connection between virtual machines 

In this task, you verify that resources in peered virtual networks can communicate with each other. Network Watcher will be used to test the connection. Before continuing, ensure both virtual machines have been deployed and are running. 

1. From the Azure portal, search for and select `Network Watcher`.

1. From Network Watcher, in the Network diagnostic tools menu, select **Connection troubleshoot**.

1. Use the following information to complete the fields on the **Connection troubleshoot** page.

    | Field | Value | 
    | --- | --- |
    | Source type           | **Virtual machine**   |
    | Virtual machine       | **vm-core-student-X**    | 
    | Destination type      | **Virtual machine**   |
    | Virtual machine       | **vm-manu-student-X**   | 
    | Preferred IP Version  | **Both**              | 
    | Protocol              | **TCP**               |
    | Destination port      | `3389`                |  
    | Source port           | *Blank*         |
    | Diagnostic tests      | *Defaults*      |

1. Select **Run diagnostic tests**.

    >**Note**: It may take a couple of minutes for the results to be returned. The screen selections will be greyed out while the results are being collected. Notice the **Connectivity test** shows **UnReachable**. This makes sense because the virtual machines are in different virtual networks. 

 
## Task 4: Configure virtual network peerings between virtual networks

In this task, you create a virtual network peering to enable communications between resources in the virtual networks. 

1. In the Azure portal, select the `vnet_core_student_X` virtual network.

1. In CoreServicesVnet, under **Settings**, select **Peerings**.

1. On CoreServicesVnet | Peerings, select **+ Add**.

1. Use the information in the following table to create the peering.

| **Parameter**                                    | **Value**                             |
| --------------------------------------------- | ------------------------------------- |
| **This virtual network**                                       |                                       |
| Peering link name                             | `CoreServicesVnet-to-ManufacturingVnet` |
| Allow CoreServicesVnet to access the peered virtual network            | selected (default)                       |
| Allow CoreServicesVnet to receive forwarded traffic from the peered virtual network | selected                       |
| Allow gateway in CoreServicesVnet to forward traffic to the peered virtual network | Not selected (default) |
| Enable CoreServicesVnt to use the peered virtual networks' remote gateway       | Not selected (default)                        |
| **Remote virtual network**                                   |                                       |
| Peering link name                             | `ManufacturingVnet-to-CoreServicesVnet` |
| Virtual network deployment model              | **Resource manager**                      |
| I know my resource ID                         | Not selected                          |
| Subscription                                  | *your subscription*    |
| Virtual network                               | **vnet_core_student_X**                     |
| Allow ManufacturingVnet to access CoreServicesVnet  | selected (default)                       |
| Allow ManufacturingVnet to receive forwarded traffic from CoreServicesVnet | selected                        |
| Allow gateway in CoreServicesVnet to forward traffic to the peered virtual network | Not selected (default) |
| Enable ManufacturingVnet to use CoreServicesVnet's remote gateway       | Not selected (default)                        |

1. Review your settings and select **Add**.

1. In CoreServicesVnet | Peerings, verify that the **CoreServicesVnet-to-ManufacturingVnet** peering is listed. Refresh the page to ensure the **Peering status** is **Connected**.

1. Switch to the **ManufacturingVnet** and verify the **ManufacturingVnet-to-CoreServicesVnet** peering is listed. Ensure the **Peering status** is **Connected**. You may need to **Refresh** the page. 


## Task 5: Use Azure PowerShell to test the connection between virtual machines

In this task, you retest the connection between the virtual machines in different virtual networks. 

### Verify the private IP address of the CoreServicesVM

1. From the Azure portal, search for and select the `vm-core-student-X` virtual machine.

1. On the **Overview** blade, in the **Networking** section, record the **Private IP address** of the machine. You need this information to test the connection.
   
### Test the connection to the vm-core-student-X from the **vm-manu-student-X**.

>**Did you know?** There are many ways to check connections. In this task, you use **Run command**. You could also continue to use Network Watcher. Or you could use a [Remote Desktop Connection](https://learn.microsoft.com/azure/virtual-machines/windows/connect-rdp#connect-to-the-virtual-machine) to the access the virtual machine. Once connected, use **test-connection**. As you have time, give RDP a try. 

1. Switch to the `vm-core-student-X` virtual machine.

1. In the **Operations** blade, select the **Run command** blade.

1. Select **RunPowerShellScript** and run the **Test-NetConnection** command. Be sure to use the private IP address of the **vm-core-student-X**.

    ```Powershell
    Test-NetConnection <vm-core-student-X private IP address> -port 3389
    ```
1. It may take a couple of minutes for the script to time out. The top of the page shows an informational message *Script execution in progress.*

   
1. The test connection should succeed because peering has been configured.

   
## Task 6: Create a custom route 

In this task, you want to control network traffic between the perimeter subnet and the internal core services subnet. A virtual network appliance will be installed in the core services subnet and all traffic should be routed there. 

1. Search for select the `vnet_core_student_X`.

1. Select **Subnets** and then **+ Create**. Be sure to **Save** your changes. 

    | Setting | Value | 
    | --- | --- |
    | Name | `perimeter` |
    | Subnet address range | `10.Z.1.0/24` (Z = 20 + X) |

   
1. In the Azure portal, search for and select `Route tables`, and then select **Create**. 

    | Setting | Value | 
    | --- | --- |
    | Subscription | your subscription |
    | Resource group | `workshop-X`  |
    | Region | (Europe) ** West/North Europe**  |
    | Name | `rt-CoreServices-student-X` |
    | Propagate gateway routes | **No** |

1. After the route table deploys, select **Go to resource**.

1. Select **Routes** and then **+ Add**. Create a route from the future NVA to the CoreServices virtual network. 

    | Setting | Value | 
    | --- | --- |
    | Route name | `PerimetertoCore` |
    | Destination type | **IP Addresses** |
    | Destination IP addresses | `10.Z.0.0/16` (core services virtual network) |
    | Next hop type | **Virtual appliance** (notice your other choices) |
    | Next hop address | `10.Z.1.7` (future NVA) |

1. Select **+ Add** when the route is completed. The last thing to do is associate the route with the subnet.

1. Select **Subnets** and then **Associate**. Complete the configuration.

    | Setting | Value | 
    | --- | --- |
    | Virtual network | **vnet_core_student_X** |
    | Subnet | **Core** |    
