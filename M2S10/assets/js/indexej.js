window.onload = function () {
 
    var chart = new CanvasJS.Chart("chartContainer", {
        animationEnabled: true,
        theme: "light2", // "light1", "light2", "dark1", "dark2"
        exportEnabled: true,
        title:{
            text: "Hola mundo en una chart de Canvas jQuery - 2024"
        },
        subtitles: [{
            text: "All Prices are in USD"
        }],
        axisX: {
            valueFormatString: "MMM"
        },
        axisY: {
            prefix: "$",
            title: "Price"
        },
        axisY2: {
            prefix: "$",
            suffix: "bn",
            title: "Revenue & Income",
            tickLength: 0
        },
        toolTip: {
            shared: true
        },
        legend: {
            reversed: true,
            cursor: "pointer",
            itemclick: toggleDataSeries
        },     
        data: [{
            type: "candlestick",
            showInLegend: true,
            name: "Stock Price",
            yValueFormatString: "$#,##0.00",
            xValueFormatString: "MMMM",
            dataPoints: [   // Y: [Open, High ,Low, Close]
                { x: new Date(2016, 0), y: [101.949997, 112.839996, 89.370003, 112.209999] },
                { x: new Date(2016, 1), y: [112.269997, 117.589996, 96.820000, 106.919998] },
                { x: new Date(2016, 2), y: [107.830002, 116.989998, 104.400002, 114.099998] },
                { x: new Date(2016, 3), y: [113.750000, 120.790001, 106.309998, 117.580002] },
                { x: new Date(2016, 4), y: [117.830002, 121.080002, 115.879997, 118.809998] },
                { x: new Date(2016, 5), y: [118.500000, 119.440002, 108.230003, 114.279999] },
                { x: new Date(2016, 6), y: [114.199997, 128.330002, 112.970001, 123.940002] },
                { x: new Date(2016, 7), y: [123.849998, 126.730003, 122.070000, 126.120003] },
                { x: new Date(2016, 8), y: [126.379997, 131.979996, 125.599998, 128.270004] },
                { x: new Date(2016, 9), y: [128.380005, 133.500000, 126.750000, 130.990005] },
                { x: new Date(2016, 10), y: [131.410004, 131.940002, 113.550003, 118.419998] },
                { x: new Date(2016, 11), y: [118.379997, 122.500000, 114.000000, 115.050003] }
            ]
        },
        {
            type: "line",
            showInLegend: true,
            name: "Net Income",
            axisYType: "secondary",
            yValueFormatString: "$#,##0.00bn",
            xValueFormatString: "MMMM",
            dataPoints: [
                { x: new Date(2016, 2), y: 1.510 },
                { x: new Date(2016, 5), y: 2.055 },
                { x: new Date(2016, 8), y: 2.379 },
                { x: new Date(2016, 11), y: 3.568 }
            ]
        },
        {
            type: "line",
            showInLegend: true,
            name: "Total Revenue",
            axisYType: "secondary",
            yValueFormatString: "$#,##0.00bn",
            xValueFormatString: "MMMM",
            dataPoints: [
                { x: new Date(2016, 2), y: 5.382 },
                { x: new Date(2016, 5), y: 6.436 },
                { x: new Date(2016, 8), y: 7.011 },
                { x: new Date(2016, 11), y: 8.809 }
            ]
        }]
    });
    chart.render();
     
    function toggleDataSeries(e) {
        if (typeof (e.dataSeries.visible) === "undefined" || e.dataSeries.visible) {
            e.dataSeries.visible = false;
        } else {
            e.dataSeries.visible = true;
        }
        e.chart.render();
    }
     
    }                            