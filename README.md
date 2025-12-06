# siem-dataset-importer

Python tool for importing security datasets into SIEM platforms to support threat hunting, detection engineering, and hands-on learning in a homelab environment.

![Dataset Preview 1](https://drive.google.com/uc?export=view&id=1CLmGcmJp1F4TRzfy9xSPsGU1WpLvrfG7)
![Dataset Preview 2](https://drive.google.com/uc?export=view&id=1hBBr_eTXYSExOjv-vsB4IglsjUM0Zrng)

# How To Use The Script

## Importing Data to Elastic

### **Step 1 — Choose Elastic and JSON File Path**
Start the script and select **option 1** to choose Elastic.

![Screenshot 1](https://drive.google.com/uc?export=view&id=1C7w-XyxTpApjS2-Qbs33awHkAZJ9V7cG)

### **Step 2 — Enter SIEM IP and Port**
Enter your SIEM server's IP address and (usually) the default port.

![Screenshot 2](https://drive.google.com/uc?export=view&id=1gt1KNoH8KKxxsTui7kLl5sbYV4czitZz)

### **Step 3 — Enter Username and Password**
Type the Elastic username and password.

![Screenshot 3](https://drive.google.com/uc?export=view&id=1miI5P4pRTqc0Qq6OgMUJEC4paikH5CLe)

### **Step 4 — Enter Index Name**
Provide the target index name where the data will be stored.

![Screenshot 4](https://drive.google.com/uc?export=view&id=1_cX2ogLB2PU8A3nstBlxcfre45Q3kD-l)

### **Optional — Check Index Information in Elastic**
If you are unsure about the index name or want to verify it:

#### Step 1 — Open Elastic Stack Management
Go to **Stack Management** → **Index Management**.

![Screenshot 5](https://drive.google.com/uc?export=view&id=1JMEcJvdAXPLP1DeBRqmQHIkEc5xftNO2)

#### Step 2 — View Index Details
Click on the index you want to inspect. You will see detailed information about it:

![Screenshot 6](https://drive.google.com/uc?export=view&id=1BHWoaapdNczDps1JjNds759LhQTwVbDo)

![Screenshot 7](https://drive.google.com/uc?export=view&id=1MHhxXT2nwR_60esQAb1KEN1XyyKGFE9S)

![Screenshot 8](https://drive.google.com/uc?export=view&id=1JaLLXi_aIOoWyIZYR2gRXd1lZa18mtCO)

After all inputs are provided, the script will process the data and confirm everything is ready.

---

## Importing Data to Splunk

### **Step 1 — Choose Splunk**
Start the script and select **option 2** to choose Splunk.

### **Step 2 — Enter JSON File Path**
Provide the full path to the **JSON** file you want to import.

### **Step 3 — Enter Splunk IP**
Type the IP address of your Splunk server.

### **Step 4 — Keep Default HEC Port**
Leave the **HEC port** as default (**8088**) — do **not** change it.

![Screenshot 10](https://drive.google.com/uc?export=view&id=1A1LEKxL2FPxKTF109MczJnXdYiKtpll8)

### **Step 5 — Choose HTTPS**
Type `y` to enable **HTTPS** for the connection.

![Screenshot 11](https://drive.google.com/uc?export=view&id=1owjf01vuT5x1OHRoZNY8Qca7GTOtKQbB)

### **Step 6 — Get HEC Token**
To authenticate the import, you need a **HEC token**:

1. Open **Splunk → Settings → Data Inputs**.
    

![[99 - Meta/attachments/Screenshot_13.png]]

2. Open **HTTP Event Collector**.
    

![[99 - Meta/attachments/Screenshot_14.png]]

3. Create a **New Token** and give it a name.
    

![[Screenshot_16.png]]

4. Keep it **automatic** and submit.
    
5. Copy the generated token and paste it in the script terminal.
    

![[99 - Meta/attachments/Screenshot_18.png]]

### **Step 7 — Create Index**

1. Go to **Settings → Indexes**.
    

![[99 - Meta/attachments/Screenshot_20.png]]

2. Create a **New Index**.
    

![[99 - Meta/attachments/Screenshot_21.png]]

3. Name it the same as the one you will provide for the script.
    

![[Screenshot_22 1.png]]

---

## **Conclusion**

Once all steps are completed, your JSON dataset will be successfully imported into **Elastic** or **Splunk**, and the indexes are ready to use. The script handles the process automatically, making it fast and reliable.
