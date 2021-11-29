(function (func) {
    $.ajax({
        url: "/data/getCity1",
        type: "GET",
        dataType: "json",
        success: function (data) {
            // alert(data.year);
            // alert(data.amount);
            func(data);
        }
    });
})(function (data) {

    var myChartNorth = echarts.init(document.getElementById('chart_city1_north'), 'infographic');

    optionNorth = {
        color: ['#003366'],
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'shadow'
            }
        },
        legend: {
            data: ['北方主要城市吞吐量']
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
                data: data.north_city
            }
        ],
        yAxis: [
            {
                type: 'value'
            }
        ],
        series: [
            {
                name: '北方主要城市吞吐量',
                type: 'bar',
                barGap: 0,
                data: data.north_sum
            }
        ]
    };

    var myChartSouth = echarts.init(document.getElementById('chart_city1_south'), 'infographic');

    optionSouth = {
        color: ['#003366'],
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'shadow'
            }
        },
        legend: {
            data: ['南方主要城市吞吐量']
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
                data: data.south_city
            }
        ],
        yAxis: [
            {
                type: 'value'
            }
        ],
        series: [
            {
                name: '南方主要城市吞吐量',
                type: 'bar',
                barGap: 0,
                data: data.south_sum
            }
        ]
    };

    myChartNorth.setOption(optionNorth);
    myChartSouth.setOption(optionSouth);

    window.addEventListener("resize", function () {
        myChart.resize();
    });

});