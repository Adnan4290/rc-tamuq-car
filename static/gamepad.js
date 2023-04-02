var gamepad = new gamepad();

// Define the Dpad buttons
var dpadButtons = {
  up: 12,
  down: 13,
  left: 14,
  right: 15
};

// Define the button mappings to mouse events
var buttonMappings = {
  up: "up-btn",
  down: "down-btn",
  left: "left-btn",
  right: "right-btn"
};

// Add an event listener for gamepad connected event
gamepad.on('connect', function() {
  console.log('gamepad connected');
});

// Add an event listener for gamepad button change events
gamepad.on('buttonChange', function(e) {
  // Check if the button that changed is one of the Dpad buttons
  if (e.control === dpadButtons.up || e.control === dpadButtons.down || e.control === dpadButtons.left || e.control === dpadButtons.right) {
    // Get the corresponding button on the page
    var button = $("#" + buttonMappings[e.control]);
    // If the button is being pressed, trigger the mouse event
    if (e.value === 1) {
      button.trigger(buttonMappings[e.control]);
    }
  }
});

// Start polling the gamepad
gamepad.init();
