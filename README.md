   <h1>Playlist-Generator-CLI</h1>
    <p>A command-line utility that combines OpenAI's GPT-3.5 model and Spotify's API to generate personalized playlists based on user-defined prompts and create them directly in Spotify. This project allows you to generate a playlist of songs by providing a simple text prompt and create it on your Spotify account.</p>
    <h2>Features:</h2>
    <ul>
        <li><strong>Generate playlists</strong>: Uses OpenAI's GPT-3.5 model to generate a list of songs based on a text prompt.</li>
        <li><strong>Spotify integration</strong>: Automatically adds generated songs to a private Spotify playlist.</li>
        <li><strong>Command-line interface</strong>: Simple and user-friendly CLI to interact with the app.</li>
        <li><strong>Customizable options</strong>: Specify the number of songs and the prompt for the playlist.</li>
    </ul>
    <h2>Installation</h2>
    <h3>Requirements:</h3>
    <ul>
        <li>Python 3.11 or higher</li>
        <li>Spotify Developer account and OpenAI API key</li>
    </ul>
    <h3>Steps to get started:</h3>
    <ol>
        <li>Clone this repository:
            <pre><code>git clone https://github.com/wasayfaizan/Playlist-Generator-CLI.git</code></pre>
        </li>
        <li>Install dependencies:
            <pre><code>pip install -r requirements.txt</code></pre>
        </li>
        <li>Set up your environment variables by creating a <code>.env</code> file with the following keys:
            <ul>
                <li><code>OPEN_AI_KEY</code>: Your OpenAI API key</li>
                <li><code>SPOTIFY_CLIENT_ID</code>: Your Spotify Client ID</li>
                <li><code>SPOTIFY_CLIENT_SECRET</code>: Your Spotify Client Secret</li>
            </ul>
            Example <code>.env</code> file:
            <pre><code>OPEN_AI_KEY=your_openai_api_key
SPOTIFY_CLIENT_ID=your_spotify_client_id
SPOTIFY_CLIENT_SECRET=your_spotify_client_secret</code></pre>
        </li>
        <li>Run the script with the following command:
            <pre><code>python app.py -p "epic workout songs" -n 10</code></pre>
            <ul>
                <li><code>-p</code> is the prompt describing the playlist (e.g., "epic workout songs").</li>
                <li><code>-n</code> is the number of songs to generate (default is 10).</li>
            </ul>
        </li>
    </ol>
    <h2>How it Works:</h2>
    <ol>
        <li><strong>User Input</strong>: The user provides a prompt (e.g., "epic workout songs") and the number of songs they want in the playlist.</li>
        <li><strong>OpenAI GPT-3.5</strong>: The prompt is sent to OpenAI's GPT-3.5 model, which generates a list of song titles and artists.</li>
        <li><strong>Spotify Integration</strong>: The script then searches for these songs on Spotify and adds them to a newly created playlist on the user's account.</li>
    </ol>
    <h2>Error Handling:</h2>
    <p>If a song can't be found on Spotify, the script will log a warning and skip that song. The script will provide an error message if there is an issue with the OpenAI or Spotify API.</p>
    
</body>
</html>
