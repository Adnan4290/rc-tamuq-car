// take picture
var button = document.getElementById('take-pica-button');

button.onclick = function() {
    var div = document.getElementById('newpost');
    if (div.style.display !== 'none') {
        div.style.display = 'none';
    }
    else {
        div.style.display = 'block';
    }
};
// stop stream - called when pressing red X
var button = document.getElementById('button');

button.onclick = function() {
    var div = document.getElementById('newpost');
    if (div.style.display !== 'none') {
        div.style.display = 'none';
    }
    else {
        div.style.display = 'block';
    }
};

// Take and save a photo, call picture function in main.py
$(function() {
  $('a#take-picture').on('click', function(e) {
    e.preventDefault()
    $.getJSON('/picture',
        function(data) {
      //do nothing
    });
    return false;
  });
});