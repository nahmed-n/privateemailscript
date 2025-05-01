import subprocess
import os
import sys
from pathlib import Path
from workers import Response
import json

#Wrangler Process ##
def check_wrangler_installation():
    try:
        subprocess.run(['wrangler', '--version'], check=True, capture_output=True)
        return True
    except (subprocess.SubprocessError, FileNotFoundError):
        return False

def install_wrangler():
    print("Installing Wrangler CLI...")
    subprocess.run(['npm', 'install', '-g', 'wrangler'], check=True)

def deploy_worker():
    try:
        # Check if we're in the correct directory
        if not os.path.exists('wrangler.toml'):
            print("Error: wrangler.toml not found. Please run this script from the project root directory.")
            sys.exit(1)

        # Deploy the worker
        print("Deploying worker to Cloudflare...")
        result = subprocess.run(['wrangler', 'deploy'], check=True, capture_output=True, text=True)
        print(result.stdout)
        
        if result.returncode == 0:
            print("✅ Deployment successful!")
        else:
            print("❌ Deployment failed!")
            print(result.stderr)
            
    except subprocess.SubprocessError as e:
        print(f"Error during deployment: {str(e)}")
        sys.exit(1)

def main():
    print("🚀 Starting deployment process...")
    
    # Check if Wrangler is installed
    if not check_wrangler_installation():
        print("Wrangler CLI not found. Installing...")
        install_wrangler()
    
    # Deploy the worker
    deploy_worker()

if __name__ == "__main__":
    main()

##JSCON File For Emails##

with open("csvjson.json", "r") as f:
    data = json.load(f)



## Setting up the JSON file##

async def on_fetch(request):
    name = (await request.json()).name
    return Response(json.dumps(data), headers={"Content-Type": "application/json"})

