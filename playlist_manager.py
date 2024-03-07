import json

def load_data():
  try:
    with open('playlist.txt', 'r') as file:
      return json.load(file)
  except FileNotFoundError:
    return []

def save_data(videos):
  with open('playlist.txt', 'w') as file:
    json.dump(videos, file)

def list_all_videos(videos):
  print("\n")
  print("*" * 90)
  print("\n")
  for index, vedio in enumerate(videos, start = 1):
    print(f"{index}. {vedio['Name']}, Time needed: {vedio['Time']}, Link: {vedio['Link']}")
  print("\n")
  print("*" * 70)

def add_video(videos):
  name = input("Enter vedio name: ")
  link = input("Enter vedio link: ")
  time = input("Enter length of vedio: ")

  videos.append({'Name': name, 'Link': link, 'Time': time})
  save_data(videos)

def update_video(videos):
  list_all_videos(videos)
  toUpdate = int(input("Please enter the the vedio you want to update: "))
  if(toUpdate < 1 or  toUpdate > len(videos)):
    print("Invalid selection! Please select a valid number")
  else:
    newName = input("Enter the new name: ")
    newLink = input("Enter the new link: ")
    newTime = input("Enter the new time: ")
    videos[toUpdate - 1] = {'Name': newName, 'Time': newTime, 'Link': newLink}
    save_data(videos)
    print("\n")
    print("VEDIO DELETED SUCCESSFULLY!")
  print("\n")
  print("*" * 70)

def delete_video(videos):
  list_all_videos(videos)
  toDelete = int(input("Please enter the the vedio you want to delete: "))
  if(toDelete < 1 or  toDelete > len(videos)):
    print("Invalid selection! Please select a valid number")
  else:
    del videos[toDelete - 1]
    save_data(videos)
    print("\n")
    print("VEDIO DELETED SUCCESSFULLY!")
  print("\n")
  print("*" * 70)

def main(): 

  videos = load_data()

  while True:
    print("\n PLAYLIST MANAGER")
    print("\n Please choose any option: ")
    print("1 - List all youtube vedios")
    print("2 - Add a youtube vedio")
    print("3 - Update vedio detials")
    print("4 - Delete a youtube vedio")
    print("5 - Exit the app")

    userChoice = input("Enter your choice: ")

    match userChoice:
      case "1":
        list_all_videos(videos)
      
      case "2":
        add_video(videos)

      case "3":
        update_video(videos)

      case "4":
        delete_video(videos)

      case "5":
        break

      case _:
        print("Invalid Option! Try again.")

if __name__ == "__main__":
  main()