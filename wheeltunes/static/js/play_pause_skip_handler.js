function togglePlayPause(action) {
    if (action === 'play') {
      playButton.style.display = 'none';
      pauseButton.style.display = 'inline-block';
    } else if (action === 'pause') {
      playButton.style.display = 'inline-block';
      pauseButton.style.display = 'none';
    }
}