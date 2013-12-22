$(function() {
    $('#welcome-h2').addClass('animated fadeInDown');
    $('#welcome-p').addClass('animated fadeInUp');
    $('.feature-box').addClass('animated fadeInUp');

    $('#newsletter-form').submit(function() {
        $.ajax({
            type: 'POST',
            url: '/subscribe',
            data: $('#newsletter-form').serialize(),
            success: function(data) {
                if (data.success === true) {
                    var button = $('#subscribe-button');
                    button.html('<span class="glyphicon glyphicon-ok"></span>');
                    button.attr('type', 'button');
                    $("input[name='email_field']").val('');

                } else {
                    $('#newsletter-form').addClass('animated bounce');
                    setTimeout(function(){$('#newsletter-form').removeClass('animated bounce')}, 1000)
                }
            }
        });
        return false;
    });
});