var slider = document.getElementById("myRange");
var output = document.getElementById("pr");
output.innerHTML = "Items under" +" $ "+ slider.value;

slider.oninput = function() {
  output.innerHTML = "Items under" +" $ "+ this.value;;
}
var r="";
function render_search(results){
  u = new URL(window.location.href)
  const p = u.searchParams
  console.log(p);
  for(i=0;i<results[0].length;i++){
    console.log(r);
    console.log(i);
    print
    if(i%2==0){
      document.getElementById("results").innerHTML=document.getElementById("results").innerHTML+r;
       r= '<div class="row">';
    }
    console.log(p.get("p"));
      if(parseFloat(results[0][i][3])<=p.get("p") || p.get("p")==null){
   ///     if((p.get("c")==true && results[0][i][0].includes("halal"))||(p.get("c")==false || p.get("c")==null)){
        r+=`    
        <div class = listing>
      
        <img src="/static/assets/data/`+results[0][i][1]+`.webp">
        <div class="info" id="`+results[0][i][1]+`">
        <a href=/prod?p=`+results[0][i][1]+`><h2 class="name">`+results[0][i][0]+`</h2></a><p>`+results[0][i][2]+`</p><p class="cost"> $`+results[0][i][3]+`</p>
        <div id = "rs`+results[0][i][1]+`">
</div>
        <p>Delivery: 25 hours</p>
        </div></div>`;}
  }
  console.log(r);
  document.getElementById("results").innerHTML=document.getElementById("results").innerHTML+r+"</div>";

}
function filter(){
  console.log("hi");
  window.location.href = window.location.href+"&p="+document.getElementById("myRange").value+"&c="+document.getElementById("c").checked+"&g="+document.getElementById("g2").checked+"&o="+document.getElementById("o2").checked;
}
function render_reviews(data){
  console.log(data)
  for(var k=0;k<data[0].length;k++){
    console.log(data.length)
  r3=data[0][k][5]
  console.log(r3);
  r = r3.split("@");
  var t=0;
  for(i =0;i<r.length-1;i++){
      t+=parseInt(r[i].slice(r[i].length-1));
  }
  console.log(t)
  for(j =0;j<Math.floor(t/(r.length-1));j++){
  var s ="rs"+data[0][k][1]
  document.getElementById(s).innerHTML+="<span class='fa fa-star checked'></span>"}
  for(j =0;j<5-Math.floor(t/(r.length-1));j++){
      document.getElementById(s).innerHTML+="<span class='fa fa-star'></span>"}
    }
}