// Global
var url = "https://s3.amazonaws.com/t206/images/loc/fronts/";

// Hide initial
$("#searching").hide();
$("#results-table").hide();
$("#error").hide();

// Send AJAX request when image is clicked
$(function() {

  // sanity check
  console.log( "ready!" );

  // image click
  $(".img").click(function() {

    // empty/hide results
    $("#results").empty();
    $("#results-table").hide();
    $("#error").hide();

    // remove active class
    $(".img").removeClass("active");

    // add active class to clicked picture
    $(this).addClass("active");

    // grab image url
    var image = $(this).attr("src");
    console.log(image);

    // show searching text
    $("#searching").show();
    console.log("searching...");

    // ajax request
    $.ajax({
      type: "POST",
      url: "/search",
      data : { img : image },
      // handle success
      success: function(result) {
        console.log(result.results);
        var data = result.results;
        // show table
        $("#results-table").show();
        // append result to dom
        $("#results").append('<tr><th><a href="'+url+data.image+'"><img src="'+
          url+data.image+'" class="result-img"></a></th><th>'+data.score+
          '</th></tr>');
      },
      // handle error
      error: function(error) {
        console.log(error);
        // append to dom
        $("#error").append();
      }
    });

  });

});
