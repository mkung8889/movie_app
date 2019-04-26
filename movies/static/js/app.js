var userId = d3.select("userId").txt()
console.log(`user id: ${userId}`)

d3.json('/movies/recommended/{user_id}').then(userId=> {
    var movie_recs = d3.select("movie_rec").append()
})
