var audio = new Audio('sherlock_theme.mp3');
function ply(){
audio.play()
}
function stp(){
audio.pause()
audio.currentTime = 0;
}