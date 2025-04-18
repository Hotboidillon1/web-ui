import importlib
import pkg_resources
import sys

def check_dependencies():
    required_packages = [
        'gradio', 
        'playwright', 
        'browser_use', 
        'langchain', 
        'openai'
    ]

    print(f"Python Version: {sys.version}")
    print("\nChecking Dependencies:")
    
    for package in required_packages:
        try:
            # Try to import the package
            module = importlib.import_module(package)
            
            # Try to get the version
            try:
                version = pkg_resources.get_distribution(package).version
                print(f"{package}: Installed (Version {version})")
            except pkg_resources.DistributionNotFound:
                print(f"{package}: Imported but version unknown")
        
        except ImportError:
            print(f"{package}: NOT INSTALLED")

if __name__ == '__main__':
    check_dependencies()
