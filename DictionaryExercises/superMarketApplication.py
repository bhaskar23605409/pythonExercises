supermarket = {
    'store1':{
        'name':'Bhaskar Grocery Stotre',
        'items':[
            {'name':'soap','quantity':2},
            {'name':'brush','quantity':30},
            {'name':'pen','quantity':40}
        ]
    },
    'store2':{
        'name':"Books Store",
        'items':[
            {'name':'python','quantity':5},
            {'name':'django','quantity':6},
            {'name':'java','quantity':7}

        ]
    }
}


print(supermarket['store1']['name'])
print(supermarket['store1']['items'][0]['name'])
print(supermarket['store1']['items'][2]['quantity'])