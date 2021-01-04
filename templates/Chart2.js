let ctx = document.getElementById('myChart2').getContext('2d');
let labels = ['Banking', 'Finances', 'Shopping', 'Recreation', 'Healthcare', 'Transportation', 'Food and Drink'];
let colorHex = ['#FB3640', '#86A9C5', '#286CA1', '#77FAC', '#1C203D', '#798E9C', '#2A303D'];

let myChart2 = new Chart(ctx, {
  
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