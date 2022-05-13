$(document).ready(function() {

    $('form').on('submit', function(event) {

        $.ajax({
            data: {
                name: $('#nameInput').val(),
                email: $('#emailInput').val()
            },
            type: 'POST',
            url: '/process'
        })
        .done(function(data) {

            if (data.error) {
                $('#errorAlert').text(data.error).show();
                $('#sucessAlert').hide();

            }
            else {
                $('#sucessAlert').text(data.msg).show();
                $('#errorAlert').hide();
            }
        
        });
        event.preventDefault(); //'segurar' o envio do form
    });
});