$(document).ready(function () {
    $('.refresh').click(function () {
        var rel = parseInt($('.refresh:checked').attr('rel'));

        $.ajax({
            type: 'POST',
            dataType: 'json',
            cache: false,
            data: {
                itemID: rel
            }
            url: '/ajax.php',
            success: function (data) {
                if(!data.answer) {
                    alert('Error');
                }
            }
        });
    });
});