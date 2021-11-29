(function (func) {
    $.ajax({
        url: "/data/getAirline3",
        type: "GET",
        dataType: "json",
        success: function (data) {
            func(data);
        }
    });
})(function (data) {

    var myChartBS = echarts.init(document.getElementById('chart_airline3_BS'), 'infographic');
    
    optionBS = {
        title: {
            text: '北京——上海'
        },
        tooltip: {
            trigger: 'item',
            formatter: '{a} <br/>{b} : {c} ({d}%)'
        },
        legend: {
            type: 'scroll',
            orient: 'vertical',
            right: 10,
            top: 20,
            bottom: 20,
            data: data.legendData,
    
            selected: data.selected
        },
        series : [
            {
                name: '总航班数',
                type: 'pie',    // 设置图表类型为饼图
                radius: '40%',  // 饼图的半径，外半径为可视区尺寸（容器高宽中较小一项）的 55% 长度。
                data:data.BS,
                emphasis: {
                    itemStyle: {
                        shadowBlur: 10,
                        shadowOffsetX: 0,
                        shadowColor: 'rgba(0, 0, 0, 0.5)'
                    }
                }
            }
        ]
    };

    myChartBS.setOption(optionBS);

    

    var myChartBC = echarts.init(document.getElementById('chart_airline3_BC'), 'infographic');
    
    optionBC = {
        title: {
            text: '北京——成都'
        },
        tooltip: {
            trigger: 'item',
            formatter: '{a} <br/>{b} : {c} ({d}%)'
        },
        legend: {
            type: 'scroll',
            orient: 'vertical',
            right: 10,
            top: 20,
            bottom: 20,
            data: data.legendData,
    
            selected: data.selected
        },
        series : [
            {
                name: '总航班数',
                type: 'pie',    // 设置图表类型为饼图
                radius: '40%',  // 饼图的半径，外半径为可视区尺寸（容器高宽中较小一项）的 55% 长度。
                data:data.BC,
                emphasis: {
                    itemStyle: {
                        shadowBlur: 10,
                        shadowOffsetX: 0,
                        shadowColor: 'rgba(0, 0, 0, 0.5)'
                    }
                }
                
            }
        ]
    };

    
    myChartBC.setOption(optionBC);


    window.addEventListener("resize", function () {
        myChartBS.resize();
    });
    window.addEventListener("resize", function () {
        myChartBC.resize();
    });

});