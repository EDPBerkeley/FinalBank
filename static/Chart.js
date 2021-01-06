let ctx1 = document.getElementById("myChart").getContext('2d');
let labels = ['Banking', 'Finances', 'Shopping', 'Recreation', 'Healthcare', 'Transportation', 'Food and Drink'];
let colorHex = ['#FB3640', '#86A9C5', '#286CA1', '#77FAC', '#1C203D', '#798E9C', '#2A303D'];
var chart1Data = JSON.parse(chart1)
let data1 = [chart1["Banking"],chart1["Finances"], chart1["Shopping"], chart1["Recreation"],chart1["Healthcare"],chart1["Transportation"], chart1["Food and Drink"]];
console.log(chart1Data["Banking"])

let myChart = new Chart(ctx1, {
  
  type: 'pie',
  data: {
    datasets: [{
      data: data1,
      backgroundColor: colorHex,
      borderWidth: [0,0,0,0,0,0,0]
    }],
    labels: labels,
  
  },
  options: {
    responsive: false,
    legend: {
      position: 'bottom',
      labels: {
        fontColor: 'white'
      }
    },
    
    
    plugins: {
      
      datalabels: {
        color: '#fff',
        anchor: 'end',
        align: 'start',
        offset: 10,
        borderWidth: 0,
        // borderColor: '#fff',
        borderRadius: 0,
        
        font: {
          size: '10',
          color: '#fff'
        },
        formatter: (value) => {
          return value + ' %';
        }
      }
    }
  }
})


let ctx2 = document.getElementById('myChart2').getContext('2d');
let labels2 = ['Banking', 'Finances', 'Shopping', 'Recreation', 'Healthcare', 'Transportation', 'Food and Drink'];
let colorHex2 = ['#FB3640', '#86A9C5', '#286CA1', '#77FAC', '#1C203D', '#798E9C', '#2A303D'];
let data2 = [chart2["Banking"],chart2["Finances"], chart2["Shopping"], chart2["Recreation"],chart2["Healthcare"], chart2["Food and Drink"], chart2["Transportation"]];
console.log(chart2["Banking"])
let myChart2 = new Chart(ctx2, {
  
  type: 'pie',
  data: {
    datasets: [{
      data: data2,
      backgroundColor: colorHex,
      borderWidth: [0,0,0,0,0,0,0]
    }],
    labels: labels2,
  
  },
  options: {
    responsive: false,
    legend: {
      position: 'bottom',
      labels: {
        fontColor: 'white'
      }
    },
    ticks: {
      autoSkip: false
    },
    
    
    plugins: {
      
      datalabels: {
        color: '#fff',
        anchor: 'end',
        align: 'start',
        offset: 10,
        borderWidth: 0,
        // borderColor: '#fff',
        borderRadius: 0,
        
        font: {
          size: '10',
          color: '#fff'
        },
        formatter: (value) => {
          return value + ' %';
        }
      }
    }
  }
})

// let ctx3 = document.getElementById('myChart3').getContext('2d');
// let labels3 = ['Banking', 'Finances', 'Shopping', 'Recreation', 'Healthcare', 'Transportation', 'Food and Drink'];
// let colorHex3 = ['#FB3640', '#86A9C5', '#286CA1', '#77FAC', '#1C203D', '#798E9C', '#2A303D'];
// let myChart3 = new Chart(ctx3, {
  
//   type: 'pie',
//   data: {
//     datasets: [{
//       data: [10, 10, 10, 10, 10, 10, 10],
//       backgroundColor: colorHex,
//       borderWidth: [0,0,0,0,0,0,0]
//     }],
//     labels: labels3,
  
//   },
//   options: {
//     responsive: false,
//     legend: {
//       position: 'bottom'
//     },
    
    
//     plugins: {
      
//       datalabels: {
//         color: '#fff',
//         anchor: 'end',
//         align: 'start',
//         offset: 10,
//         borderWidth: 0,
//         // borderColor: '#fff',
//         borderRadius: 0,
        
//         font: {
//           size: '10',
//           color: '#fff'
//         },
//         formatter: (value) => {
//           return value + ' %';
//         }
//       }
//     }
//   }
// })


let ctx4 = document.getElementById('myChart4').getContext('2d');
let colorHex4 = ['#FB3640', '#86A9C5', '#286CA1', '#77FAC', '#1C203D', '#798E9C', '#2A303D'];

//Loop through the chart4 array and add it to the data4 array
var data4 = [];
for(i=1; i<=31; i++) {
  data4.push(chart4[i]);
}

console.log(chart2["Banking"])
let myChart4 = new Chart(ctx4, {
  type: 'line',
  data: {
    labels: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
    ,
    datasets: [{ 
        data: data4,
        borderColor: "#E61616",
        
        fill: true,
      }
    ]
  },
  options: {
    scaleFontColor: "white",
    legend: {
      display: false,
    },
    title: {
      display: true,
      text: ''
    },   
    scales: {
      xAxes: [{
        gridLines: {
          display: false ,
          color: "#FFFFFF"
        },
         ticks: {
            fontColor: "white",
         }
      }],
      yAxes: [{
        gridLines: {
          display: false ,
          color: "#FFFFFF"
        },
         ticks: {
            fontColor: "white",
         }
      }]
   },
   plugins: {
      
    datalabels: {
      color: '#fff',
      anchor: 'end',
      align: 'start',
      offset: 10,
      borderWidth: 0,
      // borderColor: '#fff',
      borderRadius: 0,
      
    }
  }
  }
});


let ctx5 = document.getElementById('myChart5').getContext('2d');
//Loop through the chart4 array and add it to the data4 array
var data5 = [];
for(i=1; i<=12; i++) {
  data4.push(chart5[i]);
}
let myChart5 = new Chart(ctx5, {
  type: 'line',
  data: {
    labels: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    ,
    datasets: [{ 
        data: data5,
        borderColor: "#E61616",
        
        fill: true,
      }
    ]
  },
  options: {
    scaleFontColor: "white",
    legend: {
      display: false,
    },
    title: {
      display: true,
      text: ''
    },   
    scales: {
      xAxes: [{
        gridLines: {
          display: false ,
          color: "#FFFFFF"
        },
         ticks: {
            fontColor: "white",
         }
      }],
      yAxes: [{
        gridLines: {
          display: false ,
          color: "#FFFFFF"
        },
         ticks: {
            fontColor: "white",
         }
      }]
   },
   plugins: {
      
    datalabels: {
      color: '#fff',
      anchor: 'end',
      align: 'start',
      offset: 10,
      borderWidth: 0,
      // borderColor: '#fff',
      borderRadius: 0,
      
    }
  }
  }
});



// let ctx6 = document.getElementById('myChart6').getContext('2d');
// let labels6 = ['Banking', 'Finances', 'Shopping', 'Recreation', 'Healthcare', 'Transportation', 'Food and Drink'];
// let colorHex6 = ['#FB3640', '#86A9C5', '#286CA1', '#77FAC', '#1C203D', '#798E9C', '#2A303D'];
// let myChart6 = new Chart(ctx6, {
  
//   type: 'pie',
//   data: {
//     datasets: [{
//       data: [10, 10, 10, 10, 10, 10, 10],
//       backgroundColor: colorHex,
//       borderWidth: [0,0,0,0,0,0,0]
//     }],
//     labels: labels6,
  
//   },
//   options: {
//     responsive: false,
//     legend: {
//       position: 'bottom'
//     },
    
    
//     plugins: {
      
//       datalabels: {
//         color: '#fff',
//         anchor: 'end',
//         align: 'start',
//         offset: 10,
//         borderWidth: 0,
//         // borderColor: '#fff',
//         borderRadius: 0,
        
//         font: {
//           size: '10',
//           color: '#fff'
//         },
//         formatter: (value) => {
//           return value + ' %';
//         }
//       }
//     }
//   }
// })