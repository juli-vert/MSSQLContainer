# MSSQLContainer
How to deploy MS SQL container with the required database schema  
How to import and retrieve data using pandas as driver  

## CSV takeng from: 
https://people.sc.fsu.edu/~jburkardt/data/csv/csv.html

## Usage
git clone https://github.com/julivert82/MSSQLContainer  
cd Docker  
docker build -t jmssql .  
docker run -e "ACCEPT_EULA=Y" -e "SA_PASSWORD=Julivert82" -p 1433:1433 --name sql1 -d jmssql  

## Access the contained console
docker exec -it sql1 /bin/bash  

## Connect to the local SQL Server
/opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P Julivert82  

## Python module
pip install -r requirements.txt
> from msparser import Parser  
p = Parser()  
p.parse() #insert data  
p.getQuery() #retrieve data  
