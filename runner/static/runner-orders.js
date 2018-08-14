$(document).ready(function () {
    'use strict';
    console.log("jquery working");
    var res_name = $(".res_name").text();
    var runner_id = $(".runner_id").text();
    // TODO : Change interval so it is only called when a dish is ordered
    setInterval(function() { updateContent(res_name, runner_id); }, 1000 );
    console.log("jquery working");
})



function updateContent(res_name, chef_id) {
  var link = "/runner/home/update/"+runner_id+"/"+res_name;
  $(".orders").load(link).fadeIn("fast");
}
