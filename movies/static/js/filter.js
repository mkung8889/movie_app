
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
// function yearASC( a, b ) {
//     if ( a.movie_title.slice(-5,-1) > b.movie_title.slice(-5,-1) ){
//         return -1;
//     }
//     if ( a.movie_title.slice(-5,-1) < b.movie_title.slice(-5,-1) ){
//         return 1;
//     }
//     return 0;
// }
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
    // console.log(sort);
    if (sort == "az") {
        tbody.html("")
        var sortedMovies = movies.sort(compareAZ)
        console.log(sortedMovies)
        moviesTable(sortedMovies)
        console.log("sorted movies a->z")
    }

    else if (sort == "za") {
        tbody.html("")
        var sortedMovies = movies.sort(compareZA)
        console.log(sortedMovies)
        moviesTable(sortedMovies)
        console.log("sorted movies z->a")
    }
    else if (sort == "yearASC") {
        tbody.html("")
        var sortedMovies = movies.sort(yearASC)
        console.log(sortedMovies)
        moviesTable(sortedMovies)
        console.log("sorted movies year asc.")
    }
    else if (sort == "yearDESC") {
        tbody.html("")
        var sortedMovies = movies.sort(yearDESC)
        console.log(sortedMovies)
        moviesTable(sortedMovies)
        console.log("sorted movies year desc.")
    }
    else if (sort == "genre") {
        tbody.html("")
        var sortedMovies = movies.sort(compareGenre)
        console.log(sortedMovies)
        moviesTable(sortedMovies)
        console.log("sorted movies genre")
    }

    else if (sort == "comedy") {
        
    }

    else {

    }
}