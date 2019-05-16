
// // Method 1:
// var tbody = d3.select("tbody");
// var csv_url = '/new_movies'
// d3.json(csv_url, data=> {
//     console.log(data)
//     Object.entries(data).forEach(([key,value])=> {
//         var newRow = tbody.append('tr');
//         tbody.append("td").text(value["movie_id"]);
//         tbody.append("td").text(value["movie_title"]);
//         tbody.append("td").text(value["genre"]);
//     });
// })
// console.log("done")

// Method 2:
var tbody = d3.select("tbody");

function moviesTable(movies_list){
    movies_list.forEach(movie=> {
    var newRow = tbody.append("tr");
    var cell1 = tbody.append("td");
    var cell2 = tbody.append("td");
    var cell3 = tbody.append("td");
    cell1.text(movie["movie_id"])
    cell2.text(movie["movie_title"])
    cell3.text(movie["genre"])

    });
}
moviesTable(movies)

var sortOption = d3.select("#sort");
for (var i=0; i<genres.length; i++) {
    // console.log(genres[i]);
    sortOption.append("option").attr("value", genres[i]).text(genres[i]);
}


function compareAZ( a, b ) {
    if ( a.movie_title < b.movie_title ){
      return -1;
    }
    if ( a.movie_title > b.movie_title ){
      return 1;
    }
    return 0;
}
function compareZA( a, b ) {
    if ( a.movie_title > b.movie_title ){
        return -1;
    }
    if ( a.movie_title < b.movie_title ){
        return 1;
    }
    return 0;
}
function yearASC( a, b ) {
    if ( a.movie_title.split("(").slice(-1,) < b.movie_title.split("(").slice(-1,) ){
        return -1;
    }
    if ( a.movie_title.split("(").slice(-1,) > b.movie_title.split("(").slice(-1,) ){
        return 1;
    }
    return 0;
}
function yearDESC( a, b ) {
    if ( a.movie_title.split("(").slice(-1,) > b.movie_title.split("(").slice(-1,) ){
        return -1;
    }
    if ( a.movie_title.split("(").slice(-1,) < b.movie_title.split("(").slice(-1,) ){
        return 1;
    }
    return 0;
}
function compareGenre( a,b ) {
    if ( a.genre < b.genre ){
        return -1;
      }
      if ( a.genre > b.genre ){
        return 1;
      }
      return 0;
}

function sortMovies() {
    var sort = d3.select("#sort").property("value");

    if (sort == "az") {
        var sortedMovies = movies.sort(compareAZ)
        console.log(sortedMovies)
        console.log("sorted movies a->z")
    }
    else if (sort == "za") {
        var sortedMovies = movies.sort(compareZA)
        console.log(sortedMovies)
        console.log("sorted movies z->a")
    }
    else if (sort == "yearASC") {
        var sortedMovies = movies.sort(yearASC)
        console.log(sortedMovies)
        console.log("sorted movies year asc.")
    }
    else if (sort == "yearDESC") {
        var sortedMovies = movies.sort(yearDESC)
        console.log(sortedMovies)
        console.log("sorted movies year desc.")
    }
    else if (sort == "genre") {
        var sortedMovies = movies.sort(compareGenre)
        console.log(sortedMovies)
        console.log("sorted movies genre")
    }

    else if (genres.includes(sort)) {
        function filterGenre(data) {
            return data.genre.split("|").includes(sort)
        }
        console.log(sort)
        var sortedMovies = movies.filter(filterGenre)
        console.log(sortedMovies)
    }

    tbody.html("")
    moviesTable(sortedMovies)
}