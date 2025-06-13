# Python Selenium Cucumber BDD Automation Project

## 🚀 Project Setup

1. **Clone the repository**
   ```bash
   git clone <REPOSITORY_URL>
   cd desafio-qa-web
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .env
   ```

3. **Activate the virtual environment**
   - On Windows:
     ```bash
     .env\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source .env/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Configure environment variables**
   - Edit the `.env` file and add the necessary configurations for your environment, access keys, etc.

## 🔄 WebDriver Manager

This project uses `webdriver-manager` to automatically manage the browser drivers required for Selenium.

## 🧪 Running Tests

To run the tests, use the following command:

```bash
python run.py
```

## 📊 Reports

Test reports will be automatically generated after execution. Check the console output for details about each executed scenario.

## 📁 Project Structure

- **features/**: Contains feature definitions and step definitions for BDD tests.
- **data**: Contains test data files.
- **pages/**: Contains Page Object classes for user interface interaction.
- **utils/**: Contains utilities such as configuration and logging.
- **.env**: Environment variables for project configuration.
- **requirements.txt**: Project dependencies list.
- **.gitignore**: Files and folders to be ignored by Git.
- **README.md**: Project documentation.
- **run.py**: Entry point for test execution.

## 📌 Final Notes

Make sure all libraries are up to date and the environment is properly configured before running the tests. For more information about each library, please refer to the official documentation.