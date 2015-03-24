$(document).ready(function() {

    //Searches a user. 404 error if he is not found.
    $('#search_user_btn').click(function(){
        var content = $('#search_user').val();
        window.location.replace('/TripShare/view/' + content);
    });

    //Updates the index page based on the city searched.
    $('#search_city_btn').click(function(){
        var content = $('#search_city').val();

        $('div .caption').each(function(index){
            $(this).parent().show();

            var text = $(this).children('h2').text();
            if ( text.toLowerCase().indexOf(content.toLowerCase()) == -1){
                //Hide every trip that does not depart or arrive to the city that the user is searching for.
                $(this).parent().hide();
            }
        });
    });

    setInterval(function(){
        checkNotifications() // this will run every 10 seconds
    }, 10000);

    // The function that checks for new notifications. this will be called by the above anonymous function
    function checkNotifications() {
        $requestsbtn = $('#requestsbtn');
        $.ajax({
            type: "POST",
            url: "/TripShare/checknotif/",
            data: {
                'usrid': $requestsbtn.attr('user-id'),
                'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
            },
            success: function (response) {
                if (response == "True") {
                    $requestsbtn.addClass('newnotif');
                } else {
                    $requestsbtn.removeClass('newnotif');
                }
            }
        });
    }

    //Shows everything in the index page.
    $('#clear_city_btn').click(function(){
        $('#search_city').val("");
        $('div .caption').each(function(index){
            $(this).parent().show();
        });
    });

    //Handles the rating of users.
    $('#myrating').on('rating.change', function(event, value, caption) {
        $.ajax({
            type: "POST",
            url: "/TripShare/rate/",
            //Gets the rater's and the rated user's ID and the rating value.
            data: {
                'userrater_id': $(this).attr('rater-id'),
                'userrated_id': $(this).attr('rated-id'),
                'rating': value,
                'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
            },
            success: function (response) {
                //Updates the rating's stars.
                $('#avgrating').rating('update', response);
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

    //Handles the autocompletion function for cities.
    $(function() {
        $("#id_source,#id_destination,#search_city").autocomplete({
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

    //Helper function for trimming the city output string.
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

    //Plugin for choosing a future date and time for posting trips.
    jQuery('#id_tripdate').datetimepicker({
        format:'d.m.Y H:i',
        inline:false,
        minDate:'0',
        lang:'en'
    });

    //Plugin for choosing a past date for choosing the user's birthdate.
    jQuery('#id_dob').datepicker({
        changeMonth: true,
        changeYear: true,
        inline:false,
        format:'d/m/Y',
        lang:'en',
        maxDate:'0'
    });

    //Handles the users' request to join a trip.
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
            }
        });
    });

    //Handles the user's dealing of requests from other users for his trips.
    $(".req").click(function(){
        var choice = $(this).attr('id');
        var request = $(this).attr('data-req');
        $button = $(this);
        $req_acc = $button.closest("tr").find(".req_acc");

        $.get('/TripShare/respond_request/', {request:request, choice: choice}, function(data) {
            // If the trip is full, alert the user and then reload the page to reload the trips' statuses
            if(data=="tripfull") {
                alert("This trip is full! Can't accept new requests!");
                document.location.reload();
            // If there is no driver, alert the user
            } else if (data=="nodriver") {
                alert("There is no driver in this trip and you are trying to fill the last position. Please choose a driver instead!");
            // If the repsonse was OK
            } else {
                // Change the icon of the request status
                $req_acc.removeClass("glyphicon-ok glyphicon-remove glyphicon-minus");
                if (choice == "accept")
                    $req_acc.addClass("glyphicon-ok");
                else
                    $req_acc.addClass("glyphicon-remove");

                // Delete the two buttons and replace them with an appropriate disabled button
                $('div.' + request).empty();
                $('div.' + request).append('<button type="button" class="btn btn-info disabled">Decision saved!</button>');
            }
        });
    });
    $(function() {
        $("#search_user").autocomplete({
            source: function( request, response ) {
                $.ajax({
                    type:'POST',
                    url: "/TripShare/get_users/",
                    data: {
                        q: request.term,
                        csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
                    },
                    success: function( data ) {
                        response( data );
                    }
                });
            },
            minLength: 2
        });
    });
});
