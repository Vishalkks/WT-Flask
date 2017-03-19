$("document").ready(function(){
    $('#btnsign').click(function() {
       /* $.ajax({
            url: '/signup',
            data: $('#formsign').serialize(),
            type: 'POST',
            success: function(response) {
                console.log(response);
            },
            error: function(error) {
                console.log(error);
            }
        });*/
        $('#formsign').submit();
    });
    $('#btnlog').click(function(){
    $('#loginform').submit();
    });
});
