$(document).ready(function() {
  'use strict';
  console.log("jquery working");
  var order_id = $(".order_id").text();
  updateContent(order_id);
  setInterval(function() { updateContent(order_id); }, 10000 );
  console.log("jquery working");
})



function updateContent(order_id) {
var link = "/user/pay/exit/"+order_id;
$(".exit").load(link);
}
