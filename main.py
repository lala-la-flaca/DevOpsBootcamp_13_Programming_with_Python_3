import requests

response = requests.get("https://gitlab.com/api/v4/users/techworld-with-nana/projects")
#print(response.json())
#print(type(response.json()))

my_projects =  response.json()

for project in my_projects:
    project_name = project["name"]
    print(f"Project name: {project_name}")
    project_url = project["web_url"]
    print(f"Project URL: {project_url}")




