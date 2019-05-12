var button = d3.select("#filter-btn");
var error = d3.select("error");

button.on( "click", function(){
    var userId = d3.select("#userId").property("value");
    console.log(userId)
    if (!(userId in Range(1,948))) {
        console.log("invalid User ID")
        d3.event.preventDefault();
        var errorDiv = error.append("div")
                            .attr("class","alert alert-danger alert-dismissible fade in");
    }
    console.log("error bar")
})
{/* <div class="alert alert-danger alert-dismissible fade in">
    <a href="#" class="close" data-dismiss="alert" aria-label="close">&times;</a>
    <strong>Danger!</strong> This alert box could indicate a dangerous or potentially negative action.
  </div> */}

var submitButton = d3.select("#btn");

submitButton.on("click", function(){
  var ratings = [];
  var elems = document.querySelectorAll("#exampleFormControlSelect1");
  elems.forEach(function(el){
    ratings.push(el.options[el.selectedIndex].text);
    d3.event.preventDefault();
  })
  return ratings
});

$.ajax({
  url: Flask.url_for('recommender'),
  type: "POST", 
  data: ratings
})
.done(function(result){
  console.log(result)
})