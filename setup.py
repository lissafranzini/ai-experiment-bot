#!/usr/bin/env python3
"""
AI Learning Journey Setup Script

This script helps you set up your learning environment for the 30-day AI study plan.
Run this script to create virtual environments and install dependencies for each week.
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def run_command(cmd, cwd=None):
    """Run a shell command and return True if successful."""
    try:
        result = subprocess.run(
            cmd, 
            shell=True, 
            check=True, 
            cwd=cwd,
            capture_output=True, 
            text=True
        )
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        return False, e.stderr

def check_python_version():
    """Check if Python version is 3.8 or higher."""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Python 3.8 or higher is required")
        print(f"   Current version: {version.major}.{version.minor}.{version.micro}")
        return False
    
    print(f"✅ Python version: {version.major}.{version.minor}.{version.micro}")
    return True

def setup_git():
    """Initialize git repository if not already done."""
    if os.path.exists('.git'):
        print("✅ Git repository already initialized")
        return True
    
    print("🔧 Initializing Git repository...")
    
    commands = [
        "git init",
        "git add .",
        "git commit -m 'Initial commit: 30-day AI learning journey setup'"
    ]
    
    for cmd in commands:
        success, output = run_command(cmd)
        if not success:
            print(f"❌ Git command failed: {cmd}")
            print(f"   Error: {output}")
            return False
    
    print("✅ Git repository initialized")
    return True

def create_env_file():
    """Create .env file from template if it doesn't exist."""
    if os.path.exists('.env'):
        print("✅ .env file already exists")
        return True
    
    if not os.path.exists('templates/env-template.txt'):
        print("❌ Environment template not found")
        return False
    
    shutil.copy('templates/env-template.txt', '.env')
    print("✅ Created .env file from template")
    print("🔧 Please edit .env and add your API keys!")
    return True

def setup_week_environment(week_num):
    """Set up virtual environment and dependencies for a specific week."""
    week_dir = f"week-{week_num}"
    venv_name = f"ai-week-{week_num}"
    
    print(f"\n🔧 Setting up Week {week_num} environment...")
    
    # Check if requirements file exists
    req_file = f"{week_dir}/requirements.txt"
    if not os.path.exists(req_file):
        print(f"❌ Requirements file not found: {req_file}")
        return False
    
    # Create virtual environment
    print(f"   Creating virtual environment: {venv_name}")
    success, output = run_command(f"python -m venv {venv_name}")
    if not success:
        print(f"❌ Failed to create virtual environment")
        print(f"   Error: {output}")
        return False
    
    # Determine activation command based on OS
    if sys.platform == "win32":
        activate_cmd = f"{venv_name}\\Scripts\\activate"
        pip_cmd = f"{venv_name}\\Scripts\\pip"
    else:
        activate_cmd = f"source {venv_name}/bin/activate"
        pip_cmd = f"{venv_name}/bin/pip"
    
    # Install dependencies
    print(f"   Installing dependencies from {req_file}")
    success, output = run_command(f"{pip_cmd} install -r {req_file}")
    if not success:
        print(f"❌ Failed to install dependencies")
        print(f"   Error: {output}")
        return False
    
    print(f"✅ Week {week_num} environment ready!")
    print(f"   To activate: {activate_cmd}")
    return True

def create_weekly_readme(week_num):
    """Create a README file for each week if it doesn't exist."""
    week_dir = f"week-{week_num}"
    readme_path = f"{week_dir}/README.md"
    
    if os.path.exists(readme_path):
        return True
    
    readme_content = f"""# Week {week_num} - AI Learning Journey

## Overview
This week focuses on [week theme - update based on your plan].

## Setup
```bash
# Activate virtual environment
source ../ai-week-{week_num}/bin/activate  # macOS/Linux
# ..\\ai-week-{week_num}\\Scripts\\activate  # Windows

# Install dependencies
pip install -r requirements.txt
```

## Daily Progress
- [ ] Day {(week_num-1)*7 + 1}: [Topic]
- [ ] Day {(week_num-1)*7 + 2}: [Topic]
- [ ] Day {(week_num-1)*7 + 3}: [Topic]
- [ ] Day {(week_num-1)*7 + 4}: [Topic]
- [ ] Day {(week_num-1)*7 + 5}: [Topic]
- [ ] Day {(week_num-1)*7 + 6}: [Topic]
- [ ] Day {(week_num-1)*7 + 7}: [Topic]

## Projects
- Project descriptions and goals for this week

## Resources
- Links to helpful resources
- Documentation references
- Tutorials and guides

## Notes
Use the `notes/` directory to track daily learning notes.
"""
    
    with open(readme_path, 'w') as f:
        f.write(readme_content)
    
    return True

def main():
    """Main setup function."""
    print("🚀 AI Learning Journey Setup")
    print("=" * 40)
    
    # Check Python version
    if not check_python_version():
        return False
    
    # Create .env file
    if not create_env_file():
        return False
    
    # Initialize Git repository
    if not setup_git():
        return False
    
    # Setup each week's environment
    for week in range(1, 6):
        if not setup_week_environment(week):
            return False
        if not create_weekly_readme(week):
            print(f"❌ Failed to create README for week {week}")
    
    print("\n🎉 Setup Complete!")
    print("\nNext steps:")
    print("1. Edit .env file with your API keys")
    print("2. Start with week-1/notes/day-01-setup.md")
    print("3. Activate Week 1 environment:")
    
    if sys.platform == "win32":
        print("   ai-week-1\\Scripts\\activate")
    else:
        print("   source ai-week-1/bin/activate")
    
    print("\nHappy learning! 🤖✨")
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)