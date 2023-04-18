function updateTime() {
  var now = new Date();
  var months = [
    "января", "февраля", "марта", "апреля", "мая", "июня",
    "июля", "августа", "сентября", "октября", "ноября", "декабря"
  ];
  var month = months[now.getMonth()];
  var date = now.getDate();
  var year = now.getFullYear();
  var hours = now.getHours();
  var minutes = now.getMinutes();
  var seconds = now.getSeconds();

  // format date
  var dateString = date + " " + month + " " + year;

  // format time
  var timeString = hours + ":" + minutes + ":" + seconds;

  // display date and time
  document.getElementById("date").innerHTML = dateString;
  document.getElementById("time").innerHTML = timeString;
}

// update time every second
setInterval(updateTime, 1000);
