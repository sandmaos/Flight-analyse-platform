(function (func) {
    $.ajax({
        url: "/data/getAirline2",
        type: "GET",
        dataType: "json",
        success: function (data) {
            func(data);
        }
    });
})(function (data) {

    var myChart = echarts.init(document.getElementById('chart_airline2'), 'infographic');
    
    option = {
        title: {
            text: '北京——成都价格变化'
        },
        color: ['#003366', '#006699', '#4cabce'],
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'shadow'
            }
        },
        legend: {
            data: ['上午', '下午','晚上']
        },
        toolbox: {
            show: true,
            orient: 'vertical',
            left: 'right',
            top: 'center',
            feature: {
                mark: {show: true},
                dataView: {show: true, readOnly: false},
                magicType: {show: false, type: ['line']},
                restore: {show: true},
                saveAsImage: {show: true}
            }
        },
        xAxis: [
            {
                type: 'category',
                axisTick: {show: false},
                data: data.BC_date
            }
        ],
        yAxis: [
            {
                type: 'value'
            }
        ],
        series: [
            {
                name: '上午',
                type: 'line',
                barGap: 0,
                data: data.price1
            },
            {
                name: '下午',
                type: 'line',
                data: data.price2
            },
            {
                name: '晚上',
                type: 'line',
                data: data.price3
            }
        ]
    };


    myChart.setOption(option);
    window.addEventListener("resize", function () {
        myChart.resize();
    });

});