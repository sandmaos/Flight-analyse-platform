(function (func) {
    $.ajax({
        url: "/data/getCompany4",
        type: "GET",
        dataType: "json",
        success: function (data) {
            // alert(data);
            // alert(data.year);
            // alert(data.amount);
            func(data);
        }
    });
})(function (data) {

    var myChart = echarts.init(document.getElementById('chart_company4'), 'infographic');

    // option = {
    //     xAxis: {
    //         type: 'category',
    //         data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    //     },
    //     yAxis: {
    //         type: 'value'
    //     },
    //     series: [{
    //         data: [120, 200, 150, 80, 70, 110, 130],
    //         type: 'bar',
    //         showBackground: true,
    //         backgroundStyle: {
    //             color: 'rgba(220, 220, 220, 0.8)'
    //         }
    //     }]
    // };

    
    option = {
        color: ['#003366', '#006699', '#4cabce'],
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'shadow'
            }
        },
        legend: {
            data: ['平均准点率']
        },
        toolbox: {
            show: true,
            orient: 'vertical',
            left: 'right',
            top: 'center',
            feature: {
                mark: {show: true},
                dataView: {show: true, readOnly: false},
                magicType: {show: true, type: ['line', 'bar', 'stack', 'tiled']},
                restore: {show: true},
                saveAsImage: {show: true}
            }
        },
        xAxis: [
            {
                type: 'value'
            }
        ],
        yAxis: [
            {
                type: 'category',
                axisTick: {show: false},
                data: data.company
            }
        ],
        series: [
            {
                name: '平均准点率',
                type: 'bar',
                barGap: 0,
                data: data.precision
            }
        ]
    };


    myChart.setOption(option);
    window.addEventListener("resize", function () {
        myChart.resize();
    });

});