import pandas as pd
import os
from dotenv import load_dotenv


def main():
    load_dotenv()
    file = os.environ["INPUT"]
    
    os.system("bw sync")
    os.system(f"bw export --output {file} --format csv")
    return


    
    
    # Correct the order of data
    
    data = pd.read_csv(file)
    data["empty1"]=""
    data["empty2"]=""
    
    
    column_titles=["folder","empty1","login_username","login_password","login_uri","empty2","login_totp",]
    data=data.reindex(columns = column_titles)
    
    data.to_csv("/Users/Paco/db/Vault.csv",index=False)
    
    # Remove first line of the file
    
    with open(file,"r") as file_:
        lines = file_.readlines()
    
    with open(file,"w") as file_:
        file_.writelines(lines[1:])
    

if __name__=="__main__":
    main()
