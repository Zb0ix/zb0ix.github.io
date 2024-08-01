document.addEventListener('DOMContentLoaded', () => {
    const surasList = document.getElementById('surasList');
    const playButton = document.getElementById('playButton');
    const audioPlayer = document.getElementById('audioPlayer');

    playButton.addEventListener('click', () => {
        const selectedSurah = surasList.value;
        audioPlayer.src = selectedSurah;
        audioPlayer.play();
    });
});
