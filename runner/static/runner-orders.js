$(document).ready(function () {
    'use strict';
    console.log("jquery working");
    $(".res_name").hide();
    $(".runner_id").hide();
    var res_name = $(".res_name").text();
    var runner_id = $(".runner_id").text();
    // TODO : Change interval so it is only called when a dish is ordered
    updateContent(res_name, runner_id);
    setInterval(function() { updateContent(res_name, runner_id); }, 10000 );
    console.log("jquery working");
})



function updateContent(res_name, runner_id) {
  var link = "/runner/home/update/"+runner_id+"/"+res_name;
  $(".orders").load(link);
}
