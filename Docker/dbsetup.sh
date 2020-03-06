sleep 30s
/opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P Julivert82 -d master -i dbsetup.sql

#To Import data
# NOTE: If required disable constraints
# EXEC sp_MSforeachtable "ALTER TABLE ? NOCHECK CONSTRAINT all"
#/opt/mssql-tools/bin/bcp faithful.dbo.geysers in "/tmp/data.csv" -c -t',' -S localhost -U sa -P Julivert82
# enable constraints
# exec sp_MSforeachtable "ALTER TABLE ? WITH CHECK CHECK CONSTRAINT all"