$(document).ready(function () {
    'use strict';
    $(".res_name").hide();
    $(".chef_id").hide();
    console.log("jquery working");
    var res_name = $(".res_name").text();
    var chef_id = $(".chef_id").text();
    // TODO : Change interval so it is only called when a dish is ordered
    setInterval(function() { updateContent(res_name, chef_id); }, 10000 );
    console.log("jquery working");
})



function updateContent(res_name, chef_id) {
  var link = "/chef/home/update/"+chef_id+"/"+res_name;
  $(".orders").load(link);
}
