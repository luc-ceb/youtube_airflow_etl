## Project 
![project diagram ](/images/diagrama_proyecto.png)
## AWS deployment:
1. Create a EC2 instance:
	- Ubuntu 22.04 LTS.
	- Type: t3.medium.
	- Get the key pair and save credentials on project folder.
	- Allow SSH and HTTPs traffic.
2. Connect to the instance:
	- Using a ssh client.
	- Run the followings commands:
		- sudo apt-get update
		- sudo apt install python3-pip
		- sudo pip install apache-airflow
		- sudo pip install pandas
		- sudo pip install s3fs
3. Make sure airflow is correctly installed running airflow , to initialize the airflow server run airflow standalone(copy airflow user and password).
4. Copy public IPv4 DNS and add :8080 (airflow port).
Configure security groups -> Inbound rules -> Add rule -> Type All traffic,  My Ip or Anywhere - IPv6
![project diagram ](/images/editar_regla_entradas.png)
![project diagram ](/images/grupos_de_seguridad.png)
5. Put a ETL into a python function.
6. Create a youtube_dag_etl.py
7. Create a s3 bucket:
	- Add a path into a ETL function on python. (s3://bucket-name)
8. In another terminal:
	- cd airflow
	- sudo nano airflow.cfg
	- modify dags_folder: /dags -> /youtube_dags
	- mkdir youtube_dags
	- copy airflow_youtube_etl.py and youtube_dag_etl.py on youtube_dags folder with: sudo nano airflow_youtube_etl.py and same with youtube_dag_etl.py.
9. Make sure that path on airflow.cfg is the same folder where are the dags, airflow/youtube_dags.
10. IPv4 DNS and add :8080 (airflow port). Run dags.
	- If we dont have permissions (log error:An error occurred (AccessDenied) when calling the CreateBucket operation: Access Denied)create new IAM role, with EC2FullAccess and S3FullAccess.
![project diagram ](/images/modificar_rol_iam.png)
11. Run the dag and should be success. 
![project diagram ](/images/bucket.png)
