// Script.js for the web interface 
// take picture

var button = document.getElementById('take-pica-button');

button.onclick = function () {
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

button.onclick = function () {
    var div = document.getElementById('newpost');
    if (div.style.display !== 'none') {
        div.style.display = 'none';
    }
    else {
        div.style.display = 'block';
    }
};
//code for controls
document.getElementById('up-button').addEventListener('mousedown', function () {
    sendControl('up');
  });
  
  // Stop sending the signal when the up button is released
  document.getElementById('up-button').addEventListener('mouseup', function () {
    sendControl('stop');
  });
  
  // Repeat the same process for the other buttons
  document.getElementById('down-button').addEventListener('mousedown', function () {
    sendControl('down');
  });
  
  document.getElementById('down-button').addEventListener('mouseup', function () {
    sendControl('stop');
  });
  
  document.getElementById('left-button').addEventListener('mousedown', function () {
    sendControl('left');
  });
  
  document.getElementById('left-button').addEventListener('mouseup', function () {
    sendControl('stop');
  });
  
  document.getElementById('right-button').addEventListener('mousedown', function () {
    sendControl('right');
  });
  
  document.getElementById('right-button').addEventListener('mouseup', function () {
    sendControl('stop');
  });
  
  // Function to send the control signal to the backend
  function sendControl(direction) {
    $.ajax({
      url: '/controls',
      type: 'POST',
      data: { direction: direction },
      success: function (response) {
        console.log(response);
      },
      error: function (error) {
        console.log(error);
      }
    });
  }