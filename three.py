import requests

def fetch_random_user_freeapi():
    my_url =  "https://api.freeapi.app/api/v1/public/randomusers/user/random" #this is the url from where data to be fetched
    
    my_response = requests.get(my_url) #getrequest fetches full data (string format- though looks like dict/json)

    data = my_response.json() #convert to json format

    if data["success"] and "data" in data: #checking if success key is true and data not empty
        user_data = data["data"]
        username = user_data["login"]["username"]  
        country = user_data["location"]["country"]
        return username, country
    
    else: #if error in fetching data
        raise Exception("failed to fetch user data")
    
def main():
    try:
        username, country = fetch_random_user_freeapi()
        print(f"username: {username} \n country: {country}")
    except Exception as e:
        print(str(e))

if __name__ =="__main__":
    main()