# Lab 04 - Implement Virtual Networking

## Lab introduction

In this lab, you learn the basics of virtual networking and subnetting. 

## Estimated time: 20 minutes

## Task 1: Create a virtual network with subnets using the portal

1. Sign in to the **Azure portal** - `https://portal.azure.com`.
   
1. Search for and select `Virtual Networks`.

1. Select **Create** on the Virtual networks page.

1. Complete the **Basics** tab for the CoreServicesVnet.  

	|  **Option**         | **Value**            |
	| ------------------ | -------------------- |
	| Resource Group     | `workshop-X |
	| Name               | `vnet_core_student_X`     |
	| Region             | (Europe) ** West/North Europe**         |

1. Move to the **IP Addresses** tab.

	|  **Option**         | **Value**            |
	| ------------------ | -------------------- |
	| IPv4 address space | `10.Z.0.0/16` (Z = 20 + X)    |

1. Select **+ Add a subnet**. Complete the name and address information for each subnet. Be sure to select **Add** for each new subnet. 

	| **Subnet**             | **Option**           | **Value**              |
	| ---------------------- | -------------------- | ---------------------- |
	| SharedServicesSubnet   | Subnet name          | `SharedServicesSubnet`   |
	|                        | Starting address		| `10.Z.10.0`          |
	|						 | Size					| `/24`	|
	| DatabaseSubnet         | Subnet name          | `DatabaseSubnet`         |
	|                        | Starting address		| `10.Z.20.0`        |
	|						 | Size					| `/24`	|

	>**Note:** Every virtual network must have at least one subnet. Reminder that five IP addresses will always be reserved, so consider that in your planning. 

1. To finish creating the CoreServicesVnet and its associated subnets, select **Review + create**.

1. Verify your configuration passed validation, and then select **Create**.

1. Wait for the virtual network to deploy and then select **Go to resource**.

1. Take a minute to verify the **Address space** and the **Subnets**. Notice your other choices in the **Settings** blade. 

1. In the **Automation** section, select **Export template**, and then wait for the template to be generated.

1. **Download** the template.

1. Navigate on the local machine to the **Downloads** folder and **Extract all** the files in the downloaded zip file. 

1. Before proceeding, ensure you have the **template.json** file. You will use this template to create the ManufacturingVnet in the next task. 
 
## Task 2: Create a virtual network and subnets using a template

In this task, you create the ManufacturingVnet virtual network and associated subnets. The organization anticipates growth for the manufacturing offices so the subnets are sized for the expected growth. For this task, you use a template to create the resources. 

1. Locate the **template.json** file exported in the previous task. It should be in your **Downloads** folder.

1. Edit the file using the editor of your choice. Many editors have a *change all occurrences* feature. If you are using Visual Studio Code be sure you are working in a **trusted window** and not in the **restricted mode**. Consult the architecture diagram to verify the details. 

### Make changes for the ManufacturingVnet virtual network

1. Replace all occurrences of **vnet_core_student_X** with `vnet_manu_student_X`. 

1. Replace all occurrences of **10.Z.0.0** with `10.Y.0.0`. (Y = 40 + X)

### Make changes for the ManufacturingVnet subnets

1. Change all occurrences of **SharedServicesSubnet** to `SensorSubnet1`.

1. Change all occurrences of **10.Z.10.0/24** to `10.Y.20.0/24`.

1. Change all occurrences of **DatabaseSubnet** to `SensorSubnet2`.

1. Change all occurrences of **10.Z.20.0/24** to `10.Y.21.0/24`.

1. Read back through the file and ensure everything looks correct.

1. Be sure to **Save** your changes.

>**Note:** There is a completed template files in the lab files directory. 

### Make changes to the parameters file

1. Locate the **parameters.json** file exported in the previous task. It should be in your **Downloads** folder.

1. Edit the file using the editor of your choice.

1. Replace all occurrences of **vnet_core_student_X** with `vnet_manu_student_X`. 

1. **Save** your changes.
   
### Deploy the custom template

1. In the portal, search for and select **Deploy a custom template**.

1. Select **Build your own template in the editor** and then **Load file**.

1. Select the **templates.json** file with your Manufacturing changes, then select **Save**.

1. Select **Review + create** and then **Create**.

1. Wait for the template to deploy, then confirm (in the portal) the Manufacturing virtual network and subnets were created.

>**Note:** If you have to deploy more than one time you may find some resources were successfully completed and the deployment is failing. You can manually remove those resources and try again. 
