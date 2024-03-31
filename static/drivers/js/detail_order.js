$('input.status').change(
    function () {
        if (this.checked) {
            let status = {"status": $(this).val()};
            let obj = JSON.stringify(status)
            let csrftoken = getCookie('csrftoken');

 
        }
    });
