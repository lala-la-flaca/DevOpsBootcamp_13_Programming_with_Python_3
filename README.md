# 🐍Module 13 – Programming with Python
This exercise is part of Module 13: Programming with Python, module introduces Python programming fundamentals through three hands-on demo projects. Each demo focuses on solving a different type of problem: a countdown application, automation with spreadsheets, and interacting with an external API.

# 📦Demo 3 – API request to Gitlab
# 📌 Objective
Write a Python application that interacts with GitLab’s API to list all public repositories for a specified user.

# 🚀 Technologies Used
* Python: programming language.
* IntelliJ-PyCharm: IDE used for development.
* GitLAB API
  
# 🎯 Features
✅ Sends requests to GitLab’s API.

📡 Retrieves public repositories for a given user.

📋 Displays repository names in the console

# 🏗 Project Architecture

# ⚙️ Project Configuration
1. Create a new Python file named GitLabRepo.
2. Install the requests module.
   ```bash
   pip install requests
   ```
3. Import the requests module to work with HTTP.
   ```bash
   import requests
   ```
   <img src="https://github.com/lala-la-flaca/DevOpsBootcamp_13_Programming_with_Python_3/blob/main/Img/importing%20module.PNG" width=800 />
   
4. Call the GitLab API and save the response.
   
    ```bash
    response = requests.get("https://gitlab.com/api/v4/users/techworld-with-nana/projects")
   ```
   <img src="https://github.com/lala-la-flaca/DevOpsBootcamp_13_Programming_with_Python_3/blob/main/Img/saving%20resposne%20form%20api.PNG" width=800 />
   
5. Decode the JSON response into a Python object.
    ```bash
    my_projects =  response.json()
   ```
   <img src="https://github.com/lala-la-flaca/DevOpsBootcamp_13_Programming_with_Python_3/blob/main/Img/parsin%20reponse%20to%20json.PNG" width=800 />
   
6. Iterate through the response to obtain the public repositories.
    ```bash
    for project in my_projects:
      project_name = project["name"]
      print(f"Project name: {project_name}")
      project_url = project["web_url"]
      print(f"Project URL: {project_url}")
   ```
   <img src="https://github.com/lala-la-flaca/DevOpsBootcamp_13_Programming_with_Python_3/blob/main/Img/getting%20porject.PNG" width=800 />
   
10. Output the results.

    <img src="https://github.com/lala-la-flaca/DevOpsBootcamp_13_Programming_with_Python_3/blob/main/Img/results.PNG" width=800/>
