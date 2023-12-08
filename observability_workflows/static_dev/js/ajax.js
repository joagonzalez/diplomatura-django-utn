var csrftoken = $.cookie('csrftoken');

function csrfSafeMethod(method){
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$('#search_button').click(function(){
    console.log('click on search button!')
    val = $('#autocomplete').val();
    searchDashoard(val);
})

function searchDashoard(val){
    $.ajax({
        beforeSend: function(xhr, settings){
            if(!csrfSafeMethod(settings.type) && !this.crossDomain){
                xhr.setRequestHeader("x-CSRFToken", csrftoken);
            }
        },
        url: '/tienda/search_dashboard_async/',
        type: "GET",
        data: {val: val,},
        success: function(json){
            returned_val = "<h2 style='padding-top: 50px;'>"+json[0].label+"</h2>" + "<img style='width: 5%; height: 5%;' src='/media/"+json[0].image+"'/><br />" + json[0].description;
            $('#filtered_return').html(returned_val);
            console.log(json[0].label);
        },
        error: function(xhr, errmsg, err){
            console.log('Error delivering search data');
        },
    });
}