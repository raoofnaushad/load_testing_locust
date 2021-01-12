from locust import HttpUser, task, between

class WebsiteTestUser(HttpUser):
    wait_time = between(0.5, 3.0)

    def on_start(self):
        data = {"email" : "raoof@raoof.com", "password" : "iamraoof"}
        response = self.client.post("http://localhost:5000/login", data).json()
        self.token = {"x-access-token" : response["token"]}

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """
        pass
 
    @task(1)
    def hello_world(self):
        self.client.get("http://localhost:5000", headers=self.token)
        
        
    @task(2)
    def poster(self):    
        self.client.post("http://localhost:5000/posting",
                         json= {"content" : "2"}, headers=self.token)
