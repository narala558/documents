// jQuery


// selectors
$('#category option[value="blog_list?category=TECH"]').prop('selected', true);


// Disable button

$("input[value='vcf']").click(writeData);
function writeData() {
    jQuery("input[value=vcf]").attr('disabled',true);
}

// disable by default
$('select item').disabled = true;



// change vs click
$('#target').is('input')

$('#target').get(0).tagName.toLowerCase()


// set select to an option
$('#category option[value="blog_list?category=TECH"]').prop('selected', true);



// jquery autocomplete plugin

var tissues = [
    {"label": "taaaa 1"},
    {"label": "tbbbb 2"},
    {"label": "tcccc 3"},
    {"label": "tissue 4"},
    {"label": "tissue 5"},
];

$('input#id_tissue').autocomplete({
    source: function (request, response) {
        var term = $.ui.autocomplete.escapeRegex(request.term)
            , startsWithMatcher = new RegExp("^" + term, "i")
            , startsWith = $.grep(tissues, function(value) {
                return startsWithMatcher.test(value.label || value.value || value);
            })
            , containsMatcher = new RegExp(term, "i")
            , contains = $.grep(tissues, function (value) {
                return $.inArray(value, startsWith) < 0 &&
                    containsMatcher.test(value.label || value.value || value);
            });
        response(startsWith.concat(contains));
    }
});







// 1 =========================================================================
function likePost(post, user) {
     // ajax request..
     // return promise
}


function submitAction(actionHandler) {
    var user = getCurrentUser()
    var promise = actionHandler(user)
    // handle promise
}

var post = 1;

submitAction(likePost);


// 2 =========================================================================
function Polygon(height, width) {
    this.height = height;
    this.width = width;
}


var square = new Square(10);
console.log(square.area()); // 100

// 3 =========================================================================
// My test string -> yM tset gnirts








// bootstrap

// make navbar link active
$(document).ready(function() {
    $('a[href="' + this.location.pathname + '"]').parent().addClass('active');
});


























//  ember

//  Logs the arguments to the console.
var foo = 1;
Ember.Logger.log('log value of foo:', foo);
