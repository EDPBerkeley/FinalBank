let ctx1 = document.getElementById("myChart").getContext('2d');
let labels = ['Banking', 'Finances', 'Shopping', 'Recreation', 'Healthcare', 'Transportation', 'Food and Drink'];
let colorHex = ['#FB3640', '#86A9C5', '#286CA1', '#77FAC', '#1C203D', '#798E9C', '#2A303D'];

let myChart = new Chart(ctx1, {
  
  type: 'pie',
  data: {
    datasets: [{
      data: [10, 10, 10, 10, 10, 10, 10],
      backgroundColor: colorHex,
      borderWidth: [0,0,0,0,0,0,0]
    }],
    labels: labels,
  
  },
  options: {
    responsive: false,
    legend: {
      position: 'bottom'
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
let myChart2 = new Chart(ctx2, {
  
  type: 'pie',
  data: {
    datasets: [{
      data: [10, 10, 10, 10, 10, 10, 10],
      backgroundColor: colorHex,
      borderWidth: [0,0,0,0,0,0,0]
    }],
    labels: labels2,
  
  },
  options: {
    responsive: false,
    legend: {
      position: 'bottom'
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

let ctx3 = document.getElementById('myChart3').getContext('2d');
let labels3 = ['Banking', 'Finances', 'Shopping', 'Recreation', 'Healthcare', 'Transportation', 'Food and Drink'];
let colorHex3 = ['#FB3640', '#86A9C5', '#286CA1', '#77FAC', '#1C203D', '#798E9C', '#2A303D'];
let myChart3 = new Chart(ctx3, {
  
  type: 'pie',
  data: {
    datasets: [{
      data: [10, 10, 10, 10, 10, 10, 10],
      backgroundColor: colorHex,
      borderWidth: [0,0,0,0,0,0,0]
    }],
    labels: labels3,
  
  },
  options: {
    responsive: false,
    legend: {
      position: 'bottom'
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


let ctx4 = document.getElementById('myChart4').getContext('2d');
let labels4 = ['Banking', 'Finances', 'Shopping', 'Recreation', 'Healthcare', 'Transportation', 'Food and Drink'];
let colorHex4 = ['#FB3640', '#86A9C5', '#286CA1', '#77FAC', '#1C203D', '#798E9C', '#2A303D'];
let myChart4 = new Chart(ctx4, {
  
  type: 'pie',
  data: {
    datasets: [{
      data: [10, 10, 10, 10, 10, 10, 10],
      backgroundColor: colorHex,
      borderWidth: [0,0,0,0,0,0,0]
    }],
    labels: labels4,
  
  },
  options: {
    responsive: false,
    legend: {
      position: 'bottom'
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


let ctx5 = document.getElementById('myChart5').getContext('2d');
let labels5 = ['Banking', 'Finances', 'Shopping', 'Recreation', 'Healthcare', 'Transportation', 'Food and Drink'];
let colorHex5 = ['#FB3640', '#86A9C5', '#286CA1', '#77FAC', '#1C203D', '#798E9C', '#2A303D'];
let myChart5 = new Chart(ctx5, {
  
  type: 'pie',
  data: {
    datasets: [{
      data: [10, 10, 10, 10, 10, 10, 10],
      backgroundColor: colorHex,
      borderWidth: [0,0,0,0,0,0,0]
    }],
    labels: labels5,
  
  },
  options: {
    responsive: false,
    legend: {
      position: 'bottom'
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


let ctx6 = document.getElementById('myChart6').getContext('2d');
let labels6 = ['Banking', 'Finances', 'Shopping', 'Recreation', 'Healthcare', 'Transportation', 'Food and Drink'];
let colorHex6 = ['#FB3640', '#86A9C5', '#286CA1', '#77FAC', '#1C203D', '#798E9C', '#2A303D'];
let myChart6 = new Chart(ctx6, {
  
  type: 'pie',
  data: {
    datasets: [{
      data: [10, 10, 10, 10, 10, 10, 10],
      backgroundColor: colorHex,
      borderWidth: [0,0,0,0,0,0,0]
    }],
    labels: labels6,
  
  },
  options: {
    responsive: false,
    legend: {
      position: 'bottom'
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