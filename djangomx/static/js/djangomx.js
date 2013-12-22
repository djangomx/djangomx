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
                console.log(data);
            }
        });
        return false;
    });
});