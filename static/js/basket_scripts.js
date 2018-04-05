window.onload = function (event) {
    $('table').on('click', 'input[type="number"]', function (event) {
        var t_href = event.target;

        $.ajax({
            url: "/basket/product/edit/" + t_href.name + "/" + t_href.value + "/",
            success: function (data) {
                $('table').html(data.result);
            },
        });

        event.preventDefault();
    });
}
