function render_prod(info){
    console.log(info);
    console.log(document.getElementById("label").value);
    document.getElementById("label").innerHTML = info[0];
    document.getElementById("price").innerHTML = "$"+info[3];
    document.getElementById("store").innerHTML = info[2];
    document.getElementById("d").innerHTML = info[4];
    document.getElementById("image").innerHTML =  `<img src="http://127.0.0.1:5000/static/assets/data/`+info[1]+`.webp">`;
    r=info[5].split("@");
    console.log(r)

    var t=0;
    for(i =0;i<r.length-1;i++){
        document.getElementById("reviews").innerHTML+=  '<br><div class="comment"><p>'+r[i].slice(0,r[i].length-1)+'</p></div>';
        t+=parseInt(r[i].slice(r[i].length-1));
    }
    console.log(t)
    console.log(r)
    console.log(r.length)
    console.log(Math.floor(t/(r.length-1)))
    for(j =0;j<Math.floor(t/(r.length-1));j++){
    document.getElementById("rs").innerHTML+="<span class='fa fa-star checked'></span>"}
    for(j =0;j<5-Math.floor(t/(r.length-1));j++){
        document.getElementById("rs").innerHTML+="<span class='fa fa-star'></span>"}
}

