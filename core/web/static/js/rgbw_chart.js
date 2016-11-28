$(function () {
    var chart = {
        title: {
            text: 'RGBW color components',
            align: 'left',
            x: 30
        },
        xAxis: {
            type: 'datetime'
        },
        yAxis: {
            plotLines: [{
                value: 0,
                width: 1,
                color: '#808080'
            }],
            title: {
                text: ""
            }
        },

        legend: {
            layout: 'vertical',
            align: 'right',
            verticalAlign: 'middle',
            borderWidth: 0
        },
        series: [{
            name: 'White',
            color: '#2f2f2f'
        }, {
            name: 'Red',
            color: '#ec4a4a'
        }, {
            name: 'Green',
            color: '#35b863'
        }, {
            name: 'Blue',
            color: '#6291d2'
        },],
        credits: {
            enabled: false
        }
    };

    $.getJSON('rgbw_json', function (json_data) {
        chart.series[1].data = json_data.red;
        chart.series[2].data = json_data.green;
        chart.series[3].data = json_data.blue;
        chart.series[0].data = json_data.white;
        Highcharts.chart('rgbw-chart', chart);
    });
});