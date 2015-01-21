$(document).ready(function(){

    price = 0;
    min_evaluation = 0;

    $('#search').keyup(function(){
        filter(price, min_evaluation);
    });

    $('#filter').change(function(){
        filter(price, min_evaluation);
    });

    $('#ascdesc').change(function(){
        filter(price, min_evaluation);
    });

    $('#price_commercial').click(function(){
        price = 1;
        filter(price, min_evaluation);
    });

    $('#star1').click(function(){
        filter(price, 1);
    });

    $('#star2').click(function(){
        filter(price, 2);
    });

    $('#star3').click(function(){
        filter(price, 3);
    });

    $('#star4').click(function(){
        filter(price, 4);
    });

    $('#star5').click(function(){
        filter(price, 5);
    });

});

function filter(price, min_evaluation)
{
    $.ajax({
            type: "POST",
            url: "/apps/search/",
            data: {
                'search_text': $('#search').val(),
                'filter': $('#filter').val(),
                'ascdesc': $('#ascdesc').val(),
                'price': price,
                'min_evaluation': min_evaluation,
                'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
            },
            success: searchSuccess,
            dataType: 'html'
        });
}

function searchSuccess(data, textStatus, jqXHR)
{
    $('#store_content').html(data);
}