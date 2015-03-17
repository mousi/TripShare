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
                return $content.is(":visible") ? "Hide details" : "View details";
            });
        });

    });

    $('.btn').click(function(e) {
        e.preventDefault();
    });
});