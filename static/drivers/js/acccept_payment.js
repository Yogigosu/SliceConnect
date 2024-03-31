$(document).ready(function () {
    $(document.body).on('click', '.received', function () {
        let data = {"order_id": $(this).data('order')};
        let obj = JSON.stringify(data);
        let csrftoken = getCookie('csrftoken');


 
        })
    });
})
