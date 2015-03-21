$(document).ready(function() {

    $(".join").click(function(){
        $button = $(this);
        $.ajax({
            type:"POST",
            url:"join_trip/",
            data:{
                'user_id': $(this).attr('data-user'),
                'trip_id': $(this).attr('data-trip'),
                'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
            },
            success: function(response){
                $button.removeClass("btn-primary");
                $button.addClass("btn-success disabled");
                $button.text("Request Successful");
            },
            error: function(rs, e) {
                $button.removeClass("btn-primary");
                $button.addClass("btn-danger disabled");
                $button.text("Error! Please reload");
                       //alert(rs.responseText);
            }
        });
    });

    $(".req").click(function(){
        var choice = $(this).attr('id');
        var request = $(this).attr('data-req');
        $button = $(this);

        $.get('/TripShare/respond_request/', {request:request, choice: choice}, function(data){

            $('div.'+request).empty();
            $('div.'+request).append('<button type="button" class="btn btn-info">Your decision has been saved!</button>')
        });

    });
});
