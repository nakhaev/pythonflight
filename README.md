# Python Flight Project

A Python project with proper virtual environment setup and dependency management.

## Setup Instructions

### Prerequisites
- Python 3.x installed on your system
- Git (optional, for version control)

### Getting Started

1. **Clone the repository** (if using Git):
   ```bash
   git clone <repository-url>
   cd pythonflight
   ```

2. **Create and activate virtual environment**:
   ```bash
   # Create virtual environment
   python3 -m venv venv
   
   # Activate virtual environment
   # On Linux/macOS:
   source venv/bin/activate
   
   # On Windows:
   # venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   python main.py
   ```

### Development

#### Adding New Dependencies
When you install new packages, update the requirements file:
```bash
pip install package_name
pip freeze > requirements.txt
```

#### Deactivating Virtual Environment
When you're done working:
```bash
deactivate
```

### Project Structure
```
pythonflight/
├── venv/              # Virtual environment (ignored by Git)
├── main.py           # Main application file
├── requirements.txt  # Python dependencies
├── .gitignore       # Git ignore patterns
└── README.md        # This file
```

### Notes
- The virtual environment (`venv/`) is excluded from version control
- Always activate the virtual environment before working on the project
- Keep `requirements.txt` updated when adding new dependencies