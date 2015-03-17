$(document).ready(function() {

    $(".join").click(function(){
        $button = $(this)
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
                $button.addClass("btn-success");
                $button.text("Request Successful");
            },
            error: function(rs, e) {
                $button.removeClass("btn-primary");
                $button.addClass("btn-danger");
                $button.text("Error! Please reload");
                       //alert(rs.responseText);
            }
        });

    });
});
