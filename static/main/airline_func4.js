(function (func) {
    $.ajax({
        url: "/data/getAirline4",
        type: "GET",
        dataType: "json",
        success: function (data) {
            func(data);
        }
    });
})(function (data) {

    var myChartBS = echarts.init(document.getElementById('chart_airline4_BS'), 'infographic');
    
    optionBS = {
        color: ['#003366', '#006699', '#4cabce'],
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'shadow'
            }
        },
        legend: {
            data: ['北京——上海平均准点率']
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
                data: data.BS_company
            }

        ],
        series: [
            {
                name: '北京——上海平均准点率',
                type: 'bar',
                barGap: 0,
                data: data.BS_precision
            }
        ]
    };

    var myChartBC = echarts.init(document.getElementById('chart_airline4_BC'), 'infographic');
    
    optionBC = {
        color: ['#003366', '#006699', '#4cabce'],
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'shadow'
            }
        },
        legend: {
            data: ['北京——成都平均准点率']
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
                data: data.BC_company
            }

        ],
        series: [
            {
                name: '北京——成都平均准点率',
                type: 'bar',
                barGap: 0,
                data: data.BC_precision
            }
        ]
    };


    myChartBS.setOption(optionBS);
    myChartBC.setOption(optionBC);


    window.addEventListener("resize", function () {
        myChart.resize();
    });

});