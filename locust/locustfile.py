from locust import task, run_single_user
from locust import FastHttpUser


class php_app_mod_dev_399807308626_us_central1_run_app(FastHttpUser):
    @task
    def login(self):
        with self.client.request(
            "POST",
            "/login.php",
            headers={
                "content-type": "application/x-www-form-urlencoded",
                "origin": "https://php-app-mod-dev-399807308626.us-central1.run.app",
            },
            data="username=locust&password=Test%40123",
            catch_response=True,
        ) as response:
            if response.status_code != 200:
                print(f"Error: Login failed. Status code: {response.status_code}")
        
    @task
    def view_login_page(self):
        with self.client.request("GET", "/login.php", catch_response=True) as response:
            if response.status_code != 200:
                print(f"Error: Login page failed to load. Status code: {response.status_code}")
    @task
    def upload_image(self):
        with self.client.request(
            "POST",
            "/upload.php",
            data='------WebKitFormBoundaryGlJJARqn8ETjVnIm\r\nContent-Disposition: form-data; name="image"; filename="IMG_2380.jpeg"\r\nContent-Type: image/jpeg\r\n\r\n\r\n------WebKitFormBoundaryGlJJARqn8ETjVnIm--\r\n',
            catch_response=True,
        ) as response:
            if response.status_code == 200:
                print("Image uploaded successfully")
            else:
                print(f"Error: Image upload failed. Status code: {response.status_code}")


if __name__ == "__main__":
    run_single_user(php_app_mod_dev_399807308626_us_central1_run_app)
