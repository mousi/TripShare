$(document).ready(function() {
    $('.filters_header').click(function(){
        $header = $(this);
        $content = $(this).next();
        $content.slideToggle(500, function () {
            //execute this after slideToggle is done
            //change text of header based on visibility of content div
            $header.text(function () {
                //change text based on condition
                return $content.is(":visible") ? "Hide Filters" : "Show Filters";
            });
        });
    });
    $('#myrating').on('rating.change', function(event, value, caption) {
        $.ajax({
            type: "POST",
            url: "/TripShare/rate/",
            data: {
                'userrater_id': $(this).attr('rater-id'),
                'userrated_id': $(this).attr('rated-id'),
                'rating': value,
                'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
            },
            success: function (response) {
                //$(this).val(0)
            },
            error: function (rs, e) {
                $(this).rating('clear');
            }

        });
    });

    $('.detailsbtn').click(function () {
        $button = $(this);
        //getting the next element
        $content = $button.closest("div").find(".hiddencontent");
        //open up the content needed - toggle the slide- if visible, slide up, if not slidedown.
        $content.slideToggle(500, function () {
            //execute this after slideToggle is done
            //change text of header based on visibility of content div
            $button.text(function () {
                //change text based on condition
                return $content.is(":visible") ? "Hide Details" : "View Details";
            });
        });
    });

    $(function() {
        $( "#id_source,#id_destination" ).autocomplete({
            source: function( request, response ) {
                $.ajax({
                    url: "http://gd.geobytes.com/AutoCompleteCity?filter=UK",
                    dataType: "jsonp",
                    data: {
                        q: request.term
                    },
                    success: function( data ) {
                        response( data );
                    }
                });
            },
            minLength: 3,
            select: function(event, ui) {
                var selectedObj = ui.item;
                getcityname(selectedObj.value, $(this));
            }
        });
    });

    jQuery('#id_tripdate').datetimepicker({
        format:'d.m.Y H:i',
        inline:false,
        minDate:'0',
        lang:'en'
    });

    jQuery('#id_dob').datepicker({
        inline:false,
        lang:'en',
        maxDate:'0'
    });

    function getcityname(fqcn, txtField) {
        if(fqcn) {
            jQuery.getJSON(
                "http://gd.geobytes.com/GetCityDetails?callback=?&fqcn="+fqcn,
                function (data) {
                    txtField.val(data.geobytescity);
                }
            );
        }
    }

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
        $req_acc = $button.closest("tr").find(".req_acc");

        $.get('/TripShare/respond_request/', {request:request, choice: choice}, function(data){
            $req_acc.removeClass("glyphicon-ok glyphicon-remove glyphicon-minus");
            if (choice=="accept")
                $req_acc.addClass("glyphicon-ok");
            else
                $req_acc.addClass("glyphicon-remove");
            $('div.'+request).empty();
            $('div.'+request).append('<button type="button" class="btn btn-info">Your decision has been saved!</button>')
        });

    });
});
