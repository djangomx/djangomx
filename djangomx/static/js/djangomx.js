// Developed by Ernesto Vargas
// me@netoxico.com

$(function() {
    // Animations
    $('.welcome-h2').addClass('animated fadeInDown');
    $('.welcome-p').addClass('animated fadeInUp');
    $('.feature-box').addClass('animated fadeInUp');

   // Add new subscription
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

    // Add new job form     
    $('#add-job-form').submit(function() {
        var fields = ['title', 'content', 'contact']
        $.ajax({
            type: 'POST',
            url: '/ofertas/nueva',
            data: $('#add-job-form').serialize(),
            success: function(data) {
                if (data.success === true) {
                    console.log("Job saved");
                } else {
                    $.each(fields, function( index, value ) {
                        $("label[for='" + value + "']").parent().removeClass('label-error');
                    });
                    $.each(data.errors, function( index, value ) {
                        $("label[for='" + value + "']").parent().addClass('label-error');
                    });
                }
            }
        });
        return false;
    });
});