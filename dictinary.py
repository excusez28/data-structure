student_data = {'id1':
    {'name' : ['Maisa'],
     'class' : ['viii'],
     'suubject_integration' : ['bangla,english,science']
    },
'id2':
    {'name' : ['David'],
     'class' : ['v'],
     'suubject_integration' : ['bangla,english,science']
    },
'id3':
    {'name' : ['Maisa'],
     'class' : ['viii'],
     'suubject_integration' : ['bangla,english,science']
    },
'id4':
    {'name' : ['Surya'],
     'class' : ['v'],
     'suubject_integration' : ['bangla,english,science']
    },

}

result = {}

for key,value in student_data.items():
    if value not in result.values():
        result[key] = value
print(result)
    
    
    
    