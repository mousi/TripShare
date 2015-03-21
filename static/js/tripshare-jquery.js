$(document).ready(function() {

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
});
