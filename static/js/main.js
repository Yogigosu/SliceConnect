// using jQuery
function notifyNow(message, type){
    $.notify(
        message, 
        type, 
        { elementPosition: 'top center', globalPosition: 'top center' }
    );
}


    
$(document).ready(function () {
    $("#messages").fadeIn(1000).delay(3000).fadeOut(1000);
    // search placeholder
    function addToPlaceholder(toAdd, el) {
        el.attr('placeholder', el.attr('placeholder') + toAdd);
        // Delay between symbols "typing"
        return new Promise(resolve => setTimeout(resolve, 70))
    }

    // Clear placeholder attribute in given element
    function clearPlaceholder(el) {
        el.attr("placeholder", "");
    }

 

    // Print given phrases to element
    function printPhrases(phrases, el) {
        // For each phrase
        // wait for phrase to be typed
        // before start typing next
        phrases.reduce(
            (promise, phrase) => promise.then(_ => printPhrase(phrase, el)),
            Promise.resolve()
        );
    }

    // Start typing
    function runSearchHelp() {
        let phrases = [
            "e.g. Rajshahi",
            "e.g. Pizza",
            "e.g Master Chef"
        ];
        printPhrases(phrases, $('#search_input'));
    }
    runSearchHelp();

 


    /*	MOBILE */
    $("#btn_expand").click(function () {
        $("#cartMenuContainer").removeClass("d-none");
        $("#cartMenuContainer").addClass("fixed-top mt-5");
    });
    $("#close_btn").click(function () {
        $("#cartMenuContainer").addClass("d-none");
        $("#cartMenuContainer").removeClass("fixed-top mt-5");
    });

});