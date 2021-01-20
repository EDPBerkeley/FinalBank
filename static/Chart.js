let ctx1 = document.getElementById("myChart").getContext('2d');
let labels = ['Banking', 'Finances', 'Shopping', 'Recreation', 'Healthcare', 'Transportation', 'Food and Drink'];
let colorHex = ['#FB3640', '#86A9C5', '#286CA1', '#77FAC', '#1C203D', '#798E9C', '#2A303D'];
var chart1Data = JSON.parse(chart1)
let data1 = [chart1Data["Banking"], chart1Data["Finances"], chart1Data["Shopping"], chart1Data["Recreation"],chart1Data["Healthcare"],chart1Data["Transportation"], chart1Data["Food and Drink"]];
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
        fontColor: '#4c4c4c'
      }
    },
    
    
    plugins: {
      
      datalabels: {
        color: '#4c4c4c',
        anchor: 'end',
        align: 'start',
        offset: 10,
        borderWidth: 0,
        // borderColor: '#fff',
        borderRadius: 0,
        
        font: {
          size: '10',
          color: '#4c4c4c'
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
var chart2Data = JSON.parse(chart2)
let data2 = [chart2Data["Banking"],chart2Data["Finances"], chart2Data["Shopping"], chart2Data["Recreation"],chart2Data["Healthcare"], chart2Data["Food and Drink"], chart2Data["Transportation"]];
console.log(chart2Data["Banking"])
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
        fontColor: '#4c4c4c'
      }
    },
    ticks: {
      autoSkip: false
    },
    
    
    plugins: {
      
      datalabels: {
        color: '#4c4c4c',
        anchor: 'end',
        align: 'start',
        offset: 10,
        borderWidth: 0,
        // borderColor: '#fff',
        borderRadius: 0,
        
        font: {
          size: '10',
          color: '#4c4c4c'
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
var chart4Data = JSON.parse(chart4)
//Loop through the chart4 array and add it to the data4 array
var data4 = [];
var label4 = [];
for(i=0; i<=30; i++) {
  data4.push(chart4Data[i.toString()]);
}
console.log("Hi1")
console.log(chart4Data)
console.log(data4)
console.log("Hi2")
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
    scaleFontColor: "4c4c4c",
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
          color: "#4c4c4c"
        },
         ticks: {
            fontColor: "white",
         }
      }],
      yAxes: [{
        gridLines: {
          display: false ,
          color: "#4c4c4c"
        },
         ticks: {
            fontColor: "#4c4c4c",
         }
      }]
   },
   plugins: {
      
    datalabels: {
      color: '#4c4c4c',
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
chart5Data = JSON.parse(chart5)
var data5 = [];
var label5 = [];
for(i=0; i<=12; i++) {

  label5.push(chart5Data[i][0]);
  data5.push(chart5Data[i][1]);
}
let myChart5 = new Chart(ctx5, {
  type: 'line',
  data: {
    labels: label5
    ,
    datasets: [{ 
        data: data5,
        borderColor: "#E61616",
        
        fill: true,
      }
    ]
  },
  options: {
    scaleFontColor: "#4c4c4c",
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
          color: "#4c4c4c"
        },
         ticks: {
            fontColor: "#4c4c4c",
         }
      }],
      yAxes: [{
        gridLines: {
          display: false ,
          color: "#4c4c4c"
        },
         ticks: {
            fontColor: "#4c4c4c",
         }
      }]
   },
   plugins: {
      
    datalabels: {
      color: '#4c4c4c',
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