import requests
import json
from todoist_api_python.api import TodoistAPI

with open('___PATH TO FILE___', 'r+') as f:
    content = f.read()
    f.seek(0, 0)
    
    # api call - get all of today's tasks from todoist
    url = 'https://api.todoist.com/rest/v2/tasks'
    api_token = '___API TOKEN___'
    headers = {
        'Authorization': f'Bearer {api_token}'
    }
    params = {
        'filter': 'today'
    }
    response = requests.get(url, headers=headers, params=params)
    
    # If succesful
    if response.status_code == 200:
        todoistData = response.json()
        
        # writes the todoist content in a format that works in logseq
        for todo in todoistData:
            f.write("- " + todo['content'] + "\n")
        f.write("\n- \n" + content)
        
        # when completed, marks the tasks as done in todoist
        api = TodoistAPI(api_token)
        for todo in todoistData: 
            try:
                is_success = api.close_task(todo['id'])
            except Exception as error:
                print(error)
                
    else:
        print(response)
