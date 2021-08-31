function send(cmd){
NRF.requestDevice({ filters: [{ namePrefix: 'Puck.js' }] }).then(function(device) {
  require("ble_simple_uart").write(device, cmd, function() {
    print('Done!');
  });
});
}




function red(){

  digitalWrite(LED1,1,1000);
  send("digitalWrite(LED1,1,1000)\n");

}
function red_off(){

  digitalWrite(LED1,0,1000);
  send("digitalWrite(LED1,0,1000)\n");

}

function green(){

  digitalWrite(LED2,1,1000);
  send("digitalWrite(LED2,1,1000)\n");

}

function green_off(){

  digitalWrite(LED2,0,1000);
  send("digitalWrite(LED2,0,1000)\n");

}




setWatch(red, D1, { edge:"rising", debounce:50, repeat: true });
setWatch(red_off, D1, { edge:"falling", debounce:50, repeat: true });

setWatch(green, D31, { edge:"rising", debounce:0, repeat: true });
setWatch(green_off, D31, { edge:"falling", debounce:50, repeat: true });


/*
var zero = Puck.mag();
var doorOpen = false;

function onMag(p) {
  p.x -= zero.x;
  p.y -= zero.y;
  p.z -= zero.z;
  var s = Math.sqrt(p.x*p.x + p.y*p.y + p.z*p.z);
  console.log(s);
  
  
  var open = s<1000;
  if (open!=doorOpen) {
    doorOpen = open;
    digitalPulse(open ? LED1 : LED2, 1,1000);
    send(open ? "digitalPulse(LED1,1,1000)\n" : "digitalPulse(LED2,1,1000)\n");
  }
  
}*/
//Puck.on('voice', voice);
//Puck.magOn();