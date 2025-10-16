let charts = {};

function createChart(id, title){
    const ctx = document.getElementById(id).getContext('2d');
    charts[id] = new Chart(ctx,{
        type:'pie',
        data:{
            labels:['Good','Average','Bad'],
            datasets:[{
                label:title,
                data:[0,0,0],
                backgroundColor:['#28a745','#ffc107','#dc3545']
            }]
        },
        options:{ responsive:true }
    });
}

function updateCharts(data){
    for(let meal in data){
        let chart = charts[meal+'Chart'];
        chart.data.datasets[0].data = [data[meal]['Good'],data[meal]['Average'],data[meal]['Bad']];
        chart.update();
    }
}

function fetchChartData(){
    fetch('/get_chart_data')
    .then(res=>res.json())
    .then(data=>updateCharts(data));
}

function submitFeedback(){
    const roll = document.getElementById('roll').value;
    const meal = document.getElementById('meal').value;
    const rating = document.getElementById('rating').value;
    if(!roll){ alert('Enter Roll Number'); return; }

    fetch('/submit_feedback',{
        method:'POST',
        headers:{'Content-Type':'application/json'},
        body:JSON.stringify({roll_no:roll, meal:meal, rating:rating})
    })
    .then(res=>res.json())
    .then(()=>{ fetchChartData(); document.getElementById('roll').value=''; });
}

// Initialize charts
['Breakfast','Lunch','Snacks','Dinner'].forEach(m=>createChart(m+'Chart',m));

// Auto refresh every 5 seconds
setInterval(fetchChartData,5000);
fetchChartData();
// Get current date
let today = new Date();
let dateStr = today.getFullYear() + "-" 
            + String(today.getMonth() + 1).padStart(2, '0') + "-" 
            + String(today.getDate()).padStart(2, '0');

// Display on the page
document.getElementById('current-date').innerText = dateStr;
