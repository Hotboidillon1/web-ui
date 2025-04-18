import sys
import os

def verify_project_setup():
    print("Python Executable:", sys.executable)
    print("Current Working Directory:", os.getcwd())
    
    # Check critical files
    critical_files = [
        'webui.py',
        'requirements.txt',
        '.env'
    ]
    
    print("\nChecking Critical Files:")
    for file in critical_files:
        if os.path.exists(file):
            print(f"{file}: EXISTS")
        else:
            print(f"{file}: MISSING")
    
    # Check virtual environment
    print("\nVirtual Environment:")
    print("Is Virtual Env Active:", hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix))

    # Import checks
    print("\nImport Checks:")
    try:
        import gradio
        print("Gradio: Importable")
    except ImportError:
        print("Gradio: IMPORT FAILED")
    
    try:
        import browser_use
        print("Browser Use: Importable")
    except ImportError:
        print("Browser Use: IMPORT FAILED")

if __name__ == '__main__':
    verify_project_setup()
