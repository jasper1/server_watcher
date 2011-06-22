loadGoogle();
setInterval(processData, 1000);

function loadGoogle() {
    google.load('visualization', '1', {packages:['gauge']});
    google.setOnLoadCallback(drawChart);
}

function processData() {

    var url = '/js/data?r='+Math.random();

    $.get(url, function(d) {
        d = $.parseJSON(d);
        $.each(d, function(index, value) {
            value.id = index;

            $.each(value, function(i, v) {

                var avg = '';

                if (i == 'memory' || i == 'cpu' ) {

                    var data = new google.visualization.DataTable();
                    data.addColumn('string', 'Label');
                    data.addColumn('number', 'Value');
                    data.addRows(1);
                    data.setValue(0, 0, i);
                    data.setValue(0, 1, v);

                    //var chart = new google.visualization.Gauge(document.getElementById('i' + index + i));
                    //var options = {width: 100, height: 100, redFrom: 90, redTo: 100,
                    //    yellowFrom:75, yellowTo: 90, minorTicks: 5};
                    //chart.draw(data, options);

                } else if (i == 'load_avg') {
                    $('#data-avg' + index).html(v['1'] + ' / ' + v['2'] + ' / ' + v['3'])
                } else if (i == 'disk-space') {
                    $('#data-disk' + index).html(v+'Gb')
                } else if (i == 'status') {

                    var class = 'offline';
                    $('#chart_div' + index).closest('.c').show().parent().find('.unavailable').detach();
                    switch (v) {
                        case -1:
                            class = 'offline'
                            $('#chart_div' + index).closest('.c').hide().parent().append('<div class="unavailable">Сервер недоступен</div>');
                            break
                        case 0:
                            class = 'red'
                            break
                        case 1:
                            class = 'orange'
                            break
                        case 2:
                            class = 'green'
                            break

                    }

                    $('#chart_div' + index).closest('.i').find('.status').removeClass('offline red orange yellow green').addClass(class);
//                    $('.h.attention').removeClass('attention');
//                    $('.red').closest('.h').addClass('attention');
                    
                    
                    $('.h.attention').removeClass('attention');
                    $('.i.attention-body').removeClass('attention-body');
                    $('.red').closest('.h').addClass('attention');
                    $('.red').closest('.i').addClass('attention-body');
                }
                ;
            });

        })

    });
}


function drawChart() {
    var url = '/js/data';
    
    $.get(url, function(data){
        makeChart(data)
    });
//    makeChart(rqst)

}

function makeChart(d) {
    var d = $.parseJSON(d);

    $.each(d, function(index, value){
        $('#chart_div' + index).text('');
        value.id = index;
        var element = $('#chart_div' + index);

        $('.indicators').append($('#indicator-tpl').tmpl(value));

        $.each(value, function(i, v){

            var avg = '';

            if(i == 'memory' || i == 'cpu' ) {

                var data = new google.visualization.DataTable();
                data.addColumn('string', 'Label');
                data.addColumn('number', 'Value');
                data.addRows(1);
                data.setValue(0, 0, i);
                data.setValue(0, 1, v);

                $('#chart_div' + index).append('<div class="chart" id=i' + index + i + '></div>')



                var chart = new google.visualization.Gauge(document.getElementById('i' + index + i));
                var options = {width: 100, height: 100, redFrom: 90, redTo: 100,
                    yellowFrom:75, yellowTo: 90, minorTicks: 5};
                chart.draw(data, options);

            } else if(i == 'load_avg'){
                $('#data-avg'+index).html(v['1'] + ' / ' + v['2'] + ' / ' + v['3'])
            } else if(i == 'status') {

                var class = 'offline';
                $('#chart_div' + index).closest('.c').show();
                switch(v){
                    case -1:
                        class = 'offline'
                        $('#chart_div' + index).closest('.c').hide().parent().append('<div class="unavailable">Сервер недоступен</div>');
                        break
                    case 0:
                        class = 'red'

                        break
                    case 1:
                        class = 'orange'
                        break
                    case 2:
                        class = 'green'
                        break

                }

                $('#chart_div' + index).closest('.i').find('.status').removeClass('offline red orange yellow green').addClass(class);
                $('.h.attention').removeClass('attention');
                $('.i.attention-body').removeClass('attention-body');
                $('.red').closest('.h').addClass('attention');
                $('.red').closest('.i').addClass('attention-body');

            };
        });

    })

}