(function (func) {
    $.ajax({
        url: "/data/getCompany3",
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

    var myChart = echarts.init(document.getElementById('chart_company3'), 'infographic');

    option = {
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
                radius: '55%',  // 饼图的半径，外半径为可视区尺寸（容器高宽中较小一项）的 55% 长度。
                data:data.company_func3,
                emphasis: {
                    itemStyle: {
                        shadowBlur: 10,
                        shadowOffsetX: 0,
                        shadowColor: 'rgba(0, 0, 0, 0.5)'
                    }
                }
                    // {value:10,name="data.company_func1"},
                    // {value:10,name="data.company_func2"}
                    // {value:data.amount[0], name:data.year[0]},
                    // {value:data.amount[1], name:data.year[1]},
                    // {value:data.amount[2], name:data.year[2]},

                
            }
        ]
    };


    myChart.setOption(option);
    window.addEventListener("resize", function () {
        myChart.resize();
    });

});