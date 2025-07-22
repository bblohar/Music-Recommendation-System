🎶 Music Recommendation System
This project implements a basic music recommendation system with a Python Flask backend and an HTML/CSS/JavaScript frontend. It allows users to get song recommendations based on their preferences (genre, artist, keywords) and tracks their listening history.

✨ Features
Song Database: A simulated in-memory database of diverse songs, including a collection of popular Hindi tracks.

Genre & Artist Filtering: Get recommendations by specifying a preferred genre or artist.

Keyword/Mood Search: Find songs matching specific moods or keywords (e.g., "energetic," "romantic").

Listening History: Tracks recently played songs for each user (simulated).

User ID Simulation: Easily switch between simulated users to demonstrate personalized history and recommendations.

Responsive Frontend: A clean and responsive user interface built with Tailwind CSS.

Loading Indicators: Visual feedback during API calls.

🚀 Technologies Used
Backend:

Python 3.x

Flask: A lightweight WSGI web application framework.

Flask-CORS: For handling Cross-Origin Resource Sharing, allowing the frontend to communicate with the backend.

Frontend:

HTML5

CSS3 (Tailwind CSS for utility-first styling)

JavaScript (ES6+)

📦 Setup and Installation
Follow these steps to get the Music Recommendation System up and running on your local machine.

1. Backend Setup
Clone the Repository (or create the project structure):
If you haven't already, create a directory for your project (e.g., MusicRecommender).

mkdir MusicRecommender
cd MusicRecommender

Create app.py:
Create a file named app.py inside the MusicRecommender directory and paste the Python backend code (provided in the previous responses) into it.

Install Python Dependencies:
Open your terminal or command prompt and navigate to your project directory:

cd D:\project\Music system\ # Or wherever your project is located

Install the required Python packages:

pip install Flask Flask-CORS

Run the Backend Server:
In the same terminal, start the Flask application:

python app.py

You should see output similar to this, indicating the server is running:

 * Serving Flask app 'app'
 * Debug mode: on
...
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit

Keep this terminal window open and running while you use the frontend.

2. Frontend Setup
Create index.html:
Create a file named index.html in the same directory as your app.py (MusicRecommender/index.html). Paste the HTML/CSS/JavaScript frontend code (provided in the previous responses) into this file.

Open in Browser:

Navigate to your project directory (D:\project\Music system\) in your file explorer.

Double-click index.html. This will open the application in your default web browser.

Recommended for Development: If you use Visual Studio Code, you can install the "Live Server" extension. Then, right-click on index.html in VS Code's Explorer and select "Open with Live Server". This provides a local development server and automatically reloads the page on changes.

💡 Usage
Set User ID: Enter a user ID (e.g., user123 or guest_user) in the input field. This simulates different user profiles.

Get Recommendations:

Select a Genre from the dropdown.

Enter an Artist name.

Type Mood/Keywords (e.g., "energetic", "romantic", "dance").

Click "Find My Music!" to get personalized recommendations.

View All Songs: The "All Available Songs" section displays the entire catalog.

Record Listening History: Click the "Listen" button on any song in the "Recommended For You" or "All Available Songs" sections to add it to your listening history.

View History: Your "Your Listening History" section will update automatically after you listen to songs.

🚀 Future Enhancements (Towards a Spotify/Resso-like App)
This project serves as a foundational step. To evolve it into a more comprehensive music application like Spotify or Resso, consider implementing the following:

Actual Audio Streaming: Store and stream real audio files.

User Authentication: Implement secure user registration and login.

Persistent Database: Replace in-memory data with a robust database (e.g., PostgreSQL, MongoDB).

Advanced Recommendation Algorithms: Explore collaborative filtering, content-based filtering, or hybrid models.

Playlist Management: Allow users to create, save, edit, and share custom playlists.

Robust Search: Implement advanced search functionalities with various filters.

Rich UI/UX: Enhance the visual design with album art, artist profiles, and more interactive elements.

User Library: Sections for liked songs, saved albums, and followed artists.
