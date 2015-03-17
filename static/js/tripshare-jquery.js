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
            open: function() {
                //$( this ).removeClass( "ui-corner-all" ).addClass( "ui-corner-top" );
            },
            close: function() {
                //$( this ).removeClass( "ui-corner-top" ).addClass( "ui-corner-all" );
            }
        });
    });

    jQuery('#id_tripdate').datetimepicker({
        format:'d.m.Y H:i',
        inline:false,
        minDate:'0',
        lang:'en'
    });
    /*$(function() {
    $( "#id_tripdate" ).datepicker({
        minDate: 1,
    onSelect: function(theDate) {
        $("#dataEnd").datepicker('option', 'minDate', new Date(theDate));
    },
    dateFormat: 'dd/mm/yy',
    });

  });*/

});
