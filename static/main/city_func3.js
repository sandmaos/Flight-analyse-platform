(function (func) {
    $.ajax({
        url: "/data/getCity3",
        type: "GET",
        dataType: "json",
        success: function (data) {
            func(data);
        }
    });
})(function (data) {

    var myChart= echarts.init(document.getElementById('chart_city3'), 'infographic');

    option = {
        color: ['#003366'],
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'shadow'
            }
        },
        legend: {
            data: ['城市吞吐量']
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
                type: 'category',
                axisTick: {show: false},
                data: data.city
            }
        ],
        yAxis: [
            {
                type: 'value'
            }
        ],
        series: [
            {
                name: '城市吞吐量',
                type: 'bar',
                barGap: 0,
                data: data.sum
            }
        ]
    };


    myChart.setOption(option);

    window.addEventListener("resize", function () {
        myChart.resize();
    });

});