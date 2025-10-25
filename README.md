# UDTech_demo
Technikal task for UDTech

⚙️ Requirements

Python ≥ 3.12

pip (Installed with Python)

Git

Linux

🚀 Steps to setup Environment:

0. Use Terminal for comands:

1. Clone Reposetory:

    git clone https://github.com/savchukura/UDTech_demo.git
    cd UDTech_demo

2. Install Deps:

2.1 Create Virtual Environment:

    python3 -m venv venv
    source venv/bin/activate

2.2 Update pip:

    python -m pip install --upgrade pip

2.3 Install Deps from requirements:

    pip install -r requirements.txt

2.4 Install Chromium browser:

    playwright install chromium --with-deps

🧰 3. Run Tests:

3.1for test running use:
    pytest tests

3.2 Or use Allure reporter:

    pytest --alluredir=allure-results

and after tests:

    allure serve allure-results

  
