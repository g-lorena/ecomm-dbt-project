from dbt.cli.main import dbtRunner, dbtRunnerResult
import os
# when working locally
#project_dir = os.getcwd()

# initialize
dbt = dbtRunner()
#/Users/lgongang/Documents/personel/dbt_training/e_commerce

# create CLI args as a list of strings
cli_args = ["run", "--profiles-dir", "/usr"]

# run the command
res: dbtRunnerResult = dbt.invoke(cli_args)

# inspect the results
for r in res.result:
    print(f"{r.node.name}: {r.status}")