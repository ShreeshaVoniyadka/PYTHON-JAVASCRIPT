/*function clk(){
    
    var date=new Date();
    var sec=date.getSeconds();
    var min=date.getMinutes();
    var hr=date.getHours();
    session="AM";

    if(hr==0){
       hr=12;
    }
    if(hr>12){
        hr=12-hr;
        session="PM";
    }
    hr = (hr < 10) ? "0" + hr : hr;
    min = (min < 10) ? "0" + min : min;
    sec = (sec < 10) ? "0" + sec : sec;

    //var time=hr+":"+min+":"+sec+session;
   // document.getElementById("clock").innerHTML=time;
   // document.getElementById("clock").textContent = time;
    

}
clk();*/
