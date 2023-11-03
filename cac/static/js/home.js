
function render_recent(data){
s=""
for (i=0;i<data.length;i++){
    l="'http://127.0.0.1:5000/static/assets/data/"+data[i][1]+".webp'"
    c2 = 'style="height:50%;width:50%; background-image: url('+l+'); background-size: 100% 100%; margin-left: 25%"'
    c = 'style=""'
    imc = '<div class = imgc '+c2+'></div>'
    s+='<div class = pcard '+c+'"><a class=title>'+data[i][0]+'</a>'+imc+'<p>'+'$'+data[i][3]+'</p><p>'+data[i][2]+'</p></div>'
}
document.getElementById("recent").innerHTML = s;
console.log(s)
//document.getElementById("recent").innerHTML = '<div class = "pcard">'+data[0][0]+'</div>';
}