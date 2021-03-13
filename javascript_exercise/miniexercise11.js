window.onload=function(){
    var milisec="00";
    var sec="00";
    var buttonStart = document.getElementById('bs');
    var buttonStop = document.getElementById('bst');
    var buttonReset = document.getElementById('br');
    var interval;


bs.onclick=function(){
    clearInterval(interval);
    interval=setInterval(startTimer(),1000)
    }
bst.onclick=function(){
    clearInterval(interval);
}
br.onclick=function(){
    clearInterval(interval);
     milisec="00";
     min="00";
     append.innerHTML
}
function startTimer(){
    min=0;
    sec=0;
    sec++;
    if(sec<9){
        append.innerHTML="0"+sec;
    }
    if(sec>9)
    {
        append.innerHTML=sec;
    }
    
    if(sec==60){
    
    min=min+1;
    append.innerHTML="0"+min;
    sec=0;
    }
    if(min>60){
        hr=hr+1;
        append.innerHTML="0"+hr;
        sec="00";
        min="00";
    }
document.getElementById('abc').innerHTML=hr+":"+min+":"+sec
}
}