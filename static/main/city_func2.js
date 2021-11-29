(function (func) {
    $.ajax({
        url: "/data/getCity2",
        type: "GET",
        dataType: "json",
        success: function (data) {
            func(data);
        }
    });
})(function (data) {

    var myChart = echarts.init(document.getElementById('chart_city2'), 'infographic');
    
    option = {
        color: ['#003366', '#006699', '#4cabce'],
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'shadow'
            }
        },
        legend: {
            data: ['北京', '成都', '杭州','上海','深圳']
        },
        toolbox: {
            show: true,
            orient: 'vertical',
            left: 'right',
            top: 'center',
            feature: {
                mark: {show: true},
                dataView: {show: true, readOnly: false},
                magicType: {show: true, type: ['line']},
                restore: {show: true},
                saveAsImage: {show: true}
            }
        },
        xAxis: [
            {
                type: 'category',
                axisTick: {show: false},
                data: data.BJ_date
            }
        ],
        yAxis: [
            {
                type: 'value'
            }
        ],
        series: [
            {
                name: '北京',
                type: 'line',
                data: data.BJ_count
            },
            {
                name: '成都',
                type: 'line',
                data: data.CD_count
            },
            {
                name: '杭州',
                type: 'line',
                data: data.HZ_count
            },
            {
                name: '上海',
                type: 'line',
                data: data.SH_count
            },
            {
                name: '深圳',
                type: 'line',
                data: data.SZ_count
            }
        ]
    };


    myChart.setOption(option);
    window.addEventListener("resize", function () {
        myChart.resize();
    });

});