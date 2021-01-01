let ctx = document.getElementById('myChart').getContext('2d');
let labels = ['Banking', 'Finances', 'Recreation', 'Food and Drink', 'Shopping', 'Transportation', 'Healthcare'];
let colorHex = ['#FB3640', '#EFCA08', '#43aa8b', '#253d5b','#9f2dbc', '#cd812b', '#000000' ];


let myChart = new Chart(ctx, {
  type: 'pie',
  data: {
    datasets: [{
      data: [10, 10, 10, 10, 10, 10, 10],
      backgroundColor: colorHex
    }],
    labels: labels
  },
  options: {
    responsive: true,
    legend: {
      position: 'bottom'
    },
    plugins: {
      datalabels: {
        color: '#fff',
        anchor: 'end',
        align: 'start',
        offset: -10,
        borderWidth: 2,
        borderColor: '#fff',
        borderRadius: 200,
        backgroundColor: (context) => {
          return context.dataset.backgroundColor;
        },
        font: {
          weight: 'bold',
          size: '10'
        },
        formatter: (value) => {
          return value + ' %';
        }
      }
    }
  }
})
// data: [banking, finances, recreation, foodAndDrink, shopping, transportation, healthcare]