from locust import HttpUser, task, between

class WebsiteTestUser(HttpUser):
    wait_time = between(0.5, 3.0)

    def on_start(self):
        """ on_start is called when the TaskSet is starting """
        pass

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """
        pass
 
    @task(1)
    def hello_world(self):
        self.client.get("http://localhost:5000")
        
        
    @task(2)
    def poster(self):    
        self.client.post("http://localhost:5000/posting",
                         json= {"content" : "2"})
