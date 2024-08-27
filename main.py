from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app=FastAPI()

class Blog(BaseModel):
    title:str 
    body:str 
    published:Optional[bool]=False

@app.get('/blog')
def about():
    return {'data':{'message':'About Page'}}

@app.get('/blog/{id}')
def getBlog(id:int):
    return {'message':f'blog {id} returned!','data':id}

@app.get('/')
def server():
    return {'data':{'message':'Hello from server'}}

@app.post('/blog/create')
def createBlog(blog:Blog):
    return {'message':f"Blog {blog.title} is Created","blog":blog}






if __name__ == "__main__":
    uvicorn.run(app,host='127.0.0.1',port=4000)