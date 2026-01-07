import requests


def get_user_id(username):
    """Get Roblox user ID from username using the updated API."""
    url = f"https://users.roblox.com/v1/users/search?keyword={username}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['data']:
            return data['data'][0]['id']  # Take the first matching user
    return None


def get_user_stats(user_id):
    """Fetch and print Roblox user stats: username, account created, friends, followers."""

    # Get basic info
    user_url = f"https://users.roblox.com/v1/users/{user_id}"
    user_resp = requests.get(user_url)

    if user_resp.status_code != 200:
        print("User not found or error occurred.")
        return

    user_data = user_resp.json()

    # Friends count
    friends_url = f"https://friends.roblox.com/v1/users/{user_id}/friends"
    friends_resp = requests.get(friends_url)
    friends_count = len(friends_resp.json().get('data', []))

    # Followers count
    followers_url = f"https://friends.roblox.com/v1/users/{user_id}/followers"
    followers_resp = requests.get(followers_url)
    followers_count = len(followers_resp.json().get('data', []))

    # Print stats
    print("\n--- Roblox User Stats ---")
    print(f"Username: {user_data['name']}")
    print(f"User ID: {user_data['id']}")
    print(f"Account Created: {user_data['created']}")
    print(f"Friends: {friends_count}")
    print(f"Followers: {followers_count}")
    print("-------------------------\n")


# Main program
if __name__ == "__main__":
    username = input("Enter Roblox username: ")
    user_id = get_user_id(username)

    if user_id:
        get_user_stats(user_id)
    else:
        print("Username not found.")
