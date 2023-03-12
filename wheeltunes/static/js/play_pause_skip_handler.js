var currentlyPlayingAudio = null;
var currentPlaylist = getAllCurrentSongs();
var currentPlaylistPosition = 0;

function togglePlayPause(action) {
    if (action === 'play') {
      playButton.style.display = 'none';
      pauseButton.style.display = 'inline-block';
      playSong();
    } else if (action === 'pause') {
      playButton.style.display = 'inline-block';
      pauseButton.style.display = 'none';
      pauseSong();
    }
}

function playSong() {
  // Play button is clicked. This should either:
  //      1. Play the first song after page load.
  //      2  OR -- play the previously paused song.
  if (currentlyPlayingAudio) {
    // Case 2
    currentlyPlayingAudio.play();
  } else {
    // Case 1
    firstSong = getAllCurrentSongs()[0];
    firstSong.play();
    currentlyPlayingAudio = firstSong;
  }
}

function pauseSong() {
  // Pauses the currently playing song.
  currentlyPlayingAudio.pause();
}

function getAllCurrentSongs() {
  // Gets all the current songs catered to current state.
  return $(".audio");
}

function setNowPlaying(title) {
  $("#now_playing_song").text(title);
}

function playNextSong() {
  // Skip button is pressed.
  updatedCurrentPlaylist = getAllCurrentSongs();

  // Stop the current song
  currentlyPlayingAudio.pause();
  currentlyPlayingAudio.currentTime = 0;

  var equal = true;
  // Compare the length of the arrays
  if (currentPlaylist.length === updatedCurrentPlaylist.length) {
    // If the arrays are the same length, compare each element
    var isEqual = true;
    currentPlaylist.each(function(index) {
      if (this !== updatedCurrentPlaylist[index]) {
        equal = false
      }
    });
  } else {
    equal = false;
  }

  if (equal) {
    // Playlist/state has not changed.
    currentPlaylistPosition = (currentPlaylistPosition + 1) % currentPlaylist.length;
    currentlyPlayingAudio = currentPlaylist[currentPlaylistPosition];
    currentlyPlayingAudio.play();
  } else {
    // The state has changed. The playlist is different. Start as if it were a new page load.
    lastSong = currentlyPlayingAudio;
    currentlyPlayingAudio = null;
    currentPlaylist = getAllCurrentSongs();
    currentPlaylistPosition = 0;
    playSong();

    if (currentlyPlayingAudio == lastSong) {
      playNextSong();
    }
  }

  playButton.style.display = 'none';
  pauseButton.style.display = 'inline-block';
}

function playLastSong() {
  // If current song time is > 2s then skip to the start of the song.
  if (currentlyPlayingAudio.currentTime > 2) {
    currentlyPlayingAudio.currentTime = 0;
  } else {
    // Otherwise, skip to the previous song.
    currentlyPlayingAudio.pause();
    currentlyPlayingAudio.currentTime = 0;

    currentPlaylistPosition = (currentPlaylistPosition - 1 + currentPlaylist.length) % currentPlaylist.length;
    currentlyPlayingAudio = currentPlaylist[currentPlaylistPosition];
    currentlyPlayingAudio.play();

    playButton.style.display = 'none';
    pauseButton.style.display = 'inline-block';
  }

}