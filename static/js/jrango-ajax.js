$( document ).ready(function() {

    $('#likes').click(function(){
        var creatorid;
        var tripid;

        tripid = $(this).attr("data-tripid");
        creatorid = $(this).attr("data-creatorid");

        $.get('/TripShare/like_category/', {creator_id: creatorid, trip_id: tripid}, function(data){

                   $('#likes').hide();
        });
    });
});