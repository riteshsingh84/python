# This demo project is to show how to create a movie schedule using Python.

# Description: A simple movie schedule management system that allows adding, removing, and displaying movies in a schedule.

# Dictionary to store movie schedules with date as key and list of movies as value
movie_schedule = {"The Dark Knight": "11:00 am",
                "Inception": "2:00 pm", 
                "Interstellar": "5:00 pm",
                "The Matrix": "8:00 pm"}

# Function to add a movie to the schedule
# It checks if the movie is already scheduled and adds it if not
def add_movie(movie_name, time):
    """Add a movie to the schedule."""
    if movie_name in movie_schedule:
        print(f"{movie_name} is already scheduled at {movie_schedule[movie_name]}.")
    else:
        movie_schedule[movie_name] = time
        print(f"{movie_name} has been added to the schedule at {time}.")

# Function to display the current movie schedule
# It checks if the schedule is empty and displays the movies with their scheduled times
def display_schedule(): 
    """Display the current movie schedule."""
    if not movie_schedule:
        print("No movies scheduled.")
    else:
        print("Current Movie Schedule:")
        for movie, time in movie_schedule.items():
            print(f"{movie} at {time}")  

# Function to remove a movie from the schedule
# It checks if the movie exists in the schedule and removes it if found
def remove_movie(movie_name):
    """Remove a movie from the schedule."""
    if movie_name in movie_schedule:
        del movie_schedule[movie_name]
        print(f"{movie_name} has been removed from the schedule.")
    else:
        print(f"{movie_name} is not in the schedule.")

# Function to display the schedule of a specific movie
# It prompts the user to enter a movie name and displays its scheduled time if it exists
def display_movie_schedule():
    """Display the current movie schedule."""
    if not movie_schedule:
        print("No movies scheduled.")   
    else:
        print("Current Movie Schedule:")
        movie = input("Enter the movie name to display its schedule: ")
        if movie in movie_schedule:
            print(f"{movie} is scheduled at {movie_schedule.get(movie)}.")   
        else:
            print(f"{movie} is not in the schedule.")      

def main():     
    """Main function to run the movie schedule management system."""
    while True:
        print("\nMovie Schedule Management System")
        print("1. Add Movie")
        print("2. Display Schedule")
        print("3. Remove Movie")
        print("4. Show Movie Schedule of a Specific Movie")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            movie_name = input("Enter movie name: ")
            time = input("Enter movie time (e.g., 11:00 am): ")
            add_movie(movie_name, time)
        elif choice == '2':
            display_schedule()
        elif choice == '3':
            movie_name = input("Enter movie name to remove: ")
            remove_movie(movie_name)
        elif choice == '4':
            display_movie_schedule()
            break
        elif choice == '5':
            print("Exiting the Movie Schedule Management System.")
            break
        else:
            print("Invalid choice. Please try again.")
                  

main()  # Call the main function to start the program