
let date = new Date();
let day  = date.getDate();


let week = date.getDay()
let weeks = ["日","一","二","三","四","五","六"]
for(var i=0;i<7;i++){
  if(week===i){
    week="星期"+weeks[i];
  }
}


let year  = date.getFullYear();
let month = date.getMonth()+1;
month < 10 ? month='0'+month : month;
let ym = year+ '.' +month;


window.onload = function () {
  //日期
  let node1=document.createElement("P")
  let dateNode=document.createTextNode(day);
  node1.appendChild(dateNode);
  document.getElementById('date').appendChild(node1)
  //星期
  let node2=document.createElement("P")
  let weekNode=document.createTextNode(week);
  node2.appendChild(weekNode);
  document.getElementById('week').appendChild(node2)
  //年月
  let node3=document.createElement("P")
  let ymNode=document.createTextNode(ym);
  node3.appendChild(ymNode);
  document.getElementById('year').appendChild(node3)
};
