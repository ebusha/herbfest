$(function () {
  var activities = c3.generate({
    bindto: '#activities-chart',
    data: {
      columns: [
        ['data1', 30],
        ['data2', 120],
      ],
      type : 'donut',
    },
    donut: {
      title: "Iris Petal Width"
    }
  });
  var super_activities = c3.generate({
    bindto: '#superactivities-chart',
    data: {
      columns: [
        ['data1', 30],
        ['data2', 120],
      ],
      type : 'donut',
    },
    donut: {
      title: "Iris Petal Width"
    }
  });
  var super_activities = c3.generate({
    bindto: '#ethno-chart',
    data: {
      columns: [
        ['data1', 30],
        ['data2', 120],
      ],
      type : 'donut',
    },
    donut: {
      title: "Iris Petal Width"
    }
  });
  var super_activities = c3.generate({
    bindto: '#countries-chart',
    data: {
      columns: [
        ['data1', 30],
        ['data2', 120],
      ],
      type : 'donut',
    },
    donut: {
      title: "Iris Petal Width"
    }
  });

})
