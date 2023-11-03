function e2(i){
    console.log("sdfsdfdssdfds")
    document.getElementById("next").innerHTML=`


    <h1>`+d2[i][0]+`</h1>
    <p>`+d2[i][1] +`</p>
    <p>`+d2[i][2]+`</p>
    <p>At `+ d2[i][3]+`</p>
    <br><h2></h2><p></p>
    

    
    `   
}
function render_events(d){
d2=d;
    document.getElementById("next").innerHTML=`


<h1>`+d[0][0]+`</h1>
<p>`+d[0][1] +`</p>

<br><h2></h2><p></p>






`
for(i=0;i<d.length;i++){
    document.getElementById("calendar").innerHTML+=`
<div class="event" onclick="e2(`+i+`)">
<div><h2>`+d[i][0]+`</h2><p>`+d[i][1]+`</p></div><div class="time"></div>
</div>
`
}
}
