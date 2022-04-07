var mysql = require('mysql');

var con = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "123",
  database: "colyser"
});

var mencount = 0;
var womencount = 0;

con.connect(function(err) {
    if (err) throw err;
    con.query("SELECT COUNT(*) FROM user_table where gender = M", function (err, result, fields) {
      if (err) throw err;
      console.log(result);
      mencount = result;
    });
});

con.connect(function(err) {
    if (err) throw err;
    con.query("SELECT COUNT(*) FROM user_table where gender = F", function (err, result, fields) {
      if (err) throw err;
      console.log(result);
      womencount = result;
    });
});

var barColors = ["grey", "blue","purple","orange","brown"];

new Chart("myChart", {
  type: "bar",
  data: {
    labels: ["Men", "Women"],
    datasets: [{
      backgroundColor: barColors,
      data: [mencount, womencount]
    }]
  },
  options: {
    legend: {display: false},
    title: {
      display: true,
      text: "Gender count for positives tests"
    }
  }
});

new Chart("myChart2", {
    type: "pie",
    data: {
      labels:["Men", "Women"],
      datasets: [{
        backgroundColor: barColors,
        data: [mencount, womencount]
      }]
    },
    options: {
      title: {
        display: true,
        text: "World Wide Wine Production"
      }
    }
  });