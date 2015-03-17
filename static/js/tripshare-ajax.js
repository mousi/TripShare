$(document).ready(function() {

    $(".join").click(function(){
        $.ajax({
            type:"POST",
            url:"join_trip/",
            data:{
                'user_id': $(this).attr('data-user'),
                'trip_id': $(this).attr('data-trip'),
                'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
            },
            success: function(response){

            },
            error: function(rs, e) {
                       alert(rs.responseText);
            }
        });

    });

});